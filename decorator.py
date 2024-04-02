def logtime(func):
    def wrapper():
        print("Before")                 # do something before
        val = func()
        print("After")                  # do something after
        return val
    return wrapper
@logtime
def hello():
    print("Hello")

hello()