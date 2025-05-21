lst = (1,2,3,6,(8,895,'7'),3,2,89)

for item in lst:
    if type(item) == tuple:
        for subitem in item:
            print(subitem)
    else:
        print(item)
        


string = "Happy Birthday Dylan"

# print(len(string))
# print(string[20])

# print(string[15:])
# words = string.split()

# print(words[1])