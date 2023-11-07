from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('deleteoneproduct/<int:id>', views.deleteOneProduct, name='delete_one_product'),
    path('deleteallproducts/', views.deleteAllProducts, name='delete_all_products'),
    path('updateoneproduct/<int:id>', views.updateOneProduct, name='update_one_product'),
    path('updateallproducts/', views.updateAllProducts, name='update_all_products'),
    path('addproduct/', views.addProduct, name='add_product'),
    path('addcategory/', views.addCategory, name='add_category'),
    path('deleteonecategory/', views.deleteOneCategory, name='delete_one_category'),
    path('deleteallcategories/', views.deleteAllCategories, name='delete_all_categories'),
    path('search-products/', views.search_products, name='search_products')
    ]

