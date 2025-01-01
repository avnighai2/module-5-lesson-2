class Employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print("Destructur called")

def CreatObj():
    print('Making object...')
    obj = Employee()
    print('Function end...')
    return obj

print('Calling CreateObj() function...')
obj = CreatObj()
print('Program end...')