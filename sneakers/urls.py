"""
URL configuration for sneakers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from SneakerApp.views import index, product_detail, brand_list, cart, checkout, update_item,process_order, loginPage,register, logoutUser, help
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('login/', loginPage, name="login"),
    path('register/', register, name="register"),
    path('logout/', logoutUser, name="logout"),
    path('index/', index, name="index"),
    path('item/<slug:slug>/', product_detail, name="product_detail"),
    path('search/<slug:brand_slug>/', brand_list , name="brand_list"),
    path('cart/', cart , name="cart"),
    path('checkout/', checkout , name="checkout"),
    path('update_item/',update_item, name ="update_item"),
    path('process_order/',process_order, name ="process_order"),
    path('help/', help, name="help"),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
