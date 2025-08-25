import random
import time

def generate_id(id_type):
    timestamp = int(time.time())
    generated_id = id_type + str(timestamp) + str(random.randint(1, 100))
    return generated_id
