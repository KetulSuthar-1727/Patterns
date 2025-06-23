# def pattern():

#     user = int(input("Enter the number : "))

#     inin = 1
#     ini = 8
#     for i in range(0,user):
        
#         for j in range(0,user-i):
#             print("*",end="")
        
#         for j in range(1,inin):
#             print(" ",end="")

#         for j in range(0,user-i):
#             print("*",end="")
#         print("")
#         inin += 2

#     for i in range(1,user+1):
        
#         for j in range(0,i):
#             print("*",end="")
        
#         for j in range(0,ini):
#             print(" ",end="")

#         for j in range(0,i):
#             print("*",end="")

#         ini -= 2
#         print(" ")
        
# pattern()

def func():
    user = int(input("enter the number : "))
    count = user
    for i in range(0,user):
        print(count,end=" ")
    print("")
        
    for j in range(0,user-2):
            print(count,end="")
            count -= 1
            print(f"{count}" * (user+2),end="")
            count += 1
            print(count)

    for k in range(0,user):
        print(count,end=" ")

func()