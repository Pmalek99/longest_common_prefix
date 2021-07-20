input_list = ["flower","flow","flight"]
input_list = ["dog","racecar","car"]
add_list = ["a","b","c"]
add = 0
strr = "dog"
theSame = True
letter = 0
prefix = ""
while(1):
    for ind,word in enumerate(input_list):
        input_list[ind] = word + add_list[add]
        add +=1
        add = add%3
    break





while(theSame):
    x = input_list[0][letter]
    for word in input_list:
        if word[letter] != x:
            theSame = False
            break
    if theSame == True:
        prefix = prefix + x


    letter +=1

print(prefix)
