#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
while True: #infinite loop for error handling
    user_input = input("Enter number of terms: ") 
    try: 
        terms = int(user_input)
        if terms > 0:
            break   #end loop if condition is met
        else:
            print("Please enter a positive integer.")
    except:    #handles other exception (x !< 0, x !> 0)
          print("Please enter a positive integer.")
fibonacci= []
for fib in range(terms): #first two terms are given in fibonacci
    if fib == 0:
        fibonacci.append(fib)
    elif fib == 1:
        fibonacci.append(fib)
    else:
        fibonacci.append((fibonacci[-1]) + (fibonacci[-2])) #fibonacci sequence, fn = fn-1 + fn-2
print(*fibonacci) #* removes brackets and seperates by space
    