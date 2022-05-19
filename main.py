
# Given an array of integers greater than zero, find if there is a way to
# split the array in two (without reordering any elements) such that the
# numbers before the split add up to the numbers after the split. If so,
# print the two resulting arrays.
#
# In [1]: can_partition([5, 2, 3])
# Output [1]: ([5], [2, 3])
# Return [1]: True
#
# In [2]: can_partition([2, 3, 2, 1, 1, 1, 2, 1, 1])
# Output [2]([2, 3, 2], [1, 1, 1, 2, 1, 1])
# Return [2]: True
#
# In [3]: can_partition([1, 1, 3])
# Return [3]: False
#
# In [4]: can_partition([1, 1, 3, 1])
# Return [4]: False

import random

def can_partition():
    # The function asks the length of the array
    # And fills it by random integer numbers
    # Just set a limit of the integer for debug
    max_value = 1
    field = []
    print("Hello, please enter the size of the array")
    length = int(input('->>'))
    if int(length) < 0:
        print("The size of the array should be bigger than 0")
        return
    field = [random.randint(0, max_value) for i in range(length)]
    print(field)
    for x in range(length):
        v1 = sum(field[:x + 1])
        v2 = sum(field[x + 1::])
        print(v1, v2)
        if v1 == v2:
            newarray1 = field[:x +1]
            newarray2 = field[x + 1::]
            print('Got it', newarray1, newarray2)
            return
    print("Not found")
    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    can_partition()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
