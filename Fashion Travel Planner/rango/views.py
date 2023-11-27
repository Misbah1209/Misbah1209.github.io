import json
from django.http import HttpResponse
from django.http import JsonResponse
from rango.forms import UserForm, UserProfileForm, TipForm, ListForm, ItemForm, OutfitForm
from django.urls import reverse
from rango.models import Category, Tip, Season, List, Item, Outfit
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'rango/index.html')

def outfit(request):
    #criteria to find season according to temperature.
    season_mapping = {
        (26, 55): 'Summer',
        (21, 25): 'Spring',
        (11, 20): 'Autumn',
        (0, 10): 'Winter' 
    }

    if request.method == 'POST':
        #if form is submitted get data.
        temperature = int(request.POST.get('temperature', 0))
        rain = float(request.POST.get('rain', 0))

        #if rain data is more that 0 then display rain outfits else find season according temperature.
        if rain > 0:
            outfits = Outfit.objects.filter(season__name='Rainy')
            return render(request, 'rango/outfit.html', {'outfits': outfits, 'hide_weatherapp': True}) 
        else:
            for temp_range, name in season_mapping.items():
                if temp_range[0] <= temperature <= temp_range[1]:
                    season_name = name
                    break
        outfits = Outfit.objects.filter(season__name=season_name)
        return render(request, 'rango/outfit.html', {'outfits': outfits,'hide_weatherapp': True}) 
    else:
        outfits = Outfit.objects.filter(season__name='Summer')

    return render(request, 'rango/outfit.html', {'outfits': outfits})

def register(request):
    registered = False
    if request.method == 'POST':
        #if form is submitted get data.
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #form data is valid
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            #save the user data in the database succesfully.
            registered = True
        else:
            print(user_form.errors, profile_form.errors)#print errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()#display the registration form

    return render(request,'rango/register.html', context = {'user_form': user_form,
                                                            'profile_form': profile_form,
                                                            'registered': registered})

def user_login(request):
    if request.method == 'POST': 
        #if form is submitted get data.    
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)#check is user exist

        if user: 
            if user.is_active:#login succesfull
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")     
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:     
        return render(request, 'rango/register.html') 

@login_required
def user_logout(request):
    #logout the currest logged in user
    logout(request)
    return redirect(reverse('rango:index'))

def tips(request):
    #get all categories and tips 
    category_list = Category.objects.all
    tip_list = Tip.objects.all

    category = request.GET.get('category')
    if category == None:
        #if no category is specified display all tips
        tip_list = Tip.objects.all
    else:
        tip_list = Tip.objects.filter(category__name=category)#filter tip as per category

    return render(request, 'rango/tips.html', context = {'categories': category_list,'tips': tip_list})

class LikeTipsView(View):
    def get(self, request):
        #get tip id of liked tip
        tip_id = request.GET['tip_id']
        try:
            tip = Tip.objects.get(id=int(tip_id))
        except Tip.DoesNotExist:
            return HttpResponse(-1,content_type='text/plain')
        except ValueError:
            return HttpResponse(-1,content_type='text/plain')
        #increment the like count of the tip
        tip.likes = tip.likes + 1
        tip.save()#save the updated like count in the database
        
        return HttpResponse(tip.likes,content_type='text/plain')

def admin(request):
    #get all the tips
    tip_list = Tip.objects.all
    #display the add tip and edit tip form
    addform = TipForm()
    editform=TipForm()
    return render(request, 'rango/admin.html',context = {'tips': tip_list, 'addform': addform,'editform': editform})

def add_tip(request):
    tip_list = Tip.objects.all#get all tips
    if request.method=='POST':
        #if form is submitted get data.
        form = TipForm(request.POST, request.FILES)
        if form.is_valid():
            #if orm data is valid; add tip to the database
            form.save()
            return redirect('/rango/admin/')
        else:
            print(form.errors)
    
    return render(request,'rango/admin.html',context = {'tips': tip_list,'form': form})

