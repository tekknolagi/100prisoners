import random


def try_find_self(boxes, start, limit):
    next_box = boxes[start]
    num_opened = 1
    found = False
    while next_box != start and num_opened < limit:
        next_box = boxes[next_box]
        num_opened += 1
    return next_box == start


def sample(n=100, limit=50):
    # boxes = random.sample(range(n), k=n)
    boxes = list(range(n))
    random.shuffle(boxes)
    return sum(try_find_self(boxes, person, limit) for person in range(n))


if __name__ == '__main__':
    print(sample(100, 50))
