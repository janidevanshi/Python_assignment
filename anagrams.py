# taking input as strs
strs = input()
# empty dictionary used for storing an output
dict_anagram = {}

for i in strs.split():
    unique_anagram = str(''.join(sorted(i)))
    # checking value if it is present in the dictionary or not
    if unique_anagram not in dict_anagram:
        dict_anagram.update({unique_anagram: [i]})
    # if not then appending that value
    else:
        dict_anagram[unique_anagram].append(i)

Output = sorted(list((dict_anagram.values())))
print("Output: ", Output)
