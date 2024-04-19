def example_01():
    T = [4, 3, 0, 2, 5, 1]
    # Essayez aussi avec
    # T = [1, 2, 3, 4, 5, 6]
    for i in range(2):
        T[i], T[T[i]] = T[T[i]], T[i]

    print(T)


def example_02():
    T = [4, 3, 0, 2, 5, 1]
    for i in range(2):
        T[i] = T[T[i]]
        T[T[i]] = T[i]

    print(T)


def example_03():
    x = 1
    y = 2
    x, y = 2, 3
    print(x, y)


def example_04():
    x = 1
    y = 2
    x = 2
    y = 2 + 2
    print(x, y)


if __name__ == '__main__':
    example_01()
    example_02()
    example_03()
    example_04()
