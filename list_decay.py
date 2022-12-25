import time

items = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def decay(decay_rate, max_duration, items = items):
    start = time.time()
    now = start
    while now <= start + max_duration:
        x = items.pop()
        print(x)
        if not items: break
        time.sleep(decay_rate)
        now = time.time()

    if not items: print('ran out of items')
