def print_name(*args, **kwargs):
    print(args)
    print(kwargs)


def print_name1(person,*args, **kwargs):
    print(args)
    print(kwargs)



print_name(name='test', name2= 'name2')
print_name1('person',name='test', name2= 'name2')



# print(*'mike', *'second', 'third')

# myDict = {'header': 'test', 'name': 'testName'}

# for i in myDict:
#     print(i)