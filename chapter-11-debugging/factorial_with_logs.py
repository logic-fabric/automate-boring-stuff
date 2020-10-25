import logging


logging.basicConfig(
    filename='factorial_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def factorial(n):
    logging.debug(f"Start of factorial({n})")

    result = 1
    for i in range(1,n + 1):
        result *= i
        logging.debug(f"i is {i}, reult is {result}")
    
    logging.debug(f"End of factorial({n})")

    return result


if __name__ == '__main__':
    print(factorial(5))
    logging.debug("End of program")
