from django.urls import path

from product.views import ProductListView, ProductDetailView

app_name = 'product'




urlpatterns = [
    path('list/<slug:slug>/',ProductListView.as_view(),name='product_list'),
    path('detail/<slug:slug>/',ProductDetailView.as_view(),name='product_detail'),

]
