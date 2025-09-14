def add_num(a,b):
    c=a+b
    return print("output is:", c)
add_num(2,3)

def calculator(num1,num2,operation):
    if operation == "add": 
        answer= num1 + num2 
    elif operation == "subtract":
        answer = num1 - num2 
    elif operation == "divide" :
        if num2 == 0:
            return print (f"{num1} {operation} {num2} Error : Division by 0")
        answer=num1/num2
    else:
        return print (f" {num1} {operation} {num2} Error: {operation} is an Invalid Operation")
    return print (f"Solution : {num1} {operation} {num2} = {answer}")
calculator(10,5,"add")
calculator(10,4,"exponent") 
calculator(2,0,"divide")
calculator(12,6,"divide")
