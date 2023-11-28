"""untitled7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from onroadservice import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.loginn),
    path('loginn_post', views.loginn_post),
    path('homepage',views.homepage),
    path('addservice',views.addservice),
    path('viewservice', views.viewservice),
    path('addservice_post', views.addservice_post),
    path('viewworker', views.viewworker),
    path('viewuser',views.viewuser),
    path('changepw', views.changepw),
    path('changepw_post', views.changepw_post),
    path('register_worker', views.register_worker),
    path('register_worker_post', views.register_worker_post),
    path('worker_view_service',views.worker_view_service),
    path('view_ownservice',views.view_ownservice),
    path('addtoown/<id>',views.addtoown),
    path('workerhomepage',views.workerhomepage),
    path('accept_worker/<id>', views.accept_worker),
    path('verifiedworker',views.verifiedworker),
    path('ratingsreview',views.ratingsreview),
    path('registration_user',views.registration_user),
    path('registration_user_post',views.registration_user_post),
    path('userhomepage',views.userhomepage),
    path('viewservices',views.viewservices),
    path('delete_ownsevice/<sid>',views.delete_ownsevice),
    path('user_view_workers/<sid>',views.user_view_workers),
    path('long_lat/<id>',views.long_lat),
    path('long_lat_post/<id>',views.long_lat_post),
    path('view_user_request',views.view_user_request),
    path('accept_request/<id>',views.accept_request),
    path('reject_request/<id>', views.reject_request),
    path('user_view_request_status',views.user_view_request_status),
    path('rate_review/<id>',views.rate_review),
    path('rate_review_post',views.rate_review_post),
    path('user_view_ratings/<id>',views.user_view_ratings),
    path('delete_service/<id>',views.delete_service),
    path('logout',views.logout),
]
