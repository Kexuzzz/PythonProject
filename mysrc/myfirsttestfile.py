from loguru import logger
from icecream import ic
a = int(input())
logger.info("a = "+ str(a))
def myfuncsum(z):
    return z ** z
ic(myfuncsum(6))
print(myfuncsum(a))