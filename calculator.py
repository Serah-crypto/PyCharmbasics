#write a simple calc. program
#prompts the user to enter first no.,operator(+,*,/,-) and second no.
#based on the operator entered it should provide the correct output

x = float(input("Enter first no: "))
operator = input("Enter operator (+, -, *, /): ")
y = float(input("Enter second no: "))

if operator == '+':
    result = x + y
    print("Output:", result)

elif operator == '-':
    result = x - y
    print("Output:", result)

elif operator == '*':
    result = x * y
    print("Output:", result)

elif operator == '/':
    if y != 0:
        result = x / y
        print("Result:", result)
    else:
        print("Error")

else:
    print("Invalid operator! use only +, -, *, or /")








