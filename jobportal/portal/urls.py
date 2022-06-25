from django.urls import path
from . import views
urlpatterns = [
    path('',views.login1),
    path('reg',views.reg),
    path('log',views.log),
    path('remployee',views.remployee),
    path('employeehomepage',views.employeehomepage),
    path('companylogin', views.companyregister),
    path('companyreg', views.companyreg),
    path('companyhomepage', views.companyhomepage),
    path('index2', views.index2),
    path('addvacancy', views.addvacancy1),
    path('addvacancy2', views.addvacancy2),
    path('adminhome', views.adminhome),
    path('viewemp', views.viewemp),
    path('ar', views.ar),
    path('reject/<int:id>', views.reject, name='reject'),
    path('accept/<int:id>', views.accept, name='accept'),
    path('feed',views.feed),
    path('sendfeed',views.sendfeed3),
    path('sendfeed2',views.sendfeed2),
    path('emphomepage',views.emphomepage),
    path('uploadcv/<int:id>',views.uploadcv,name='uploadcv'),
    path('viewjobs',views.viewjobs),
    path('jreq',views.jreq),
    path('viewjobreq',views.viewjobreq),


]