# Enter tree circumference in cm: 120 
# Tree can be cut down: False

circumference = int(input("Enter tree circumference in cm: "))
diameter = circumference/3.14
can_be_cut_down = (diameter >= 50)
print(f"Tree can be cut down: {can_be_cut_down}")