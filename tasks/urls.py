from django.urls import path 

from .views import CustomLoginView, CustomLogoutView, SignUpView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, PhotoDeleteView, TaskDetailView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('task_list/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]