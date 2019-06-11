def matrixMult(a,b):
    result = []
    try:
        m = len(a)
        t = len(a[0])
    except TypeError:
        print("\nError: a is not a matrix")
        return None
    try:
        p = len(b[0])
        t = len(b)
    except TypeError:
        print("\nError: b is not a matrix")
        return None
    n = len(a[0])
    
        
    #Step 1: Print the matricies for user
    print("Matrix a:")
    for x in a:
        string = "| "
        for y in x:
            string += str(y)+" "
        string += "|"
        print(string)
    
    print("\nMatrix b:")
    for x in b:
        string = "| "
        for y in x:
            string += str(y)+" "
        string += "|"
        print(string)   
    
    #Step 2: Check if input format is wrong
    if(len(a) == 0 or len(a[0]) == 0):
        print("\nError: Matrix a is missing values")
    if(len(b) == 0 or len(b[0]) == 0):
        print("\nError: Matrix b is missing values")
    if(n != len(b)):
        print("\nError: n is not the same")
        return None
    count = len(a[0])
    for x in a:
        if(len(x) != count):
            print("\nError: Matrix a incorrect format")
            return None
    count = len(b[0])
    for x in b:
        if(len(x) != count):
            print("\nError: Matrix b incorrect format")
            return None
    
    #Step 3: Compute result[]
    print("\nm:",m,"p:",p,"n:",n)
    for i in range(m):
        array = []
        for j in range(p):
            element = 0
            for k in range(n):
                element += a[i][k] * b[k][j]
            array.append(element)
        result.append(array)
           
            
    #Step 4: Print result[] for user
    print("\nMatrix axb:")
    for x in result:
        string = "| "
        for y in x:
            string += str(y)+" "
        string += "|"
        print(string)
         
    return result

print("Matrix with 4 rows 3 columns:\n")
print("[ [a,b,c] , [d,e,f] , [g,h,i] , [j,k,l] ]")
print("_       _")
print("| a b c |")
print("| d e f |")
print("| g h i |")
print("| j k l |")
print("‾       ‾")
