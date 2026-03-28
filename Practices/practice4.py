# list = ["apple","banana","Licchi","jackfruit"]
# print(type(list),list)

# def len_of_list(list):
#     print(len(list))
#     return list
# len_of_list(list)


# def show(n):#recursive function
#     if(n==0): 
#         return
#     print(n)
#     show(n-1)
    
# show(10)


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return factorial(n-1)*n
print(factorial(7))