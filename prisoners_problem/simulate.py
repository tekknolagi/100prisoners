import random


def seed_random(i):
    random.seed(i)


def try_find_self(boxes, start, limit):
    next_box = boxes[start]
    num_opened = 1
    while next_box != start and num_opened < limit:
        next_box = boxes[next_box]
        num_opened += 1
    return next_box == start


def sample(n=100, limit=50, strategy=try_find_self):
    # boxes = random.sample(range(n), k=n)
    boxes = list(range(n))
    random.shuffle(boxes)
    return sum(strategy(boxes, person, limit) for person in range(n))


def nsamples(n):
    return sum([sample(100, 50) == 100 for _ in range(n)]) / n


if __name__ == "__main__":
    seed_random(5)
    print(nsamples(1000))
