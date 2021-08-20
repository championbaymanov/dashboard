from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('billing', views.billing, name="billing"),
    path('profile', views.profile, name="profile"),
    path('rtl', views.rtl, name="rtl"),
    path('sign_in', views.login_user, name="sign_in"),
    path('sign_up', views.register_user, name="sign_up"),
    path('tables', views.tables, name="tables"),
    path('virtual_reality', views.virtual_reality, name="virtual_reality"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('<int:pk>', views.MentorUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('tables/<int:pk>', views.group_filter, name='filter'),
    path('tables/<str:pk>', views.payment_status_filter, name='filterr'),
    path('create_student', views.create_student, name="create_student"),
    path('update_student/<int:pk>', views.update_student, name="update_student"),
    path('delete_student/<int:pk>', views.delete_student, name="delete_student"),
    path('create_mentor', views.create_mentor, name="create_mentor"),
    path('update_mentor/<int:pk>', views.update_mentor, name="update_mentor"),
    path('delete_mentor/<int:pk>', views.delete_mentor, name="delete_mentor"),
    path('create_group', views.create_group, name="create_group"),
    path('update_group/<int:pk>', views.update_group, name="update_group"),
    path('delete_group/<int:pk>', views.delete_group, name="delete_group"),

]
