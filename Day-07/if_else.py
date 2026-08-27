import sys

ec2_type = sys.argv[1]

if ec2_type == "t2.micro":
    print("The ec2 instance type costs 2 dollars")
elif ec2_type == "t2.medium":
    print("The ec2 instance type costs 4 dollars")
elif ec2_type == "t2.large":
    print("The ec2 instance type costs 6 dollars") 
else:
    print("This is not a valid ec2 instance type")  

