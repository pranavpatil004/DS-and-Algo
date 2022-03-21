def merge_sort(A):
    array_size = 1
    while array_size < len(A):
        for i in range(0, len(A), array_size*2):
            if i+(array_size*2) < len(A):
                A[i:i+array_size*2] = merge(A[i:i+array_size], A[i+array_size:i+array_size*2])
            else:
               A[i:] = merge(A[i:i+array_size], A[i+array_size:])
        array_size = array_size*2
    return A
    

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

print(merge_sort([4,5,6,3,1,5,7,4]))