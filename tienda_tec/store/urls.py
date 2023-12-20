from django.urls import path, include
from store import views
from store.views import ProductListView
from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()
router.register('products/', ProductViewSet, 'products')

store_urlpatterns = ([
    path('', ProductListView.as_view(), name='product_list'),
    path('detail_order/', views.detail_order, name='detail_order'),
    path('api/', include(router.urls))
], 'store')
