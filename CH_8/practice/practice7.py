def rem(l, word):
    new_list = []
    for item in l:
        if item != word:
            new_list.append(item)
    return new_list

l = ["Aditya", "Raj", "Raju", "Rajesh", "Rajeshwari"]

print(rem(l, "Aditya"))