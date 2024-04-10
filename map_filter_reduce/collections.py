from collections import defaultdict

def group_anagrams(str_list):
    anagrams = defaultdict(lambda: "Not Present")
    for str in str_list:
        str_sorted = ''.join(sorted(str))

        if str_sorted in anagrams:
            anagrams[str_sorted].append(str)
        else:
            anagrams[str_sorted] = [str]
    return list(anagrams.values())


strs = ["rat", "tar", "chin", "thing", "inch", "night"]
print(group_anagrams(strs))