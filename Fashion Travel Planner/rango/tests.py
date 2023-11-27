from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Tip, UserProfile,Season,Outfit, List, Item
from rango.forms import UserForm, UserProfileForm, TipForm, ListForm, ItemForm, OutfitForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse
from django.apps import apps

#Creating test cases for django unit testing here.

class AppsTest(TestCase):
    #testing to ensure the app is named rango.
    def test_rango_config_name(self):
        rango_app_config = apps.get_app_config('rango')
        self.assertEqual(rango_app_config.name, 'rango')

class ModelTests(TestCase):
    #testing the models of the database.
    def setUp(self):
        #Creating objects for the models in the database
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@email.com',
        )

        self.user_profile = UserProfile.objects.create(
            user=self.user,
            telephone='1234567890',
        )
        
        self.category = Category.objects.create(
            name='Test Category'
        )

        self.tip = Tip.objects.create(
            category=self.category,
            title='Test Tip',
            content='This is a test tip.',
            likes=5,
        )

        self.season_summer = Season.objects.create(
            name='Summer',
            maxtemp=30.0,
            mintemp=20.0,
        )

        self.outfit_summer = Outfit.objects.create(
            season=self.season_summer,
            username=self.user_profile,
            name='Summer Outfit',
            description='This is a summer outfit.',
        )

        self.list = List.objects.create(
            name='Test List',
            username=self.user_profile,
        )

        self.item = Item.objects.create(
            list=self.list,
            title='Test Item',
            completed=False,
        )

    #checking if the object created currently exist in the database
    def test_category_model(self):
        self.assertEqual(self.category.slug, 'test-category')
        self.assertEqual(str(self.category), 'Test Category')

    def test_slug_category(self):
        category = Category(name='Random Test Category')
        category.save()
        self.assertEqual(category.slug, 'random-test-category')

    def test_tip_model(self):
        self.assertEqual(self.tip.likes, 5)
        self.assertEqual(str(self.tip), 'Test Tip')

    def test_user_profile_model(self):
        self.assertEqual(self.user_profile.telephone, '1234567890')
        self.assertEqual(str(self.user_profile), 'testuser')

    def test_list_model(self):
        self.assertEqual(self.list.slug, 'test-list')
        self.assertEqual(str(self.list), 'Test List')

    def test_slug_List(self):
        list = Category(name='Random Test List')
        list.save()
        self.assertEqual(list.slug, 'random-test-list')

    def test_item_model(self):
        self.assertFalse(self.item.completed)
        self.assertEqual(str(self.item), 'Test Item')
    
    def test_season_model(self):
        self.assertEqual(self.season_summer.name, 'Summer')
        self.assertEqual(float(self.season_summer.maxtemp), 30.0)
        self.assertEqual(float(self.season_summer.mintemp), 20.0)
        self.assertEqual(str(self.season_summer), 'Summer')

    def test_outfit_model(self):
        self.assertEqual(self.outfit_summer.season, self.season_summer)
        self.assertEqual(self.outfit_summer.username, self.user_profile)
        self.assertEqual(self.outfit_summer.name, 'Summer Outfit')
        self.assertEqual(self.outfit_summer.description, 'This is a summer outfit.')
        self.assertEqual(str(self.outfit_summer), 'Summer Outfit')

