example_dictionary = {
    "키A" : "키A",
    "키B" : "키B",
    "키C" : "키C"
    }

print("# 딕셔너리의 items() 함수")
print("item():", example_dictionary.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")
for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key,element))
    
