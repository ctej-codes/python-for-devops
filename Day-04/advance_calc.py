import basic_calculator
import sys

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "sub":
    output = basic_calculator.sub(num1, num2)
    print(output)