def edit_tip(request,pk):
    tip_list = Tip.objects.all()#get all tips
    tip = Tip.objects.get(id=pk)
    editform = TipForm(instance=tip)#load the form with details

    if request.method == 'POST':
        #if form is submitted get data.
        editform = TipForm(request.POST, request.FILES, instance=tip)
        if editform.is_valid():
            editform.save()#update tip details in database
            return redirect('/rango/admin/')
        else:
            print(editform.errors)
    
    return render(request,'rango/admin.html',context = {'tips': tip_list,'editform': editform})

def delete_tip(request,pk):
    #get tip id and find the tip in the database
    tip = Tip.objects.get(id=pk)
    tip.delete()#delete tip with matching id
    return redirect('/rango/admin/')

def profile(request):
    #get all outfit of the logged in user
    outfit_list = Outfit.objects.filter(username=request.user.userprofile)
    return render(request, 'rango/myprofile.html', context = {'outfits': outfit_list})

@login_required
def lists(request):
    list = List.objects.filter(username=request.user.userprofile)

    if request.method == 'POST':
        #if form is submitted get data.
        addlistform = ListForm(request.POST)

        if addlistform.is_valid():
            #if the form data is valid
            newlist = addlistform.save(commit=False)
            newlist.username = request.user.userprofile#get the logged in user username
            newlist.save() #save the list with the username
            list = List.objects.filter(username=request.user.userprofile)#get all the list of the logged in user
    else:
        addlistform = ListForm()#display form

    return render(request, 'rango/list.html',context = {'lists': list ,'addlistform': addlistform})

@login_required
def items(request, list_id):
    
    if request.method == 'POST':
            #if form is submitted get data.
            additemform = ItemForm(request.POST)
            list_instance = List.objects.get(id=list_id)#get list id

            if additemform.is_valid():
                #if the form data is valid
                newitem = additemform.save(commit=False)
                newitem.list = list_instance
                newitem.save()#add the item to the list
                list_instance = List.objects.get(id=list_id)
                items = Item.objects.filter(list=list_instance)#get all the items in the list
    else:
        list_instance = List.objects.get(id=list_id)# get the specified list wit id
        items = Item.objects.filter(list=list_instance)#get all items if the list
        additemform = ItemForm()#display form

    return render(request, 'rango/listitems.html', {'lists': list_instance, 'items': items,'additemform': additemform})

@login_required
def delete_list(request, list_id):
    #get list id and find the list in the database
    list_instance = get_object_or_404(List, id=list_id, username=request.user.userprofile)
    list_instance.delete()#delete list with matching id
    return redirect( 'rango:lists')

def delete_item(request, item_id):
    #get item id and find the item in the database
    item = get_object_or_404(Item, id=item_id)
    list_id = item.list.id 
    item.delete()#delete item with matching id
    return redirect('rango:items', list_id=list_id)
  
@csrf_exempt
def update_item(request, item_id):
    if request.method == 'POST':
        try:
            item = Item.objects.get(id=item_id)#get data of the item id.
        except Item.DoesNotExist:
            #if item doesnot exist show error.
            return JsonResponse({'message': 'Item not found.'}, status=404)

        #load the data into the form
        data = json.loads(request.body)
        is_completed = data.get('completed', False)

        item.completed = is_completed
        item.save()#save form with updated data

        return JsonResponse({'message': 'Item status updated successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)
    
def add_outfit(request):
    #display outfit form
    form=OutfitForm()
    if request.method=='POST':
        #snce the form is submitted, get the data inputted
        form = OutfitForm(request.POST, request.FILES)
        if form.is_valid():
            #validate form data
            newOutfit = form.save(commit=False)
            newOutfit.username = request.user.userprofile
            newOutfit.save()# if data is valid add the outfitto the database
            return redirect('/rango/profile/')
        else:
            print(form.errors)
    
    return render(request,'rango/addoutfit.html',context = {'form': form})

def delete_outfit(request,pk):
    #get outfit id and find the outfit in the database
    outfit = Outfit.objects.get(id=pk)
    outfit.delete()#delete outfit with matching id
    return redirect('/rango/profile/')