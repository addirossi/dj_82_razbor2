from rest_framework import serializers

from main.models import Car, Sale


# class CarSerializer(serializers.Serializer):
#     model = serializers.CharField(max_length=100)
#     year = serializers.IntegerField()
#     color = serializers.CharField(max_length=20)
#     price = serializers.CharField(max_length=20)
#     equipment = serializers.CharField(max_length=20)
#     image = serializers.ImageField()


class EquipmentSerializer(serializers.Serializer):
    leather_interior = serializers.BooleanField()
    seat_heater = serializers.BooleanField()
    cruise_control = serializers.BooleanField()


class CarSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(write_only=True)


    # def validate(self):
    #     ...

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Неверная цена')
        return price

    def create(self, validated_data):
        equipment = validated_data.pop('equipment', {})
        if all(equipment.values()):
            validated_data['equipment'] = 'full'
        else:
            validated_data['equipment'] = 'partial'
        return super().create(validated_data)

    class Meta:
        model = Car
        fields = ['model', 'year', 'color', 'image', 'sales', 'equipment']
        depth = 1
        # fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'
