from rest_framework import viewsets

from .models import Product
from .serialziers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        if status := self.request.query_params.get("status"):
            queryset = queryset.filter(status=status)

        if article := self.request.query_params.get("article"):
            queryset = queryset.filter(article=article)

        if name := self.request.query_params.get("name"):
            queryset = queryset.filter(name=name)

        return queryset