class FormTests(TestCase):
    #testing if the forms created function correctly for different scenarios.
    def setUp(self):
        #created pre existing category and season as they are foreign keys.
        self.test_category = Category.objects.create(name='Test Category')
        self.test_season = Season.objects.create(name='Test Season')

    def test_user_form_valid_data(self):
        #test to ensure if valid user data is provided form is valid.
        form = UserForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword123'
        })
        self.assertTrue(form.is_valid())

    def test_user_form_invalid_data(self):
        #test to ensure if invalid user data is provided form is invalid.
        form = UserForm(data={}) #data is empty
        self.assertFalse(form.is_valid())


    def test_user_profile_form_valid_data(self):
        #test to ensure if valid userprofile data is provided form is valid.
        form = UserProfileForm(data={
            'telephone': '1234567890'
        })
        self.assertTrue(form.is_valid())

    def test_user_profile_form_invalid_data(self):
        #test to ensure if invalid userprofile data is provided form is invalid.
        form = UserProfileForm(data={}) #data is empty
        self.assertFalse(form.is_valid())
   
    def test_tip_form_valid_data(self):
        #test to ensure if valid tip data is provided form is valid.
        form = TipForm(data={
            'category': self.test_category.pk,
            'title': 'Test Tip',
            'img': '',
            'content': 'This is a test tip content.',
            'likes': 10,
        })
        self.assertTrue(form.is_valid())

    def test_tip_form_invalid_data(self):
        #test to ensure if invalid tip data is provided form is invalid.
        form = TipForm(data={}) #data is empty
        self.assertFalse(form.is_valid())
   
    def test_list_form_valid_data(self):
        #test to ensure if valid list data is provided form is valid.
        form = ListForm(data={
            'name': 'Test List',  
        })
        self.assertTrue(form.is_valid())

    def test_list_form_invalid_data(self):
        #test to ensure if invalid list data is provided form is invalid.
        form = ListForm(data={}) #data is missing
        self.assertFalse(form.is_valid())

    def test_item_form_valid_data(self):
        #test to ensure if valid item data is provided form is valid.
        form = ItemForm(data={
            'title': 'Test Item', 
        })
        self.assertTrue(form.is_valid())

    def test_item_form_invalid_data(self):
        #test to ensure if invalid item data is provided form is invalid.
        form = ItemForm(data={}) #data is missing
        self.assertFalse(form.is_valid())
  
    def test_outfit_form_valid_data(self):
        #test to ensure if valid outfit data is provided form is valid.
        form = OutfitForm(data={
            'season': self.test_season.pk,
            'name': 'Test Outfit',
            'image': '',
            'description': 'This is a test outfit description.',
        })
        self.assertTrue(form.is_valid())

    def test_outfit_form_invalid_data(self):
        #test to ensure if invalid outfit data is provided form is invalid.
        form = OutfitForm(data={}) #data is empty
        self.assertFalse(form.is_valid())

class UrlTests(TestCase):
    #testing if the url render the correct template
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'rango/index.html')
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('rango:register'))
        self.assertTemplateUsed(response, 'rango/register.html')
        self.assertEqual(response.status_code, 200)

    def test_tips_view(self):
        response = self.client.get(reverse('rango:tips'))
        self.assertTemplateUsed(response, 'rango/tips.html')
        self.assertEqual(response.status_code, 200)

    def test_outfit_view(self):
        response = self.client.get(reverse('rango:outfit'))
        self.assertTemplateUsed(response, 'rango/outfit.html')
        self.assertEqual(response.status_code, 200)

    def test_admin_view(self):
        response = self.client.get(reverse('rango:admin'))
        self.assertTemplateUsed(response, 'rango/admin.html')
        self.assertEqual(response.status_code, 200)

    def test_add_outfit_view(self):
        response = self.client.get(reverse('rango:add_outfit'))
        self.assertTemplateUsed(response, 'rango/addoutfit.html')
        self.assertEqual(response.status_code, 200)

class TemplateTests(TestCase):
    #testing if the template generate corrent content.
    def test_index_view_content(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'EXPLORE YOUR FASHION')

    def test_register_view_content(self):
        response = self.client.get(reverse('rango:register'))
        self.assertContains(response, 'Create an Account')
        self.assertContains(response, 'Sign In')

    def test_tips_view_content(self):
        response = self.client.get(reverse('rango:tips'))
        self.assertContains(response, 'Fashion & Travel Tips')

    def test_outfit_view_content(self):
        response = self.client.get(reverse('rango:outfit'))
        self.assertContains(response, 'Enter city:')

    def test_admin_view_content(self):
        response = self.client.get(reverse('rango:admin'))
        self.assertContains(response, 'Add Tips')
        self.assertContains(response, 'Edit Tips')

    def test_add_outfit_view_content(self):
        response = self.client.get(reverse('rango:add_outfit'))
        self.assertContains(response, 'Upload Outfits')

