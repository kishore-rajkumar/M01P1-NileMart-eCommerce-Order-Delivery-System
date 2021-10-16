from DeliveryMap import DeliveryMap
from DeliveryRoute import DeliveryRoute
from DeliveryStage import TruckDispatch,TrainDispatch,FlightDispatch,ShipDispatch,BoatDispatch

# DeliveryStage is an object storing information for a specific stage of a specific route
# It'll also store the next stage in the route
class DeliverySystem:
    def __init__(self):
        self.delivery_centers = []
        self.stage_routes = {}

    def populate_route(self, center, stages):
        stage_list = []
        # This parses the stage strings and creates all stage objects
        for stage in stages:
            source, dispatch_method, destination = stage.split('-')
            if (dispatch_method == 'truck'):
                stage_list.append(TruckDispatch(source, destination))
            elif (dispatch_method == 'train'):
                stage_list.append(TrainDispatch(source, destination))
            elif (dispatch_method == 'flight'):
                stage_list.append(FlightDispatch(source, destination))
            elif (dispatch_method == 'ship'):
                stage_list.append(ShipDispatch(source, destination))
            elif (dispatch_method == 'boat'):
                stage_list.append(BoatDispatch(source, destination))

        # This adds the next stage information in each stage object, creating a chain
        for i in range(0, len(stage_list) - 1):
            stage_list[i].next_stage = stage_list[i+1]
        
        # Finally, the DeliveryRoute object is created, composing all its stages, in order
        route = DeliveryRoute(stage_list, destination)
        print(route)

        return route

    def configure(self, DELIVERY_MAP_CONFIG):
        # Creates and triggers DeliveryMap to ingest destination and stage information
        delivery_map = DeliveryMap()
        delivery_map.read_config(DELIVERY_MAP_CONFIG)

        self.delivery_centers.extend(delivery_map.get_destinations())
        
        # It goes through each destination-delivery_type and creates appropriate objects for stages and the route
        for center_delivery_type in self.delivery_centers:
            stages = delivery_map.get_stages(center_delivery_type)
            route = self.populate_route(center_delivery_type, stages)
            self.stage_routes[center_delivery_type] = route

    # Returns the route for a particular destination and with a particular velivery type which can then be used for dispatching an order
    def get_route_v2(self, destination,delivery_type):
            return self.stage_routes[(destination,delivery_type)]
