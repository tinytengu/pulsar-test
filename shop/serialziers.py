from rest_framework import serializers

from .models import Product


class ImageField(serializers.ImageField):
    def to_representation(self, value):
        return {
            "path": ".".join(str(value.url).split(".")[:-1]),
            "formats": ["webp"],
        }


class ProductSerializer(serializers.ModelSerializer):
    image = ImageField()

    class Meta:
        model = Product
        fields = "__all__"
