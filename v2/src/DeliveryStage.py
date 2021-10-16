# DeliveryStage is an object storing information for a specific stage of a specific route
# It'll also store the next stage in the route
class DeliveryStage:
    def __init__(self, source, destination):
        self._source = source
        self._destination = destination
        self._next_stage = None

    @property
    def next_stage(self):
        return self._next_stage

    # This is a way to create a setter for a private attribute
    # The name in the annotation and the method name should match the attribute name (without the underscore)
    # It can be used like an attribute and python will automatically call this function to assign the value
    # for example, you can say ds_object.next_stage = dfg_stage, treating it like an attribute
    # This would automatically call this function and assign the value to the internal attribute appropriately
    @next_stage.setter
    def next_stage(self, successor):
        self._next_stage = successor

    def process_order(self, order):
        pass


# TrainDispatch, FlightDispatch, and TruckDispatch override DeliveryStage.
# They specify a particular type of transport, alongwith the base source and destination attributes

class TrainDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)

    def __str__(self):
        return f'Train from {self._source} to {self._destination}'
    
    
    def process_order(self, order):
        # This would have the actual logic of processing the train dispatch
        # The following string is a placeholder since this logic is not relevant to the project
        print(f'Order {order.id} - Train Dispatch from {self._source} to {self._destination}')

        # After processing the stage, this triggers the next stage in the route for processing
        # This is an example of the chain of responsibility pattern
        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 


class FlightDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)
    
    def __str__(self):
        return f'Flight from {self._source} to {self._destination}'
    
    
    def process_order(self, order):
        # This would have the actual logic of processing the flight dispatch
        # The following string is a placeholder since this logic is not relevant to the project
        print(f'Order {order.id} - Flight Dispatch from {self._source} to {self._destination}')

        # After processing the stage, this triggers the next stage in the route for processing
        # This is an example of the chain of responsibility pattern
        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 


class TruckDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)

    def __str__(self):
        return f'Truck from {self._source} to {self._destination}'
        
    def process_order(self, order):
        # This would have the actual logic of processing the truck dispatch
        # The following string is a placeholder since this logic is not relevant to the project
        print(f'Order {order.id} - Truck Dispatch from {self._source} to {self._destination}')

        # After processing the stage, this triggers the next stage in the route for processing
        # This is an example of the chain of responsibility pattern
        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 


class ShipDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)

    def __str__(self):
        return f'Ship from {self._source} to {self._destination}'
        
    def process_order(self, order):
        # This would have the actual logic of processing the truck dispatch
        # The following string is a placeholder since this logic is not relevant to the project
        print(f'Order {order.id} - Ship Dispatch from {self._source} to {self._destination}')

        # After processing the stage, this triggers the next stage in the route for processing
        # This is an example of the chain of responsibility pattern
        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 


class BoatDispatch(DeliveryStage):
    def __init__(self, source, destination):
        super().__init__(source, destination)

    def __str__(self):
        return f'Boat from {self._source} to {self._destination}'
        
    def process_order(self, order):
        # This would have the actual logic of processing the truck dispatch
        # The following string is a placeholder since this logic is not relevant to the project
        print(f'Order {order.id} - Boat Dispatch from {self._source} to {self._destination}')

        # After processing the stage, this triggers the next stage in the route for processing
        # This is an example of the chain of responsibility pattern
        if self.next_stage:
            return self.next_stage.process_order(order)
        else:
            return None 