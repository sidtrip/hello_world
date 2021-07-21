# Practicing Exception Handling

a = int(input())
b = int(input())
try:
    c = a / b
#Divide by 0 error
    print(c)
except ZeroDivisionError:
    print('Invalid input, divisor cannot be zero') 

try:
    print(d)
except NameError:
    print('Variable d is not defined')

try:
    f = open('abc.txt','r')
    f.close()
    #Wont implement if error occured so go to finally
except FileNotFoundError:
    print("Invalid file name. Please Check again.") 

except:
    print('Somthing that I dunno, but still went wrong')

finally:
    f.close()
    print('From finally block')



