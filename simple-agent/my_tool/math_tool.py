from agents import function_tool

@function_tool
def plus(n1:int,n2:int):
    """This is plus function
        arg:
            n1:int
            n2:int
        return str
    """
    
    print("Plus tool fire--->")
    return f"Your answer is {n1+n2}"



@function_tool
async def subtract(n1:int,n2:int):
    """This is subtract function
        arg:
            n1:int
            n2:int
        return str
    """
    
    print("subtract tool fire--->")
    return f"Your answer is {n1-n2}"



@function_tool
async def multiply(n1:int,n2:int):
    """This is multiply function
        arg:
            n1:int
            n2:int
        return str
    """
    
    print("multiply tool fire--->")
    return f"Your answer is {n1*n2}"