from django.urls import path, include

from . import views



urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),

    path("promotion/", views.Promotion.as_view(), name='promotion'),
    path("buyer/", views.Buyer.as_view(), name='buyer'),
    path("contact/", views.Contact.as_view(), name='contact'),
    path("about/", views.About.as_view(), name='about'),

    path('<slug:slug>/', views.ListIndex.get_index, name="list-index"),

    path('<str:nav>/<slug:slug>/', views.ListIndex.get_detail, name="list-detail"),
]