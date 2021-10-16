# Order class stores details of a particular order and its attributes
# It also has a dispatch method to trigger delivery of the order via a specific route
class Order:
    def __init__(self, id, item_name, customer, order_date, city, delivery_date, delivery_type):
        self._id = id
        self._item_name = item_name
        self._customer = customer
        self._order_date = order_date
        self._city = city
        self._delivery_date = delivery_date
        self._delivery_type = delivery_type

    #__str__ is a special function that allows customising the information that's displayed when one prints the object
    def __str__(self):
        return f'ID - {self.id}, Item Name - {self.item_name}, Order Date - {self.order_date}, Customer - {self.customer}, City - {self.city}, Delivery Date - {self.delivery_date}, Delivery Type - {self.delivery_type}'
    
    # @property is a way of creating a getter function for internal attributes.
    # The actual attribute is named with an underscore at the beginning highlighting no direct access, by convention
    # The function should have the same name, without the underscore
    # It can be used like an attribute and python will automatically call this function to retrieve the correct value
    @property
    def id(self):
        return self._id

    @property
    def item_name(self):
        return self._item_name

    @property
    def order_date(self):
        return self._order_date

    @property
    def customer(self):
        return self._customer

    @property
    def city(self):
        return self._city

    @property
    def delivery_date(self):
        return self._delivery_date

    @property
    def delivery_type(self):
        return self._delivery_type
    

    #This will trigger a dispatch of the order using a specific delivery route. This is an example of double dispatch
    def dispatch(self, delivery_route):
        # print(f'Dispatching order {order}')
        print(f'Dispatching order {self}')
        delivery_route.process_order(self)