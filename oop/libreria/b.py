from a import A

class B:
    def __str__(self) -> str:
        return 'object -> class B'
    
    def futuro(self) -> None:
        # utilezzerà qualcosa della classe A
        pass

if __name__ == "__main__":
    b = B()
    print(b)
    a = A()
    print(a)