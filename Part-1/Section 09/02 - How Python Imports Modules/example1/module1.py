# module1.py

print('----- Running {0} -----'.format(__name__))


def pprint_dict(header, d):
    print('\n\n----------------------------------------')
    print('***** {0} *****'.format(header))
    for ndx, (key, value) in enumerate(d.items()):
        # print(key, value)
        print(f'index: {ndx}, key: {key}: , value: {value}')
    print('----------------------------------------\n\n')


pprint_dict('module1.globals', globals())

print('----- End of {0} -----\n\n'.format(__name__))