from django.urls import path
from . import views
app_name='demoapp' 
'''The app_name defines the application namespace so that the views in this app are identified by it.

To obtain the URL path of the index() function, call the reverse() function by prepending the namespace to it.
>>> from django.urls import reverse 
>>> reverse('index') 
'/demo/' 
>>> reverse('demoapp:index') 
'/demo/' '''

urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='homeji'),
    path('practice1',views.pra1,name='pra1'),
    path('getuser/<name>/<id>/<int:marks>',views.pathview),  #int represents path converter type and marks is the url parameter
    path('getdata/',views.queryview,name='qryview'),
    path('showform/',views.showform,name="showform"),
    path('getform/',views.getform,name="getform"),
    path('error/',views.error),
    path('<str:drink_name>', views.drinks, name="drink_name"),
   
]

# error = "demoapp."