def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  
            return num1 / num2
        else:
            return "Division by zero is not allowed"
    elif operator == '%':
        if num2 != 0:  
            return num1 % num2
        else:
            return "Modulo by zero is not allowed"
    else:
        return "Invalid operator"

result1 = calcule(5, '+', 3)
result2 = calcule(10, '*', 2)
result3 = calcule(8, '/', 4)
result4 = calcule(15, '%', 7)

print(result1)
print(result2)
print(result3)
print(result4)