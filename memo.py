def make_list(str):
    string = []
    num = int(len(str))
    for a in range(num):
        string.append(str[a])
    return string
    
print(make_list("abcd"))