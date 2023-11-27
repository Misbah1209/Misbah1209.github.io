from django.urls import path
from rango import views

app_name = 'rango'

#Listed the url path for each view here.

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('tips/', views.tips, name='tips'),
    path('outfit/', views.outfit, name='outfit'),
    path('like_tip/', views.LikeTipsView.as_view(), name='like_tip'),
    path('admin/', views.admin, name='admin'),
    path('add_tip/', views.add_tip, name='add_tip'),
    path('edit_tip/<int:pk>/', views.edit_tip, name='edit_tip'),
    path('delete_tip/<int:pk>/', views.delete_tip, name='delete_tip'),
    path('lists/', views.lists, name='lists'),
    path('delete_list/<int:list_id>/', views.delete_list, name='delete_list'),
    path('items/<int:list_id>/', views.items, name='items'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('profile/', views.profile, name='profile'),
    path('add_outfit/', views.add_outfit, name='add_outfit'),
    path('delete_outfit/<int:pk>/', views.delete_outfit, name='delete_outfit'),
]