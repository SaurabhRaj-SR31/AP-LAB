def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    print("Calling the inner function:")
    inner_function()


outer_function()
