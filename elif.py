#Simple Calculator

operand_1=int(input("Enter first operand: "))
operand_2=int(input("Enter second operand: "))

operator=input("Enter the operation to be performed: '+', '-', '*', '/' ")

if operator == '+':
    print(operand_1 + operand_2)
elif operator == '-':
    print(operand_1 - operand_2)
elif operator == '*':
    print(operand_1 * operand_2)
elif operator == '/':
    print(operand_1 / operand_2)
else:
    print("!!!!!!!!!!!None!!!!!!!!!!!")


print("Calculation complete.")