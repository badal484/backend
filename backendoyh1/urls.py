from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse   # <-- ADD THIS

def home(request):                     # <-- ADD THIS
    return JsonResponse({
        "status": "OK",
        "message": "OWN YOUR HEAVEN API is running 🚀"
    })

urlpatterns = [
    path('', home),  # <-- ADD THIS LINE

    path('admin/', admin.site.urls),

    # JWT login endpoints
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include other app URLs
    path('api/v1/', include('accounts.urls')),  # Signup, profile, etc.
    path('api/', include('api.urls')),          # Tasks endpoints
]
