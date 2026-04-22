from django.urls import path
from Projectsampleapp import views

urlpatterns = [
    path('welcome/',views.welcome,name="welcome"),
    path('one',views.one,name='one'),
    path('two',views.two,name='two'),
    path('three',views.three,name='three'),
    path('four',views.four,name='four'),
    path('five',views.five,name='five'),
    path('six',views.sixth,name='six'),
    path('nine',views.nine,name='nine'),
    path('emp',views.employeedata,name="emp"),
    path('empview',views.empview,name="Empview"),
    path('empdel/<int:did>',views.empdel,name="EmpDEL"),
    path('empedit/<int:uid>',views.empedit,name="EmpEdit"),
    path('empedit2/<int:uid>',views.empedit2,name="EmpEdit2"),
    path('profiledata',views.profiledata,name='profiledata'),
    path('studreg',views.studreg,name="StudReg"),
    path('studview',views.studview,name="StudView"),
    path('studdelete/<int:did>',views.studdelete,name="studdelete"),
    path('studedit/<int:did>',views.studedit,name="studedit"),
    path('studedit1/<int:did>',views.studedit1,name="studedit1"),
    path('addmark',views.addmark,name="AddMark"),
    path('viewmark',views.viewmark,name="ViewMark"),
    path('editmark/<int:did>',views.editmark,name="EditMark"),
    path('editmark1/<int:did>',views.editmark1,name="EditMark1"),
    path('deletemark/<int:did>',views.deletemark,name="DeleteMark"),
    path('deleteall/<int:dsid>',views.deleteall,name="DeleteAll"),
    path('sc',views.setcookie,name="Setcookie"),
    path('gc',views.getcookie,name="Getcookie"),
    path('ss',views.setsession,name="Setsession"),
    path('gs',views.getsession,name="Getsession"),
    path('ds',views.deletesession,name="Deletesession"),
    

]
