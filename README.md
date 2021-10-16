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