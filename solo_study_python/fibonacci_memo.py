def flatten(data):
    for i in data:
        if type(i) == int:
            return
        else:
            result = i, flatten

def flatten(data):
    ouput = []
    for item in data:
        print(item)
        if type(item) == list:
            output = output + flatten(item)
        else:
            output.append(item)
            
    return output

        
example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))
