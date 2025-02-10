from django.urls import path
from  .views import base,todo_vc,todo_d,todo_e,wiki

urlpatterns = [
    path('',base,name='base'),
    path('todo/',todo_vc,name='todo'),
    path('todo/<int:id>/delete/',todo_d,name='delete_todo'),
    path('todo/<int:id>/edit/',todo_e,name='edit_todo'),
    path('wikipedia/',wiki,name='wikipedia'),

]