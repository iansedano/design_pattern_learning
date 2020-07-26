
from logger import Logger

logger_object = Logger("log.txt")

logger_object.info("this is FYI")

log = Logger("mylog.txt")

log.critical("this is a major f up")
'''

from singleton import SingletonObject

obj1 = SingletonObject()

obj1.val = "Hello"
print(f"obj1 {obj1}")

print("-----")

obj2 = SingletonObject()
obj2.val = "World"

print(f"obj1 {obj1}")
print(f"obj2 {obj2}")

print(f"{obj1 == obj2}")

'''