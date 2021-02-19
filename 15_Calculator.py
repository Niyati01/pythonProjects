
def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    is_calc_reset = False
    number1 = int(input("What's your first number? "))
    while not is_calc_reset:
        number2 = int(input("What's your second number? "))

        for symbol in operations:
            print(symbol)
        operation_selected = input("Select from the above operations : ")
        result = operations[operation_selected](number1,number2)
        print(result)
        reset_calculator = input("Type 'y' to continue calculating and 'n' to reset : ")
        if reset_calculator == 'n':
            #is_calc_reset = True
            calculator()
        if reset_calculator == 'y':
            number1 = result

calculator()