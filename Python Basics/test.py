

def test(t=1, **kwargs):
    print(t)
    print(kwargs)

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

print(test(a=2, b=3))