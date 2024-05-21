from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.user_dashboard, name='dashboard_user'),
    path('dashboard_logout', views.user_logout, name='dashboard_logout'),
    
    path('logout', views.user_logout, name="logout_user"),
    path('setting', views.site_setting, name="site_setting"),
    path('blank', views.user_blank, name="user_blank"),
    path('pages', views.user_pages, name="user_pages"),
    path('profile', views.user_profile, name="user_profile"),
    path('table', views.user_table, name="user_table"),
    
    path('submit_user_info/', views.submit_user_info, name='submit_user_info'),
    
     path('profile/update/', views.edit_profile, name='profile_update'),
    
    
]