def add(num1=str, num2=str):

    if num1 == "" or num2 == "":
        return "Invaild Operation"
    
    if num1 is None or num2 is None:
        return "Invaild Operation"
    
    result = int(num1) + int(num2)
    
    return result
