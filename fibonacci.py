## This file runs everything
from modularFib.fibValidate import fibValidate 
from modularFib.fibGenerate import fibGenerate 
from modularFib.fibPrint import fibPrint

if __name__ == "__main__":
    terms = fibValidate()
    fib = fibGenerate(terms)
    fibPrint(fib)
