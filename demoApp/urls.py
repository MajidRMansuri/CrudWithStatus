from .views import *
from django.urls import path
urlpatterns = [
    path('',index,name='index'),
    path('form_data/',form_data,name='form_data'),
    path('login_page/',login_page,name='login_page'),
    path('login/',login,name='login'),
    path('profile/',profile,name='profile'),
    path('update_form_data/',update_form_data,name='update_form_data'),
    path('profile_data/',profile_data,name='profile_data'),
    path('user_data/',user_data,name='user_data'),
    path('edit_item/<int:pk>/',edit_item,name='edit_item'),
    path('remove_item/<int:pk>/',remove_item,name='remove_item'),
    path('mulDelete',mulDelete,name='mulDelete'),
    path('savevalues',savevalues,name='savevalues'),
    path('status',status,name='status'),

    # path('form_data', form_data, name=form_data),
]