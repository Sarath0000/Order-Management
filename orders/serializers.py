# from rest_framework import serializers
# from .models import Order
# from products.models import Product

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['id','product', 'quantity'] # input fields in the postman body
#         read_only_fields = ['total_amount']

#         def create(self, validated_data):
#             print("order executed..................................................")
#             user = self.context['request'].user
#             product = validated_data['product']
#             quantity = validated_data['quantity']
#             if product.quantity < quantity: # product.quantity is the actual quantity of that product, quantity is the user ordering quantity
#                 raise serializers.ValidationError("Not Enough Stock")
            
#             total_amount = product.price*quantity
#             product.quantity -= quantity
#             product.save()
        
#             order = Order.objects.create(user=user,product=product,quantity=quantity,total_amount=total_amount)
#             return order