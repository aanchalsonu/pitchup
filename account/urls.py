from . import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('', views.LoginView, name='login'),
    path('signup/', views.SignView, name='signup'),
    path('logout/', views.SignOutView, name='signout'),
    path('profile/edit', views.EditProfile, name='edit-profile'),
]


# user :admin 
# password :django

#user: mee
#password : pitchup@123

#user: FlavorFusionDelights
#password : pitchup@123
