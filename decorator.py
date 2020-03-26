def checker(is_run):
    def dec(func):
        def wrapper():
            return "hihi!" + func()

        if is_run:
            return wrapper
    return dec

@checker(is_run=True)
def hello_world():
    return("Hello world")

if __name__ == "__main__":
    print(hello_world())
