def fact_iter(n: int) -> int:
    """Return n! for n >= 0."""
    if n < 0:
        raise ValueError("n must be non-negative")

    total = 1
    for k in range(1, n + 1):
        total *= k
    return total


if __name__ == "__main__":
    print(fact_iter(11))
