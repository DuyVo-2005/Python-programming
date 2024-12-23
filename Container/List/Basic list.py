'''import decimal
decimal.getcontext().prec=10
print(decimal.Decimal(1)/decimal.Decimal(13))'''
'''n = int(input())
if n==0:
    raise Exception("Error")'''
'''try:
    print(1/n)
except ZeroDivisionError:
    print("0 error")
except:
    print("Error")
finally:
    print("Yeah!")'''
list = [1,2,3,4,5]
list2= ['a','b']
#list.insert(8,0)
#list.append(list2)
list.extend(list2)
#list.pop()
#list.pop(0)
#del list
#list.remove('b')
list.reverse()
print(list)
