from django.urls import path
from .views import PublicView, ProtectedView
from .views import SendEmailView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('send-email/', SendEmailView.as_view(), name='send_email'),
]
