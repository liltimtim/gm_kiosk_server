from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Kiosk
from .serializers import KioskSerializer


class KioskList(generics.ListAPIView):
    queryset = Kiosk.objects.all()
    serializer_class = KioskSerializer


class KioskCreate(generics.CreateAPIView):
    queryset = Kiosk.objects.all()
    serializer_class = KioskSerializer
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        validated_data = KioskSerializer.validate(request.data)
        return validated_data.save()
