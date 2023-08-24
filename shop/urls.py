from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='home'),
    path("category/",views.prod_category,name='category'),
    path("about/",views.about,name='aboutus'),
    path("contact/",views.contact_data,name='contactus'),
    path("tracker/",views.tracker,name='TrackingStatus'),
    path("search/",views.search,name='Search'),
    path("product_view/<int:myid>",views.product_view,name='productview'),
    path("checkout/",views.checkout,name='checkout'),
    path("login/",views.login,name='login'),##only for redirection purpose, no functionality will perform
    path("sign_up/",views.sign_up,name='logging'),
    path("logging/",views.logging,name='logging'),
    path("paypal_checkout/",views.paypal,name='logging'),
    path("invoice/",views.invoice,name='logging'),
]