class RegisterViewTests(TestCase):
    #testing if the registration function is correctly implemented.
    def test_valid_register_view(self):
        #creating valid test data
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com',
            'telephone':'+44123456789',
        }

        response = self.client.post(reverse('rango:register'), data)
       
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['registered'])  #asserting registration is successfull

    def test_invalid_register_view(self):
        #creating invalid test data as its empty
        data = {}
        response = self.client.post(reverse('rango:register'), data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['registered']) #asserting resgiration is unsuccessfull

    def test_register_view_get_request(self):
        #testing the get request to ensure the forms are displayed.
        response = self.client.get(reverse('rango:register'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['user_form'], UserForm)
        self.assertIsInstance(response.context['profile_form'], UserProfileForm)

class LoginViewTests(TestCase):
    #testing the login function 
    def test_valid_login_view(self):
        #creating pre existing user data
        user=User.objects.get_or_create(username="testuser",email="testuser@example.com")[0]
        user.set_password('testpassword')
        user.save()
        
        test_user_object=user
        #testing succesful login using the user data
        response=self.client.post(reverse('rango:login'),{'username':'testuser','password':'testpassword'})
        try:
            self.assertEqual(test_user_object.id,int(self.client.session['_auth_user_id']),f"2")
        except KeyError:
            self.assertTrue(False)
        self.assertEqual(response.status_code,302,f"3")
        self.assertEqual(response.url,reverse('rango:index'),f"4")

    def test_invlaid_login_view(self):
        #creating pre existing user data
        user=User.objects.get_or_create(username="testuser",email="testuser@example.com")[0]
        user.set_password('testpassword')
        user.save()

        response = self.client.post(reverse('rango:login'), {'username':'testuser','password':'wrongpassword'})
        #testing unsuccesful login using the wrong password
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid login details supplied.")

class LogoutViewTest(TestCase):
    #testing the logout function
    def test_valid_logout_view(self):
        #creating pre existing user data
        user=User.objects.get_or_create(username="testuser",email="testuser@example.com")[0]
        user.set_password('testpassword')
        user.save()
        
        test_user_object=user
        #valid login using the user data
        self.client.login(username='testuser',password='testpassword')
        
        #testing succesful logout
        try:
            self.assertEqual(test_user_object.id,int(self.client.session['_auth_user_id']))
        except KeyError:
            self.assertTrue(False)

        response=self.client.get(reverse('rango:logout'))
        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url,reverse('rango:index'))
        self.assertTrue('_auth_user_id' not in self.client.session)

class TipsViewTests(TestCase):
    #testing the the tips view
    def setUp(self):
        #creating pre existing category data 
        self.category = Category.objects.create(
            name='Test Category'
        )

        #dummy image to create tips
        image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x04\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x0fIDAT\x08\xd7c\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xde\xfe\xdd\xe9\xfe\x1b\xd4\x00\x00\x00\x00IEND\xaeB`\x82'
        dummy_image = SimpleUploadedFile(name='test_image.png', content=image_data, content_type='image/png')
        
        #creating pre existing tip data
        self.tip = Tip.objects.create(
            category=self.category,
            title='Test Tip',
            img=dummy_image,
            content='This is a test tip.',
            likes=5,
        )

    def test_tips_view(self):
        #testing the tip sort view function to get tips that belong to the category provided
        response = self.client.get(reverse('rango:tips'), {'category': 'Test Category'})
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rango/tips.html')
        #checking if the correct number of tips are shown of the provided category.
        num_tips = len(response.context['tips'])
        self.assertEquals(num_tips, 1)

    def test_tips_invalid_view(self):
        #testing the tip function when invalid category is provided 
        response = self.client.get(reverse('rango:tips'), {'category': 'Invalid Category'})

        #ensuring no tips are displayed when wrong category is entered.
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tips'], Tip.objects.none())

    def test_like_tip_view(self):
        #testing the like funciton in the view
        response = self.client.get(reverse('rango:like_tip'), {'tip_id': self.tip.id})
        self.assertEqual(response.status_code, 200)

        #ensuring the like count is increased when like button is clicked
        expected_likes = self.tip.likes + 1
        self.assertEqual(int(response.content), expected_likes)
        self.tip.refresh_from_db()
        self.assertEqual(self.tip.likes, expected_likes)