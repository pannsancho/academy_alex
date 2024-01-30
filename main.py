def devision(a: int | float, b: int | float):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно!")
    return a/b


def main():
    for i, j in enumerate([1, 2, 3, 4], 0):
        try:
            d = devision(j, i)
        except ZeroDivisionError as e:
            print(e)
        else:
            print(d)


if __name__=="__main__":
    main()