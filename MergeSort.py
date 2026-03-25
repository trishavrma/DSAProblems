def merge(A,B):
    (c,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j < m+n:
        if i==m:
            c.append(B[j])
            j = j + 1
        elif j==n:
            c.append(A[i])
            i = i+1
        elif A[i]<=B[j]:
            c.append(A[i])
            i = i + 1
        elif A[i]>B[j]:
            c.append(B[j])
            j = j + 1
    return c