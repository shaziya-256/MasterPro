from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from app1.models import Product,Vendor



class VendorSer(ModelSerializer):
    # products = ProdSer(many=True)

    class Meta:
        model = Vendor
        # fields = '__all__'
        exclude = ('id',)


class ProdSer(ModelSerializer):
    vendorref = VendorSer()

    class Meta:
        model = Product
        fields = '__all__'




