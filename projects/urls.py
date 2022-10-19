from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')
urlpatterns = router.urls # se construyen 4 rutas (GET, POST, PATCh y DELETE)