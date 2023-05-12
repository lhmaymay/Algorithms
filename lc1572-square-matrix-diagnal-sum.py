# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.




def dis(x):
    m=0
    if len(x)<=1:
        m=x[0]
    else:
        for i in range(len(x)):
            m+=x[i][i]+x[i][len(x)-i-1]
        if len(x)%2!=0:
            m-=x[len(x)//2][len(x)//2]
    return m
dis([[1,2,3],[4,5,6],[7,8,9]]), dis([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]), dis([5])

output: 25, 8, 5
