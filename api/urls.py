from django.urls import path
from .views import RegisterView, PublicView, ProtectedView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('public/', PublicView.as_view(), name='public'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
