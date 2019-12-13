from django.urls import path

from api.views import PageList, PageDetails

urlpatterns = [
    path('page/', PageList.as_view(), name='page_list'),
    path('page/<int:pk>', PageDetails.as_view(), name='page_detail')
]
