# Purpose: Ensures a class has only one instance and provides a global point of access to that instance.


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Testing Singleton
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True, both refer to the same instance
