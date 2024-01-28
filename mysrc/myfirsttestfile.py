from loguru import logger
from icecream import ic

a = int(input('Введите число: '))
logger.info("a = " + str(a))


# noinspection SpellCheckingInspection
def myfuncsum(z: int) -> int:
    """

    :param z:
    :return:
    :rtype: int
    """
    return z**z


ic(myfuncsum(6))
""" print(misfunction(a))"""
