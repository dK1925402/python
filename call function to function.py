# Sum function
def sum (x , y ):
    return x+y 

# Square function
def square (num):
    return num*num

# call to sum funtion 
print (sum ( 2,7))

#call funtion in funtion first call sum and return of sum to pass square function

# square(sum(2,7))  ---> square(2+7) --> square(9)  -----> 9*9 -----> 81  

print (square(sum(2,7))) 
