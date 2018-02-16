# returns list of list of string
def group_anagrams(input_array):
    has_dict = {}
    for word in input_array:
        chars = list(word) # ['e', 'a', 't']
        chars.sort() # ['a', 'e', 't'] #"aet"
        hash_id = "".join(chars)
        if hash_id in has_dict:
            has_dict[hash_id].append(word)
        else:
            has_dict[hash_id] = [word]
    group = []
    for key in has_dict:
        group.append(has_dict[key])
    return group


print(group_anagrams(["eat", "ate", "fa"]))