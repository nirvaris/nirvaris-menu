from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),    

]