#function to check if the brackets are balanced 
def balbrack(expr):
    stack = []
 
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # check if the stack is empty
    if stack:
        return False
    return True
 
# main program
if __name__ == "__main__":
    expr = input()
    
   if balbrack(expr):
        print("Balanced")
    else:
        print("Not Balanced")
