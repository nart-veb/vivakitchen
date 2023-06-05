from django.urls import path, include

from . import views


kitchen_patterns = [
    path("", views.Kitchen.get_index, name='kitchen'),
    path('<slug:slug>', views.Kitchen.get_detail, name="kitchen-detail")
]

wardrobes_patterns = [
    path("", views.Wardrobes.get_index, name='wardrobes'),
    path('<slug:slug>', views.Wardrobes.get_detail, name="wardrobes-detail")
]

bathroom_patterns = [
    path("", views.Bathroom.get_index, name='bathroom'),
    path('<slug:slug>', views.Bathroom.get_detail, name="bathroom-detail")
]

sofas_patterns = [
    path("", views.Sofas.get_index, name='sofas'),
    path('<slug:slug>', views.Sofas.get_detail, name="sofas-detail")
]

garden_patterns = [
    path("", views.Garden.get_index, name='garden'),
    path('<slug:slug>', views.Garden.get_detail, name="garden-detail")
]

light_chandelier_patterns = [
    path("", views.Light.get_chandelier, name='chandelier'),
    path('<slug:slug>/', views.Light.get_detail, name="chandelier-detail")
]
light_lamp_patterns = [
    path("", views.Light.get_lamp, name='lamp'),
    path('<slug:slug>/', views.Light.get_detail, name="lamp-detail")
]
light_system_patterns = [
    path("", views.Light.get_system, name='system'),
    path('<slug:slug>/', views.Light.get_detail, name="system-detail")
]
light_ceiling_patterns = [
    path("", views.Light.get_ceiling, name='ceiling'),
    path('<slug:slug>/', views.Light.get_detail, name="ceiling-detail")
]

portfolio_patterns = [
    path("", views.Portfolio.get_index, name='portfolio'),
    path('<slug:slug>/', views.Portfolio.get_detail, name="portfolio-detail")
]

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("kitchen/", include(kitchen_patterns)),
    path("wardrobes/", include(wardrobes_patterns)),
    path("bathroom/", include(bathroom_patterns)),
    path("sofas/", include(sofas_patterns)),
    path("garden/", include(garden_patterns)),
    path("light/chandelier/", include(light_chandelier_patterns)),
    path("light/lamp/", include(light_lamp_patterns)),
    path("light/system/", include(light_system_patterns)),
    path("light/ceiling/", include(light_ceiling_patterns)),
    path("portfolio/", include(portfolio_patterns)),

    path("promotion/", views.Promotion.as_view(), name='promotion'),
    path("buyer/", views.Buyer.as_view(), name='buyer'),
    path("contact/", views.Contact.as_view(), name='contact'),
    path("about/", views.About.as_view(), name='about'),
]