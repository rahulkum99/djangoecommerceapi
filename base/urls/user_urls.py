from django.urls import path
from base.views import user_views as views
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/',views.getUserProfile,name="getuser"),
    path('',views.getUser,name='user'),
    path('register/',views.registerUser,name='register'),
]