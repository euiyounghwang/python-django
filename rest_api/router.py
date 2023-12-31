
from rest_framework import routers
from .models import Student, userRank

from .views import (
    StudentViewSet, userRankViewSet, IpViewSet
)

# --
# Model && Serializer
# Create Model api automatically [GET, POST, PUT, DELETE]
router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
# router.register(r'userrank', userRankViewSet)
# router.register(r'ip', IpViewSet)
 # --