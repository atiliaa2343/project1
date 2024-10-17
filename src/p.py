import sys

#creates a zipped iterator that pairs decimal values  with 
#their corresponding roman numeral
m = zip(((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ), 
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')) 

def calc(problem): 
    
    ''' 
    Evaluates a roman numeral equation. 
    
    Parameters: 
    It cannot take any other values other than roman numerals for the equation. 
    
    Returns: 
    The result of the equation in roman numerals.
    '''  
    
    #creates a dictionary that maps roman numerals to their decimal values
    global x  
    x = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    y = []; z=''; a='0'; problem='+'+problem

    try: 
        #loops through each character in the problem
        for c in problem.upper(): 
            #checks if character is a roman numeral
            if c in x: 
                #checks if current character is a symbol
                z += c
                y.append(x[c]) 
                #handles subtractive notation
                if len(y) > 1 and y[-1] > y[-2]:
                    y[-2] *= -1
                x[z] = sum(y) 
                #handles arithmetic operators
            elif c in "+/*-":
                a = '(' + a + z + ')' + c
                y = []
                z = ''
            else: 
                #checks for invalid characters
                raise ValueError("Invalid character in input")

        #evaluates expression
        a += z
        i = eval(a, x)

        # Check for special conditions
        if i == 0:
            return "0 does not exist in Roman numerals."
        elif isinstance(i, float):
            return "There is no concept of a fractional number in Roman numerals."
        elif i < 0:
            return "Negative numbers can't be represented in Roman numerals."
        elif i > 3999:
            return "You're going to need a bigger calculator."

        # Convert result to Roman numeral
        r = ''
        for n, c in m:
            d = int(i / n)
            r += c * d
            i -= n * d

        return r

    except Exception as e:
        return "I don't know how to read this."


#executes script
if __name__ == "__main__":
    if len(sys.argv) != 2: 
        print("There should be two argumens") 
        sys.exit(1) 
        
        
    problem = sys.argv[1] 
    result = calc(problem) 
    print(result)