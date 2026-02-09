#write a simple calc. program
#prompts the user to enter first no.,operator(+,*,/,-) and second no.
#based on the operator entered it should provide the correct output

num1 = float(input("Enter first no: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second no: "))

if operator == '+':
    result = num1 + num2
    print("Output:", result)

elif operator == '-':
    result = num1 - num2
    print("Output:", result)

elif operator == '*':
    result = num1 * num2
    print("Output:", result)

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error")

else:
    print("Invalid operator! Please use only +, -, *, or /")








