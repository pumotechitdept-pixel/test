'''
def test():
    print("Hello, World!")

test()


def test123(a):
    return a + 5

result = test123(10)
print(result)

def multiply(a, b):
    return a * b    

res1 = multiply(2, 3)
print(res1)


bset={"Hello", "World", "Python", "Code"}

for item in bset:
    print(item)


a ={"Name","John","Age", 30}
b ={"Name1","Alice","Age", 25}
c ={"Name2","Bob","Age", 28}
d ={"Name3","Charlie","Age", 35}

e =a.union(b,c,d)
print(e)


set1 = {1, 2, 3, 4, 5,"mango"}
tuple1 = (6, 7, 8, 9, 10,"hello","world")
e1 = set1.union(tuple1)
print(e1)



a1 = {1, 2, 3, 4, 5}
a2 = {" apple", "banana", "cherry"}
a2.update(a1)
print(a2)


a1 ={"Name","John","Age", 30}
a2 ={"Name1","Alice","Age", 25}
a2.intersection_update(a1)
print(a2)

'''
set1 = {"apple", "banana", "cherry",1,0}
set2 = {False,"google", "microsoft", "apple", 1 ,True}
set1.difference_update(set2)
print(set1)
#print(set2)


def remove_duplicates(lst):
    return list(set(lst))

res = remove_duplicates([1, 2, 3, 2, 1, 4, 5, 4])
print(res)

