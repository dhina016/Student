def rotLeft(a, d):
    return a[d:] + a[:d]
fptr = open(os.environ['OUTPUT_PATH'], 'w')
result = rotLeft(a, d)
 
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
 
    fptr.close()

        
    
