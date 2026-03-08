from django.urls import path
from tracker.views import index, deleteTransaction, registeration, login_page, logout_page


urlpatterns = [
    path('', index, name = "index"),
    path('delete-transaction/<uuid>/', deleteTransaction, name = "deleteTransaction"),
    path('registeration/', registeration),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page")
]