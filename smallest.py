smallest = None
print('Before:', smallest)
for itervar in [2, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest :
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
