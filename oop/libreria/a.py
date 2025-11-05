class A:
    def __str__(self) -> str:
        return 'object -> class A'


if __name__ == "__main__":
    a = A()
    print(a)