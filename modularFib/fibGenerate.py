from modularFib import terms as ts

def fibGenerate(terms):
    """Generates Fibonacci Sequence from verified int"""
    fibonacci= []
    for fib in range(terms): #first two terms are given in fibonacci
        if fib == 0:
            fibonacci.append(fib)
        elif fib == 1:
            fibonacci.append(fib)
        else:
            fibonacci.append((fibonacci[-1]) + (fibonacci[-2]))