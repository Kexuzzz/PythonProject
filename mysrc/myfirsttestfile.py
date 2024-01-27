from loguru import logger
from icecream import ic

a = int(input())
logger.info("a = " + str(a))


def myfuncsum(z: int) -> int:
    """

    :rtype: int
    :param z:
    :return:
    """
    return z ** z


ic(myfuncsum(6))
# print(myfuncsum(a))
