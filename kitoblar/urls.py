from django.urls import path
from .views import*
app_name='kitoblar'
urlpatterns=[
    path('kitoblar/<int:id>/',Categoriya,name='categoriya_page'),
    path('detail/<int:id>/',Detail,name='detail_page'),
    path('Add-comment/<int:id>/',AddComment.as_view(),name='add_comment')
]