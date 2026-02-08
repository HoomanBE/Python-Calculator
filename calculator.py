def main():
    num_ope = three_numbers_operators()
    count = 0
    number1 = 0
    t_or_f = 0
    while True:
        question = input("Do you want to put more numbers? (Y/N) : ")
        if question.upper() not in ["Y","N"]:
            print("Invalid Input try again")
            continue
        while True:
            if question.upper() == "Y":
                if count == 0:
                    number1 += num_ope[0]
                    result = calculation(number1 , num_ope[1] , num_ope[2])
                    if result == "Error!!!":
                        problem = input("Your previous operation resulted in division by zero," 
                    "or has a problem Do you wana restart or shut down? (R,S) : ")
                        if problem.upper() not in ["R","S"]:
                                print("Invalid Input try again")
                                continue
                        print(f'{num_ope[0]} {num_ope[1]} {num_ope[2]} = {result}')
                        print(f"Current result is : {result}")    
                        true_or_false = problem_error(problem)
                        t_or_f = 1
                        start_again = True
                        count += 1
                        break 
                elif count != 0:
                    print(f'{result} {num_ope2[0]} {num_ope2[1]} = {x}')
                    result = x
              
                num_ope2 = two_numbers_operators()
                print(f"your operation is {result} {num_ope2[0]} {num_ope2[1]}")
                x = calculation(result , num_ope2[0] , num_ope2[1])
                count += 1
                start_again = True
                break            
            elif question.upper() == "N":
                if count == 0:
                    number1 += num_ope[0]
                elif count != 0:
                    print(result , num_ope2[0] , num_ope2[1],"= " , x)
                    final_answer = x
                    start_again = False
                    break    
                result = calculation(number1 , num_ope[1] , num_ope[2])
                if result == "Error!!!":
                    while True:
                        problem = input("Your previous operation resulted in division by zero," 
                        "or has a problem Do you wana restart or shut down? (R,S) : ")  
                        if problem.upper() not in ["R","S"]:
                            print("Invalid Input try again")
                            continue  
                        true_or_false = problem_error(problem)
                        t_or_f = 1
                        break   
                print(f'{num_ope[0]} {num_ope[1]} {num_ope[2]} = {result}')
                final_answer = result
                start_again = False
                break
            else:
                print("Invalid input, please enter Y or N.")
                continue
        if t_or_f == 1:    
            if true_or_false == True:
                print("Restarting.....")
                num_ope = three_numbers_operators()
                count = 0
                number1 = 0
                t_or_f = 0
                continue
            if true_or_false == False:
                print("Exting program......")
                break
        if start_again == True:
            continue
        elif start_again == False:
            break        
    return final_answer   

     
def three_numbers_operators():
    while True:
        operators_list = ["+" , "-" , "*" , "/" , "//" , "%" , "**"]
        try:
            number1 = float(input("Enter your number : "))
            operators = input("Enter your operator (+ , - , * , / , // , % , **) : ")
            if operators not in operators_list :
                print(f"{operators} is Invalid operators please choose from {operators_list} ")
                continue
            number2 = float(input("Enter your next number : "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue    
        print(f"your operation is {number1} {operators} {number2}")
        break
    return number1 , operators , number2    

def two_numbers_operators():
    while True:
        operators_list = ["+" , "-" , "*" , "/" , "//" , "%" , "**"]
        try:
            operators = (input("Enter your operator (+ , - , * , / , // , % , **) : "))
            if operators not in operators_list :
                print(f"{operators} is Invalid operators please choose from {operators_list} ")
                continue
            number2 = float(input("Enter your next number : "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue    
    return operators , number2    
                  
def calculation(number1 , operators , number2):
    result = 0   
    try:
        if operators == "+":
            result += number1 + number2
        elif operators == "-":  
            result += number1 - number2
        elif operators == "*":  
            result += number1 * number2
        elif operators == "%":  
            result += number1 % number2       
        elif operators == "**":  
            result += number1 ** number2       
        elif operators == "/":  
            result += number1 / number2
        elif operators == "//":  
            result += number1 // number2     
    except ZeroDivisionError:
        print("Division by zero is not allowed"  )
        return "Error!!!"  
    except:
        print("An error occurred during the calculation")
        return "Error!!!"  
    return result                  

def problem_error(problem):
    while True:
        if problem.upper() == "R":
            return True
            break
        elif problem.upper() == "S":
            return False
            break
        else:
            print("Invalid Input try again")
            continue      
    
print(main())                              
        
                
            
