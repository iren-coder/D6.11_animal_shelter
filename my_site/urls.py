
from django.contrib import admin
from django.urls import path

from my_site import settings
from animal_shelter import views
from django.conf.urls.static import static
from animal_shelter.views import HomePageView, CatsList, DogsList, ParrotsList, ContactsPageView, CatDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view()),
    path('employee/', views.employee),
    path('cats/', CatsList.as_view(), name="cats"),
    path('dogs/', DogsList.as_view(), name="dogs"),
    path('parrots/', ParrotsList.as_view(), name="parrots"),
    path('contacts/', ContactsPageView.as_view(), name="contacts"),
    path('pet_info/<int:pk>/', CatDetailView.as_view(), name="pet_info"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
