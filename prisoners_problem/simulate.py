import random


def seed_random(i: int):
    random.seed(i)


def try_find_self(boxes: list, start: int, limit: int) -> bool:
    next_box = boxes[start]
    num_opened = 1
    while next_box != start and num_opened < limit:
        next_box = boxes[next_box]
        num_opened += 1
    return next_box == start


def sample(n: int = 100, limit: int = 50, strategy=try_find_self) -> int:
    """Takes a number boxes, n, the total number of attempts per person
    allowed, limit, and a strategy function, strategy.

    strategy(boxes: list, person: int, limit: int) -> bool

    It takes a list of boxes (in the room), a person's ID (also the number on
    their dollar), and the total number of moves allowed. Currently, this is on
    the honor system."""
    # boxes = random.sample(range(n), k=n)
    boxes = list(range(n))
    random.shuffle(boxes)
    return sum(strategy(boxes, person, limit) for person in range(n))


def nsamples(n: int, strategy=try_find_self) -> float:
    """Takes a number of samples, n, and a strategy function, strategy.

    strategy(boxes: list, person: int, limit: int) -> bool

    It takes a list of boxes (in the room), a person's ID (also the number on
    their dollar), and the total number of moves allowed. Currently, this is on
    the honor system."""
    return sum([sample(100, 50, strategy) == 100 for _ in range(n)]) / n


if __name__ == "__main__":
    seed_random(5)
    print(nsamples(1000))
