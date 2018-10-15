def outer(message):

    def inner():
        print(message)

    return inner

closure = outer("hello!")
closure()