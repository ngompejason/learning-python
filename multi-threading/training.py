import threading
import random
import time

stock: dict = {
    'biscuits': 8,
    'gums': 7,
    'candies': 13
}

def supplier() -> None:
    amount:int  = random.randint(2, 10)
    item:str = random.choice(["biscuits", "gums", "candies"])
    with threading.Lock():
        stock[item] += amount
    print(f"{amount} {item} Added to the stock.\n{item} in stock: {stock[item]}")
    time.sleep(0.5)


def consumer() -> None:
    amount:int  = random.randint(2, 10)
    item:str = random.choice(["biscuits", "gums", "candies"])
    with threading.Lock():
        if stock[item] >= amount:
            stock[item] -= amount
            print(f"{amount} {item} was consumed.\n{item} is stock: {stock[item]}")
        elif stock[item] == 0:
            print(f"No {item} in stock.\n{item} is stock: {stock[item]}")
        else:
            print(f"------------\nCan't consume {amount} {item}. Insufficient {item} in stock.\n{item} is stock: {stock[item]}\n------------")
        time.sleep(0.5)

def simulate_actions() -> None:
    for _ in range(10):
        action_type = random.choice(["consume", "supply"])
        if action_type == "consume":
            consumer()
        else:
            supplier()

if __name__ == "__main__":
    
    threads =[]
    for _ in range(3):
        thread = threading.Thread(target=simulate_actions)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"New Stock: {stock}")