def unique_substring__lenghth(string):
    start = 0
    max_length = 0
    checked = set()

    for end in range(len(string)):
        
        while string[end] in checked:
            checked.remove(string[start])
            start += 1
        
        checked.add(string[end])
        
        max_length = max(max_length, end - start + 1)

    return max_length

print(unique_substring__lenghth("abcabcbb"))
