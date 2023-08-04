from django.urls import path
from todo import views


urlpatterns = [
    path("add/", views.add_task, name="add-task"),
    path("mark-as-done/<int:id>/", views.mark_as_done, name="mark-as-done"),
    path("delete-task/<int:id>/", views.delete_task, name="delete-task"),
    path("edit-task/<int:id>/", views.edit_task, name="edit-task"),
    path("undo-task/<int:id>/", views.undo_task, name="undo-task"),
]
