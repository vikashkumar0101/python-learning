class DogNotFoundError(Exception):
    pass
try:
    raise DogNotFoundError()
except DogNotFoundError:
    print("Dog Not found")
