#var1 = 45 # int
#var2 = -23.4567 #float
var3 = "Hi" #string
v4 =True #boolean

str1 = "hello\n"
str2 = "world"
str3 = str1 + str2 #helloworld

#print(str1 + str2)
#print(var1 + var2 )

#print(False + 12) #21.5433
#print(False - 12)
#print(False / 12)
#print(False * 12)

#var_int = "10"

#casting
#print(int(var_int))
#print(float(var_int))
#print(bool(var_int))



#var = input("Enter number\n")
#var = int(var)

#print(var * var)


#var = float(input("Enter a num"))

#not True = False
#True or False = True
#True & False = False

#print(not True)
#print(False or True)
#print(False & True)

#var1 = "hello"
#var2 = var1

#if 10 < 11:
 #   print(True)
#else:
 #   print(False)

#var = int(input("Enter a num\n")) #10

#for i in range(0, var):
 #   print("Loading ...", i, "%")
  #  if i == 100:
   #     print("Finish")
    #    break
#else:
 #   print("deny")


#for i in range(0, 10):
 #   print(i) #9

  #  count = 0
   # while count != 10:
    #    print(count)
     #   count += 2


import random

life = 3
num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))
var_win_num =  random.randint(num1, num2)


while life != 0:

    var_input = int(input("Enter a num"))

    if var_input == var_win_num:
        print("You win")
        break
    else:

        if var_input < var_win_num:
            print("Your guess was lower than the right one")
        else:
            print("Your guess was bigger than the right one")

        life -= 1

else:
    print("Life = " + life)




