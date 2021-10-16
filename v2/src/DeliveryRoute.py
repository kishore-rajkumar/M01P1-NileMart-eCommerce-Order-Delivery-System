# DeliveryRoute stores all the stage objects for a specific route, in order
class DeliveryRoute:
    def __init__(self, stage_list, destination):
        self._stage_list = stage_list
        self._destination = destination

    def __str__(self):
        route = ','.join(str(stage) for stage in self._stage_list)
        return f'Route to {self._destination}: {route}\n'
        
    # This triggers the first stage which will, in turn, trigger the following stage and so on, until delivery finishes
    def process_order(self, order):
        self._stage_list[0].process_order(order)