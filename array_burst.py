

def solve(A, burst_len):
    stack = [A[0]]
    temp = []
    i = 1
    while i < len(A):
        if stack and A[i] == stack[-1]:
            ele = stack[-1]
            temp = []
            while stack and stack[-1] == ele:
                temp.append(stack.pop())
            while i < len(A) and A[i] == ele:
                temp.append(A[i])
                i += 1
            if len(temp) < burst_len:
                stack.extend(temp)
        else:
            stack.append(A[i])
            i += 1
    return stack

print(solve(list('aaaaa'), 3))

        
