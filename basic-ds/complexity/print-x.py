N=int(input())

for i in range(1,N+1):
    row=""
    for j in range(1,N+1):
        if i==j and i+j==N+1:
            row+="X"
        elif i==j:
            row+="\\"
        elif i+j==N+1:
            row+="/"
        else:
            row+=" "
    print(row)