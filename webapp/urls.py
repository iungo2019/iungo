from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views



app_name = 'webapp'

urlpatterns = [
    path('register/user/',views.customerRegister,name='register'),
    path('login/user/',views.customerLogin,name='login'),
    path('profile/user/',views.customerProfile,name='profile'),
    path('user/create/',views.createCustomer,name='create'),
    path('user/update/<int:id>/',views.updateCustomer,name='update'),
    path('user/cloudupload/',views.CustomerCloud,name='cloud'),
    path('user/records/',views.record_list,name='records'),
    path('register/designer/',views.designerRegister,name='dregister'),
    path('login/designer/',views.designerLogin,name='dlogin'),
    path('profile/designer/',views.designerProfile,name='dprofile'),
    path('designer/create/',views.createDesigner,name='dcreate'),
    path('designer/update/<int:id>/',views.updateDesigner,name='dupdate'),
    path('designer/enquiry/',views.EnquiryDesigner,name='denquiry'),
    path('register/architect/',views.architectRegister,name='aregister'),
    path('login/architect/',views.architectLogin,name='alogin'),
    path('profile/architect/',views.architectProfile,name='aprofile'),
    path('architect/create/',views.createArchitect,name='acreate'),
    path('architect/update/<int:id>/',views.updateArchitect,name='aupdate'),
    path('architect/enquiry/',views.EnquiryArchitect,name='aenquiry'),
    path('register/builder/',views.builderRegister,name='bregister'),
    path('login/builder/',views.builderLogin,name='blogin'),
    path('profile/builder/',views.builderProfile,name='bprofile'),
    path('builder/create/',views.createBuilder,name='bcreate'),
    path('builder/update/<int:id>/',views.updateBuilder,name='bupdate'),
    path('builder/enquiry/',views.EnquiryBuilder,name='benquiry'),
    path('builder/addprop/',views.AddBuilderProperties,name='baddprop'),
    path('builder/props/',views.BuilderProperty,name='bprops'),
    path('register/agent/',views.agentRegister,name='agregister'),
    path('login/agent/',views.agentLogin,name='aglogin'),
    path('profile/agent/',views.agentProfile,name='agprofile'),
    path('agent/create/',views.createAgent,name='agcreate'),
    path('agent/update/<int:id>/',views.updateAgent,name='agupdate'),
    path('agent/enquiry/',views.EnquiryAgent,name='agenquiry'),
    path('agent/addprop/',views.AddAgentProperties,name='agaddprop'),
    path('agent/prop/',views.AgentProperties,name='agprop'),
    path('register/support/',views.supportRegister,name='sregister'),
    path('login/support/',views.supportLogin,name='slogin'),
    path('profile/support/',views.supportProfile,name='sprofile'),
    path('support/create/',views.createSupport,name='screate'),
    path('support/update/<int:id>/',views.updateSupport,name='supdate'),
    path('support/enquiry/',views.EnquirySupport,name='senquiry'),
    path('logout/',views.Logout,name='logout'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

]
