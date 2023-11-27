import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','development_project.settings')

import django
django.setup()
from rango.models import Category, Tip,Season, Outfit, UserProfile
from django.contrib.auth.models import User

def populate():
    fashion_tips = [
        {'title': 'Get more basics in your closet',
        'img':'tips_image/f1.jpg',
        'content':'Choose several neutral-coloured tops and pants that can mix and match with other pieces to create multiple outfits. Stop spending money on trendy pieces that are just going to go out of style in a season. For colder climates, pack clothes that you can layer for varying degrees of weather, such as long-sleeved shirts and light coats.',
        'likes':245},
        {'title': 'Use your neck to check if pants will fit',
        'img':'tips_image/f2.jpg',
        'content':'It can be exhausting trying to find your pants size. Hold both sides of the waist in either hand and wrap the waistband around your neck. If your hands just touch at the back, they will fit. If the pants don’t reach or your hands overlap, they’ll be too small or big (respectively).',
        'likes':123},
        {'title': 'Use a hair elastic to keep your belt flat',
        'img':'tips_image/f3.jpg',
        'content':'Is your belt too long? Do you have that awkward “extra belt” hanging over between your belt loops? Get a tiny elastic hair tie that matches your belt color. Pull the hair tie between your belt and pants, so it’s behind two layers of belt on top. That creates another loop that will keep your belt flat to your pants.',
        'likes':357}, 
        {'title': 'Use ice cubes to iron your clothes',
        'img':'tips_image/f4.jpg',
        'content':'Throw three or four ice cubes into your dryer along with the wrinkled garment. Let it run for 10-15 minutes. As the ice cubes melt in the dryer, they’ll create steam that can help de-wrinkle your clothes. If you don’t have any ice cubes, you can also throw a wet hand towel in with your clothes for a similar effect.',
        'likes':432},
        {'title': 'Stop hanging your sweaters',
        'img':'tips_image/f5.jpg',
        'content':'Fold your sweaters. Gravity pulls on the weight of your sweaters, and it can cause them to stretch out or leave you with misshapen shoulders. Keep your sweaters folded neatly and stacked atop one another to best preserve their material and structure',
        'likes':653}, 
    ]
    
    travel_tips = [
       {'title': 'Employ more space-saving methods',
        'img':'tips_image/t1.jpg',
        'content':'To save some space and keep things light, consider packing travel-sized toiletries to replace the full-sized versions. A toiletry bag with pockets will make organizing and packing those items much easier! Try rolling your clothing items instead of folding them, you’ll save even more space because it removes extra air and distributes weight more evenly',
        'likes':823},
        {'title': 'Pack more shoes by using a shower cap',
        'img':'tips_image/t2.jpg',
        'content':'You think you have plenty of space in your suitcase…until it’s time to pack shoes to match every outfit you have packed. Instead of sacrificing a pair or two, you can squeeze them in with your clothes by wrapping them in shower caps. Covering the bottoms of your shoes like this avoids getting your clothes dirty or scuffed.',
        'likes':483},
        {'title': 'Mark your bags as fragile',
        'img':'tips_image/t3.jpg',
        'content':'By doing this you ensure that your belongings are given the VIP treatment and you won’t have to wait for long to collect your luggage - anything marked fragile gets to the top of the pile in storage and sent out in the first batch! To process this, just request for a ‘fragile’ sticker at the counter without paying a penny more.',
        'likes':145}, 
        {'title': 'Use zip lock bags to protect your toiletries',
        'img':'tips_image/t4.png',
        'content':'Yes, zip lock bags have more than one use. They will keep the toiletry liquids from exploding and spilling all over your bag on the flight back home. Make sure to wrap the bottles well.',
        'likes':538},
        {'title': 'Pack a universal adapter',
        'img':'tips_image/t5.jpg',
        'content':'If you do not want to end up at a spot with plug points that aren’t compatible with your electronic devices, invest in a good universal adapter or plug converter with USB ports that works in all countries.',
        'likes':765}, 
    ]
        
    outfits_data = [
        {
            'season': 'Summer',
            'username': 'misbah',
            'name': 'Floral Breeze Dress',
            'image': 'outfits_image/summer1.jpg',
            'description': 'A breezy and vibrant sundress with a floral print, paired with comfortable sneakers. Complete the look with trendy sunglasses and a chic tote bag for a day at the beach or a casual stroll.'
        },
        {
            'season': 'Summer',
            'username': 'misbah',
            'name': 'Classic Denim Chic',
            'image': 'outfits_image/summer2.jpg',
            'description': 'A classic grey cotton crop top along with high-waisted denim shorts, complemented by hightop sneakers. Accessorize with a dainty necklace and a lightweight scarf for an effortlessly cool and casual summer outfit.'
        },
        {
            'season': 'Summer',
            'username': 'misbah',
            'name': 'Summer Elegance',
            'image': 'outfits_image/summer3.jpg',
            'description': 'A flowy, strappy-shoulder maxi dress in a pastel hue, adorned with delicate ruffles and embroidery. Wear with sporty shoes and a matching bag for an enchanting evening look perfect for summer parties or date nights.'
        },
        {
            'season': 'Summer',
            'username': 'misbah',
            'name': 'Sporty Graphic Vibes',
            'image': 'outfits_image/summer4.jpg',
            'description': 'A sporty yet chic ensemble featuring a bralette and high-waisted athletic shorts, ideal for outdoor activities. Add a baseball cap, aviator sunglasses, and comfortable sneakers for a day filled with adventure and fun under the sun.'
        },
        {
            'season': 'Spring',
            'username': 'misbah',
            'name': 'Cozy Spring Midi',
            'image': 'outfits_image/spring1.jpg',
            'description': 'A cozy oversized sweater worn with a flowy dress, adorned with a subtle floral pattern. Complete the outfit with hightop converse for a laid-back yet sophisticated spring ensemble.'
        },
        {
            'season': 'Spring',
            'username': 'misbah',
            'name': 'Denim Layers',
            'image': 'outfits_image/spring2.jpg',
            'description': 'A classic denim jeans paired with a white corset-top, paired with white sandals for a casual and timeless spring outfit. Add a gold bracelet and earrings for a pop of color.'
        },
        {
            'season': 'Spring',
            'username': 'misbah',
            'name': 'Effortless Sprot',
            'image': 'outfits_image/spring3.jpg',
            'description': 'A sporty and effortless sweatshirt in a soft, earthy tone, combined with sneakers and a small purse for a relaxed and stylish spring look, perfect for picnics or jogs in the park.'
        },
        {
            'season': 'Spring',
            'username': 'misbah',
            'name': 'Vibrant Maxi Bohemia',
            'image': 'outfits_image/spring4.jpg',
            'description': 'A flowy, bohemian-inspired maxi dress with a mix of vibrant colors and floral prints, accessorized with pearl earrings and strappy sandals. This outfit exudes the essence of spring and is ideal for attending outdoor festivals and gatherings.'
        },
        {
            'season': 'Winter',
            'username': 'misbah',
            'name': 'Cozy Turtleneck Chic',
            'image': 'outfits_image/winter1.jpg',
            'description': 'A cozy turtleneck sweater paired with uggs and denim jeans for a chic winter ensemble.  Accessorize with a cashmere scarf and gold jewellery for added warmth and sophistication.'
        },
        {
            'season': 'Winter',
            'username': 'misbah',
            'name': 'Timeless Wool Pea',
            'image': 'outfits_image/winter2.jpg',
            'description': 'A classic ensemble featuring a wool pea sweater worn over a crisp white button-up shirt and tailored trousers. Add ankle shoes, and a structured tote bag to elevate this professional and polished winter outfit.'
        },
        {
            'season': 'Winter',
            'username': 'misbah',
            'name': 'Practical Woolen Style',
            'image': 'outfits_image/winter3.jpg',
            'description': 'A stylish and practical woolen sweater worn with tailored pants and lace-up winter boots. Accessorize with a plaid blanket scarf for a cozy and trendy look, perfect for winter adventures.'
        },
        {
            'season': 'Winter',
            'username': 'misbah',
            'name': 'Sweater Weather',
            'image': 'outfits_image/winter4.jpg',
            'description': 'Stay cozy and chic with a outfit featuring black pants, a tank top, and a white woolen jacket sweater paired with iconic Doc Martens boots for an edgy touch. Add dainty jewelry for a touch of glamour while staying warm and stylish.'
        },
        {
            'season': 'Autumn',
            'username': 'misbah',
            'name': 'Trench & Turtleneck',
            'image': 'outfits_image/autumn1.jpg',
            'description': 'A classic trench coat worn with a lightweight turtleneck sweater and denimjeans for a sophisticated and polished fall ensemble. Add boots and a leather crossbody bag to complete this timeless outfit.'
        },
        {
            'season': 'Autumn',
            'username': 'misbah',
            'name': 'Fall Blush Vibe',
            'image': 'outfits_image/autumn2.jpg',
            'description': 'Embrace soft and feminine vibes with a baby pink sweater, pairing it elegantly with crisp white pants and shoes for a fresh and stylish look. Complete the ensemble by adding a spacious tote bag.'
        },
        {
            'season': 'Autumn',
            'username': 'misbah',
            'name': 'Edgy Moto Glam',
            'image': 'outfits_image/autumn3.jpg',
            'description': 'A trendy and edgy outfit featuring a leather moto jacket worn over a graphic tee and ripped skinny jeans. Complete the look with combat boots and a studded clutch for a bold and stylish fall statement.'
        },
        {
            'season': 'Autumn',
            'username': 'misbah',
            'name': 'Sporty Blue Harmony',
            'image': 'outfits_image/autumn4.jpg',
            'description': 'Channel a sporty and stylish vibe with a dark blue coordinated track suit, featuring a zip-up jacket and track pants, paired effortlessly with a white tank top and chunky white shoes for a trendy and comfortable athleisure outfit.'
        },
        {
            'season': 'Rainy',
            'username': 'misbah',
            'name': 'Rain-Resistant Trench',
            'image': 'outfits_image/rainy1.jpg',
            'description': 'A water-resistant trench coat worn over a lightweight top and skinny denim shorts, paired with waterproof ankle boots for a practical and stylish rainy-day outfit. Complete the look with a compact umbrella and a crossbody bag to keep your essentials dry.'
        },
        {
            'season': 'Rainy',
            'username': 'misbah',
            'name': 'Casual Rainy Comfort',
            'image': 'outfits_image/rainy2.jpg',
            'description': 'A casual and comfortable ensemble featuring a jacket worn with slim dress and rain boots. Accessorize with a patterned purse and a umbrella for a practical yet stylish rainy-day outfit.'
        },
        {
            'season': 'Rainy',
            'username': 'misbah',
            'name': 'Urban Rain-Ready Chic',
            'image': 'outfits_image/rainy3.jpg',
            'description': 'A chic and urban-inspired outfit featuring a grey graphic tshirt paired over a cotton trousers along with rubber-soled sandals and a umbrella for a trendy and rain-ready look.'
        },
        {
            'season': 'Rainy',
            'username': 'misbah',
            'name': 'Cozy Rain Day Style',
            'image': 'outfits_image/rainy4.jpg',
            'description': 'A cozy and laid-back outfit with a simple tshirt and joggers, paired with sneakers. Add a silver watch  and baseball cap to add a pop of style on a rainy day. Do not forget your umbrella'
        }
    ]

    cats = {
            'Fashion': {'tips': fashion_tips},
            'Travel': {'tips': travel_tips} 
    }
  
    seasons_data = [
            {'name': 'Spring', 'maxtemp': 21, 'mintemp': 25},
            {'name': 'Summer', 'maxtemp': 55, 'mintemp': 26},
            {'name': 'Autumn', 'maxtemp': 20, 'mintemp': 11},
            {'name': 'Winter', 'maxtemp': 10.0, 'mintemp': -10},
            {'name': 'Rainy', 'maxtemp': None, 'mintemp':None},
    ]

    for season_data in seasons_data:
        add_season(season_data['name'], season_data['maxtemp'], season_data['mintemp'])


    for outfit_data in outfits_data:
        add_outfit(outfit_data['season'], outfit_data['username'], outfit_data['name'], outfit_data['image'], outfit_data['description'])


    for cat, cat_data in cats.items():
        c= add_cat(cat)
        for t in cat_data['tips']:
            add_tip(c,t['title'],t['img'],t['content'],t['likes'])

    for c in Category.objects.all():
        for t in Tip.objects.filter(category=c):
            print(f'- {c}: {t}')

def add_tip(cat, title, img, content,likes):
    t = Tip.objects.get_or_create(category=cat, title=title)[0]
    t.img=img
    t.content=content
    t.likes=likes
    t.save()
    return t

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_season(name, maxtemp, mintemp):
    season = Season.objects.get_or_create(name=name, maxtemp=maxtemp, mintemp=mintemp)[0]
    season.save()
    return season

def add_outfit(season_name, username, name, image, description):
    season = Season.objects.get(name=season_name)
    user = UserProfile.objects.get(user__username=username)
    outfit = Outfit.objects.get_or_create(season=season, username=user, name=name, image=image, description=description)[0]
    outfit.save()
    return outfit

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()