# timing.py
"""
Times how long a snippet of code takes to run
over multiple iterations
"""

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple('Timing', 'repeats elapsed average')

def timeit(code, repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)
   
if __name__ == '__main__':
    # get code, repeats from command line arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', 
                        type=str, help='python code snippet')
    parser.add_argument('-r', '--repeats', 
                        type=int, default=10, help='times to repeat')
    args = parser.parse_args()
    
    # print(args.code)
    # print(args.repeats)
    code = args.code
    repeats = args.repeats
    result = timeit(code, repeats)
    
    print(f'timing:\n  {code=}')
    print(f'  {result=}')
    
    