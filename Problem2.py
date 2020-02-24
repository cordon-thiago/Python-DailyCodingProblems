# Problem 2 - Daily Coding Problem

'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the
numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''

# Solução usando For
def problem2_1(arr):
    # Array que irá receber o resultado da multiplicação dos itens
    arrNew = []
    # Percorre array
    for i1,val1 in enumerate(arr):
        num = 1
        # Percorre array e multiplica numeros exceto o que está no loop anterior
        for i2,val2 in enumerate(arr):
            if i1!=i2:
                num = num*val2
        # Adiciona números multiplicados em novo array
        arrNew.append(num)
    return print(arrNew)

arr = [1, 2, 3, 4, 5]
#arr = [3, 2, 1]
problem2_1(arr)