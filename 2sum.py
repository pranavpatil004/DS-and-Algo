final_substring = ''
length = 0
final_length = 0
start_i, i = 0, 0
s = "bbbb"
k = len(s)
while i < k:
    if(final_substring.find(s[i]) == -1):
        final_substring += s[i]
        length = len(final_substring)
        i+=1
    else:
        i = start_i + 1
        start_i = i
        final_substring = ''
        if(final_length < length and length != 0):
            final_length = length
            
if(final_length < length):
    final_length = length
print(final_length)