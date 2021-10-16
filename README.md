# M01P1-NileMart-eCommerce-Order-Delivery-System

### Introduction
The NileMart Portal hosts a website for customers to search and select products, and place orders.
They have a delivery system to ship orders from their warehouse to the customer’s doorstep.
The project mimics an ​ order​ delivery from warehouse to the ​ destination​ city. Every destination has a
fixed​ delivery route​ , for each ​ delivery type​ (​ normal​ or ​ premium​ ), from the central warehouse.

There are several types of dispatch between centers:

● Truck
● Train
● Flight
● Boat (New)
● Ship (New)


### Program Organization
**Please look at the ​ v1 ​ folder first**<br/>
● The source file ​ nile-mart.py​ in the ​ src/​ directory, and multiple config files in the ​ config/directory<br/>
● config/order_batch.txt​ contains one order per line in this format:<br/>
``` <Order ID>-<Order Item>-<Customer-Name>-<Order Date>-<City>-<DeliveryDate>-<Delivery Type>```<br/>
● config/normal_delivery_map.txt​ and config/premium_delivery_map.txt​ hold routing information for each destination, per delivery type (​ normal​ / ​ premium​ ):<br/>
```<Destination> <Center>-<Dispatch Type>-<Center>,<Center>-<DispatchType>-<Center>,...,<Center>-<DispatchType>-<Destination>```<br/>
● Classes<br/>
>○ OrderBatch ​ parses order information from ​ order_batch.txt​ and creates order objects<br/>
○ Order ​ stores details of an individual order, and triggers delivery via a route<br/>
○ DeliveryMap ​ parses routing information and stores it in a raw format<br/>
○ DeliverySystem ​ uses DeliveryMap to create usable routes to all destinations<br/>
○ DeliveryRoute ​ class holds the structured route to a destination, with several stages<br/>
○ DeliveryStage​ , and the inherited classes -- ​ TrainDispatch​ , ​ FlightDispatch​ , TruckDispatch ​ define specific stages of a route, depending on the dispatch type<br/>

● We have two delivery systems - ​ normal​ and ​ premium​ . We assign each order a route, based on delivery type, and destination city. The dispatch internally calls the route to process the order in a double dispatch manner.<br/>

**Two enhancements implemented for version ​ v2​**<br/>
1. Only one ​ delivery_map.txt​ file is used in ​ v2​ . The format has changed to include both normal and premium types in the same file:<br/>
```<Destination> <Delivery Type> <Center>-<DispatchType>-<Center>,<Center>-<Dispatch Type>-<Center>,...,<Center>-<DispatchType>-<Destination>```<br/><br/>
**NOTE**: ​ The two fields (​ ```<Destination> and <Delivery Type>```). ​ <br/>Implemented this field as a Python ​ tuple - (destination,delivery_type)​ - in your delivery map data structure. Alternatively, this can be implemented as a nested dictionary with delivery types within each destination.<br/>
>In​ v1​ , creating the delivery system is spread across:<br/>
● The ​ DeliverySystem builder<br/>
● The client: creates different systems from separate config files, and chooses among them based on the delivery type.<br/>

>● All this are combined in one ​ DeliverySystem​ , to put the logic together, and provided a common endpoint to the client.<br/>
● We have modified the config file and accordingly modified the code so that the DeliverySystem​ and other classes can use this config file, to create all types of routes to all destinations, in one go.<br/>
● This also make it easy to create and select a route, based on delivery type and destination city.<br/>

2. NileMart is expanding to nearby islands (​ Tiliana​ , ​ Marbut​ ). We need new methods of delivery, namely boat and ship. You would notice we added these two destinations, and two new delivery types in the config files. We have added code to include these new delivery methods.<br/>

**Key Highlights**
>○ DeliverySystem behaves as a ​ **Builder​** , converting route directions to a usable routing system<br/>
○ A ​ **Strategy​ pattern** decides between using the normal or the premium route (to the same destination). It selects the routing scheme based on the delivery type mentioned in the order. The methods remain unchanged, but the order flows through a different route.<br/>
○ The stages in the route behave as a chain, calling the next in sequence, until all the stages are completed - implementing the ​ **Chain of Responsibility​ pattern**<br/>
○ The route is passed to the order, which invokes order handling on the route. This double dispatch makes it more flexible to add say, digital deliveries and store pickups.<br/>