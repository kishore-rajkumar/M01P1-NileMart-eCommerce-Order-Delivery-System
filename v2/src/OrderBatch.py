from Order import Order
# OrderBatch is an aggregation of order objects
# It reads in the details from the order_batch_config file and creates a list of order objects
class OrderBatch:
    def __init__(self):
        self._order_batch = []

    def __str__(self):
        pass

    def read_config(self, order_batch_config):
        # Opens the file and reads all the order rows, stripping newline character at the end
        # Using the 'with' keyword automatically closes the file when the block is finished or if an error happens
        with open(order_batch_config, 'r') as obatch_file:
            obatch_lines = [obatch_line.rstrip() for obatch_line in obatch_file]

        # An order object is created for each row, and all the order objects are aggregated in the OrderBatch object
        for order_entry in obatch_lines:
            order_details = order_entry.split('-')
            order = Order(order_details[0], order_details[1], order_details[2], order_details[3], order_details[4], order_details[5], order_details[6])  

            self._order_batch.append(order)

    def get_orders(self):
        return self._order_batch
