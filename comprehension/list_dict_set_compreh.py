## fliters string of length greater than 5
strings = ["Prabin", "Fusemachines", "axe", "apple", 'ant']
filtered_str = [item for item in strings if len(item)>5]
print(filtered_str)

#multiply two list
int_list1 = [5, 4, 6, 7, 1]
int_list2 = [2, 3, 7, 2, 9]
product_list = [x* y for x,y in zip(int_list1, int_list2)]
print(product_list)

int_list3 = [-5, -8,-10,-9,-6]
sum_list = [(x,y,z) for x in int_list1 for y in int_list2 for z in int_list3 if x+y+z == 0]
print(sum_list)


#### dictionary comprehenssion:
keys= ["name", "age", "place","weight"]
values = ["Prabin", 24, "Kathmandu", 72]
made_dict = {keys: values for keys, values in zip(keys, values)}
print(made_dict)

marks_dict = {"Prabin":90, "Raju":52, "Sajjan":86, "Arjun":59, "John": 95}
filtered_dict = {k:v for k,v in marks_dict.items() if v>80}
print(filtered_dict)

ascii_dict = {chr(index): index for index in range(ord("a"), ord("z") + 1)}
print(ascii_dict)


## Set comprehenssion:
list4 = [1, 5, 8, 9, 4, 5, 8]
set4 = {x for x in list4}
print("Unique set elements :\n", set4)

word_list = ["vector", "embedding", "attention", "bert"]
unique_char_word = {chr for word in word_list for chr in word}
print(unique_char_word)

string1 = "vectors"
string2= "embeddings"
common_both = {chr1 for chr1 in string1 for chr2 in string2 if chr1 == chr2}
print(common_both)
