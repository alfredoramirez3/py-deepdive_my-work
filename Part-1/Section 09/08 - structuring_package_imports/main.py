# main.py

import common.validators as validators
import common

# from common.validators import * # not recommended

validators.is_boolean('True')
validators.is_json('{}')
validators.is_numeric(10)
validators.is_date('1-1-2025')



print('main.py executed')

print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)

print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

print('\n\n***** validators *****')
for k in validators.__dict__.keys():
    print(k)

# print('\n\n***** numeric *****')
# for k in validators.numeric.__dict__.keys():
#     print(k)