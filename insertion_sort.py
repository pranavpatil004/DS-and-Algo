def insersion_sort(A):
    for i in range(len(A)):
        temp = A[i]
        for j in reversed(range(0,i)):
            pos = -1
            if A[j] > temp:
                pos = j
            if pos != -1:
                A.remove(temp)
                A.insert(j, temp)
        print(A)
    return A

print(insersion_sort([9,8,7,6,5,4,3,2,1]))