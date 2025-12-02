# initiate a class
class employee:
    # special method/magic method/dunder method
    def __init__(self):
        print("Started Executing attributes/data")
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        print("Initialised Executing attributes/data")
    
    def travel(self, destination):
        print("This travel function is called")
        print(f"Employee is traveling to {destination}")
    
sam = employee()
print(sam.salary)
sam.travel("New York")