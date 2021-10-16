# DeliveryMap reads from one of the delivery map files and stores destinations, and stages for each destination
class DeliveryMap:
    def __init__(self):
        self._destinations = [] # tuple destination & delivery type
        self._delivery_map = {}

    def __str__(self):
        pass

    # This method creates two structures
    # It creates a list of all the destinations found
    # It also creates a dictionary with destination as the key, and list of stages as the value
    def read_config(self, delivery_map_config):
        with open(delivery_map_config, 'r') as dmap_file:
            dmap_lines = [dmap_line.rstrip() for dmap_line in dmap_file]


        for line in dmap_lines:
            destination,delivery_type, stages = line.split(' ')
            self._destinations.append((destination,delivery_type)) # tuple destination & delivery type
            stages = stages.split(',')
            self._delivery_map[(destination,delivery_type)] = stages # tuple destination & delivery type
        print(f'Destinations: {self._destinations}\n')

    def get_destinations(self):
        return self._destinations 

    def routing_map(self):
        return self._delivery_map

    def get_stages(self, delivery_center_delivery_type_tuple):
         return self._delivery_map[delivery_center_delivery_type_tuple]