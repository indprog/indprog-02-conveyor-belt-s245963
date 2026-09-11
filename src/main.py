number_of_motors = int(input())
weight_of_packages = int(input())
if weight_of_packages / number_of_motors <= 12:
    print("Yes! The conveyor belt can carry the packages.")
else: 
    print("No. The conveyor belt cannot carry the packages.")
