#Desafio 1 Daily coding problems
# Teste Sourcetree

'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

numList = [10,15,3,5]
k = 20

# Usando While
def desafio1_1(list, num):
	i1 = 0
	while i1 <= len(list)-1:
		num1 = list[i1]
		i2 = 0
		while i2 <= len(list)-1:
			if i1 != i2:
				num2 = list[i2]
				if (num1+num2) == num:
					return print([num1, num2])
					break
			i2+=1
		i1+=1
	return print("Nenhuma combinação somada resulta em {0}".format(num))

# Usando List Comprehension
# List comprehension não tem como dar break no loop
def desafio1_2(list, num):
	listRet = [[val1,val2] for i1,val1 in enumerate(list) for i2,val2 in enumerate(list) if (i1!=i2) & ((val1+val2) == num)]
	if listRet:
		return print(listRet[0])
	else:
		return print("Nenhuma combinação somada resulta em {0}".format(num))

# Usando For
def desafio1_3(list, num):
	for i1,val1 in enumerate(list):
		for i2, val2 in enumerate(list):
			if (i1 != i2) & ((val1 + val2) == num):
				return print([val1, val2])
				break
	return print("Nenhuma combinação somada resulta em {0}".format(num))

desafio1_1(numList, k)
desafio1_2(numList, k)
desafio1_3(numList, k)