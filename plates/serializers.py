from rest_framework import serializers

from .models import Plate, Owner


class PlateSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(read_only=True, source="owner.name")
    owner_surname = serializers.CharField(read_only=True, source="owner.surname")

    class Meta:
        model = Plate
        fields = ('url', 'id', 'license_number', 'owner_name', 'owner_surname', 'owner')


class OwnerSerializer(serializers.ModelSerializer):
    plates = PlateSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('url', 'id', 'name', 'surname', 'plates')
