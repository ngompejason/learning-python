import threading
import time
import random

class RestaurantOrder:
    def __init__(self, order_id:int = None, details:str = None) -> None:
        self.order_id = order_id
        self.order_details = details
        self.status:str = "Pending"
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def place_order(self):
        with self.lock:
            if self.status == "Pending":
                print(f"Order {self.order_id}: {self.order_details} has been placed.")
            else:
                print(f"Order {self.order_id} cannot be placed. Current status: {self.status}")

    def preparing_order(self):
        with self.lock:
            if self.status == "Pending":
                self.status = "Preparing"
                print(f"Order {self.order_id}: {self.order_details} is now preparing.")
                # Simulate preparation time
                preparation_time = random.uniform(1, 3)  # Random time between 1 and 3 seconds
                time.sleep(preparation_time)
                print(f"Order {self.order_id}: Preparation complete.")
            else:
                print(f"Order {self.order_id} cannot be prepared. Current status: {self.status}")

    def complete_order(self):
        with self.lock:
            if self.status == "Preparing":
                self.status = "Completed"
                print(f"Order {self.order_id}: {self.order_details} has been completed.")
            else:
                print(f"Order {self.order_id} cannot be completed. Current status: {self.status}")

def simulate_multiple_orders():
    menu = ["Burger", "Pizza", "Pasta", "Salad", "Soda"]
    orders = []
    
    # Create a list of orders with random details
    for i in range(10):  # Simulate 10 orders
        order_id = i + 1
        details = random.choice(menu)
        orders.append(RestaurantOrder(order_id, details))
    
    # Function to process each order
    def process_order(order: RestaurantOrder):
        order.place_order()
        order.preparing_order()
        order.complete_order()

    # Create and start threads for processing each order
    threads = []
    for order in orders:
        thread = threading.Thread(target=process_order, args=(order,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    simulate_multiple_orders()
