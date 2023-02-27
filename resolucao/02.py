from collections.abc import Generator


def fibo() -> Generator[int, None, None]:
    """Generates Fibonacci sequence number by number."""
    value: int = 0
    next_value: int = 1

    while True:
        yield value
        value, next_value = next_value, value + next_value


def find_in_fibo(x: int) -> bool:
    """Finds `x` in the Fibonacci sequence using `fibo` generator."""
    value = fibo()

    while (temp := next(value)) <= x:
        if temp == x:
            return True
    return False


if __name__ == '__main__':
    check: bool = find_in_fibo(x := int(input('Informe o número a ser checado: ')))
    print(
        f'{x!r} is in the Fibonacci sequence.' if check
        else f'{x!r} is not in the Fibonacci sequence.'
    )
