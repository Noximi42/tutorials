from django.urls import path
from . import views

urlpatterns = [
    # path('blog_post_list/', views.blog_post_list_as_text, name='blog_post_list'),
    # path('blog_post_details/<int:blog_post_id>/', views.blog_post_details_as_text, name='blog_post_details')

    path('blog_post_list/', views.blog_post_list_via_template, name='blog_post_list'),
    # path('blog_post_details/<int:blog_post_id>/', views.blog_post_details_via_template, name='blog_post_details'),
    path('blog_post_details/<int:blog_post_id>/', views.blog_post_details_with_form, name='blog_post_details'),
]
