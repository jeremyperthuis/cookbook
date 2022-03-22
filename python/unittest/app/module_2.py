from app import module_1


def multiply(arg1, arg2):
    return arg1*arg2

def add_multiply(arg1,arg2):
    return module_1.add(arg1*arg2,arg2)


if __name__ == "__main__":
    print(multiply(4,7))
    print(add_multiply(4, 7))