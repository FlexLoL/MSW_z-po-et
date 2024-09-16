import time
import random
from pynput.mouse import Listener

mouse_positions = []

def on_move(x, y):
    current_time = time.time()
    mouse_positions.append((x, y, current_time))
    
    if len(mouse_positions) >= 100:
        return False
def generate_random_seed():
    print("Pohybute myší pro vygenerovaní náhodného semínka:")

    with Listener(on_move=on_move) as listener:
        listener.join()
    
    random_seed = 0
    for x, y, t in mouse_positions:
        random_seed += int(x * y * t)
    
    # Oříznutí na platné hodnoty a vrácení semínka
    return random_seed % (2**32)

# Generování náhodného semínka
random_seed = generate_random_seed()
print(f"Vygenerované náhodné semínko: {random_seed}")
