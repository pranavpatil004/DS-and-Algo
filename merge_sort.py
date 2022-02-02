def merge_sort(A):
    mid = len(A)//2
    print('A in main: ', A)
    return A if len(A) == 1 else merge(merge_sort(A[0:mid]),merge_sort(A[mid:len(A)]))

def merge(A,B):
    print('A=', A, 'B=', B)
    merged = []
    i,j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    if i == len(A):
        merged.extend(B[j:])
    if j == len(B):
        merged.extend(A[i:])
    print(merged)
    return merged

print(merge_sort([1,3,2,4,5,7,6]))