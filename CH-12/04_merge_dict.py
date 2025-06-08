dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
# Merging two dictionaries using the union operator (Python 3.9+)
merged_dict = dict1 | dict2

print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}