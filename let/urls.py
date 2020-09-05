from django.urls import path 
from veiws import veiws 

urlpatterns = [
    path("", veiws.index)
]