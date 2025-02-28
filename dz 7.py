'''def double(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@double
def get_number():
    return 10

print(get_number())  '''

'''@double
def square(n):
    return n ** 2

print(square(3))  '''
