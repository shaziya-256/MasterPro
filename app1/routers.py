from rest_framework.routers import SimpleRouter
from app1.views import ProductOperations,VendorOperations
srouter = SimpleRouter()
srouter.register('product',ProductOperations)
srouter.register('vendor',VendorOperations)
urlpatterns = srouter.urls
