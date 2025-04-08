class employee:
    def __init__(self):
        print("An Employee is created")
    
    def __del__(self):
        print("An Employee is deleted")
        
obj = employee()
del obj