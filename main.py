# def addition(a,b):
#     return a+b
# a=addition(2,3)
# print(a)
# add=addition
# print(add)          # function is an object
# print(add(2,4))

# def adder(x):
#     def addition(b):
#         return x+b
#     return addition
# add=adder(10)
# print(add(5))

# Decorators: is a function that takes another function as its argument an return another function.

# def decoratorFunction(originalFunc):
#     def wrapperFunction():
#         print("Gogulan is using inside function.")
#
#         return originalFunc()
#
#     return wrapperFunction
#
#
# @decoratorFunction
# def display():
#     print("display function")
#
# display()

# First class functions:
# - passing functions as arguments
# - returning functions
# - assigning function to a variable

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='w'
)

def exception_handling(func):
    # to include any exceptions in the ETL framework process
    def wrapperfunction():
        try:
            print(x)
        except:
            print("An exception occurred")

        return func()

    return wrapperfunction


def loggingtest(func):
    # to log any issues after each step of the ETL framwork process
    def wrapperfunction():
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning("This is a warning message")
        logging.error('This is an error message')
        logging.critical('This is a critical message')
        return func()
    return wrapperfunction


@exception_handling
@loggingtest
def initiate():
    print("initiate function")


initiate()
