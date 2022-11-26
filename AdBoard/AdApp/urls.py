from django.urls import path

from . import views
from .views import AdvertList, AdvertDetail, AdvertCreate, AdvertEdit, ReplyDeleteView

urlpatterns = [
    path('', AdvertList.as_view(), name='ads'),
    path('<int:pk>', AdvertDetail.as_view(), name='ad_detail'),
    path('create/', AdvertCreate.as_view(), name='ad_create'),
    path('<int:pk>/edit/', AdvertEdit.as_view(), name='ad_edit'),
    path('reply/<int:pk>', views.SendReply.as_view(), name='send_reply'),
    path('<int:pk>/delete', ReplyDeleteView.as_view(), name='delete_reply'),
    # path('<int:pk>/apply', views.apply_reply, name='apply_reply'),
]