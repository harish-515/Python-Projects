def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Divison by zero in meaningless"
    except:
        return "Error while executing the divison"

        
print(divide(1,0))            