def func(n, **kwargs):
    """This is a function

    Args:
        n (a number): any number

    Raises:
        TypeError: must be greater than 2

    Returns:
        dictionary : returns kwargs as a dictionary
    """
    if n < 2:
        raise TypeError
    return kwargs

def main():
    ret = func(2, a=100, b=200, c=300)
    print(ret)
    print(list(ret.items()))
    return None

if __name__ == '__main__':
   main()