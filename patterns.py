# def function():

#         userinput = int(input("Enter the number : "))

#         for i in range(1,userinput+1):
#             print(" " * (userinput-i),end="")
#             print("*" * (2*i-1))
#         for j in range(userinput,0,-1):
#             print(" " * (userinput-j),end="")
#             print("*" * (2*j-1))

# function()

# def fucntion1():
#      user = int(input("Enter the number : "))

#      for i in range(1,user+1):
#         print("*" * i)
#      for j in range(user-1,0,-1):
#         print("*" * j)   

# fucntion1()

# def function2():
    
#     userinput = int(input("Enter the number : "))

    
#     for i in range(1,userinput+1):
#         if(i%2 == 0): 
#              start = 0               
#         else: 
#              start = 1

#         for j in range(0,i):
#             print(start,end="")
#             start = 1 - start
#         print("")
# function2()

# def function3():
#     user = int(input("Enter the number : "))

#     space = 2*user-2

#     for i in range(1,user+1):
#         for j in range(1,i+1):
#             print(j,end=" ")

#         for j in range(space,0,-1):
#             print(" ",end=" ")
            
#         for j in range(i,0,-1):
#             print(j,end=" ")

#         print("")
#         space -= 2
# function3()

# def function4():
#     user = int(input("Enter the number : "))

#     number = 1

#     for i in range(1,user+1):
#         for j in range(1,i+1):
#             print(number,end=" ")
#             number += 1
#         print("")
# function4()

# def function5():
#     user = int(input("Enter the number : "))

#     c = chr(65)

#     for i in range(1,user+1):
#         for j in range(0,i):
#             print(c,end=" ")
#         c = chr(ord(c) + 1)
#         print("")

# function5()

# def fucntion6():
#     user = int(input("Enter the number : "))

#     c = ord('A')

#     for i in range(1,user+1):
#         print("-" * (user-i),end="")
#         print(chr(c) * (2*i-1), end="")
#         print("-" * (user-i))
        
        
            
# fucntion6()



# def fucntion7():
#     user = int(input("Enter the number : "))

#     c = chr(65)

#     for i in range(1,user+1):
#         for j in range(0,i):
#             print(c,end=" ")
#         c = chr(ord(c) + 1)
#         print("")

# fucntion7()

# def function8():
    
#     user = int(input("Enter the number : "))


#     for i in range(user,0,-1):
#       print("*" * i,end="")
#       print("  " * (user-i),end="")
#       print("*" * i)

#     for j in range(1,user+1):
#       print("*" * j,end="")
#       print("  " * (user-j),end="")
#       print("*" * j)

# function8()

# def function9():
#     user = int(input("Enter the number : "))
#     inin = 2

#     for i in range(1,user+1):
#         print("*" * i,end="")
#         print(" " * (2*user-inin),end="")
#         print("*" * i)

#         inin += 2

#     for j in range(user-1,0,-1):
#         print("*" * j,end="")
#         print(" " * (2*(user+2)-inin),end="")
#         print("*" * j)

#         inin -= 2

# function9()


# def function10():
#     user = int(input("Enter the number : "))
    
    # for i in range(0,user):
    #     print("*",end="")
    # print("")
        
    # for j in range(0,user-2):
    #         print("*",end="")
    #         print(" " * (user-2),end="")
    #         print("*")

    # for k in range(0,user):
    #     print("*",end="")


# function10()

def function11():
    user = int(input("Enter the number : "))
    count = user
    
    


    for i in range (0,(2*user-1)):
      top = i
      left = (2*user-2) - i
      print(user - min(min(top,left)))
        
      print("")
        
    for j in range(0,(2*user-1)):
            
            
      bottom = j
      right = (2*user-2) - j
      print(user - min(min(bottom,right)))
    print("")

    
function11()
