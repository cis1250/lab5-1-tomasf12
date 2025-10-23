
def fibValidate():
    """Prompts and Validates positive int"""
    
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
    
    return terms