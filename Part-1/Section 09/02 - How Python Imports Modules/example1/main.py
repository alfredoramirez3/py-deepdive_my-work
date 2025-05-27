# main.py

print('================================')
print('Running main.py - module name: {0}'.format(__name__))

import module1

print(f'module1: {module1}')

module1.pprint_dict('main.globals', globals())

import sys
print(f'sys.path: {sys.path}')
print(sys.modules['module1'])

print('================================')