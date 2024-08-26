# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('register/', views.register_view, name='register'),


    # path for login
    path(route='login', view=views.login_user, name='login'),
 path('login/', TemplateView.as_view(template_name="index.html")),
  path('logout/', views.logout_view, name='logout'),
     path('register/', TemplateView.as_view(template_name="index.html")),
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
