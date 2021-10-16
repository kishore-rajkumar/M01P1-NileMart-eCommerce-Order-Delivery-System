#Delivery routes for each city - normal delivery
NORMAL_DELIVERY_MAP_CONFIG = '../../v1/config/normal_delivery_map.txt'
#Delivery routes for each city - premium delivery
PREMIUM_DELIVERY_MAP_CONFIG = '../../v1/config/premium_delivery_map.txt'
#Order list
ORDER_BATCH_CONFIG = '../../v1/config/order_batch.txt'

from DeliverySystem import DeliverySystem
from OrderBatch import OrderBatch

# #Delivery routes for each city - delivery
DELIVERY_MAP_CONFIG = '../config/delivery_map.txt'

# ORDER_BATCH_CONFIG = '../config/order_batch.txt'

# main function
if __name__=="__main__":

    print('V2......\n')

    # DeliverySystem object creation for routes of all destinations
    delivery_system = DeliverySystem()
    delivery_system.configure(DELIVERY_MAP_CONFIG)

    # Order objects and OrderBatch created based on order list in the config
    order_batch = OrderBatch()
    order_batch.read_config(ORDER_BATCH_CONFIG)

    orders = order_batch.get_orders()

    # For each order, based on the delivery type, either normal or premium delivery system is used
    # The route to the order destination is then retrieved from the selected delivery system
    # The order is dispatched by passing the selected route as a parameter. This in turn would trigger order processing in the route object
    for order in orders:
        route=delivery_system.get_route_v2(order.city,order.delivery_type)
        print('\n')
    