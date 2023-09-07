from django.urls import path
from . import views

app_name = 'pitch'
urlpatterns = [
    # Other URL patterns...
    path('submit_pitch/', views.submit_pitch, name='submit_pitch'),
    path('view_pitches/', views.view_pitches, name='view_pitches'),
    path('my-pitches/', views.my_pitches, name='my_pitches'),
    path('delete/<int:pitch_id>/', views.delete_pitch, name='delete_pitch'),
]
