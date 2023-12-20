from django.urls import path
from store import views
from store.views import ProductListView

store_urlpatterns = ([
    path('', ProductListView.as_view(), name='product_list'),
    path('detail_order/', views.detail_order, name='detail_order')
], 'store')
