word = "Donkey"

with open("CH-9/practice/file.txt", "r") as f:
  content = f.read()

content_new = content.replace(word, "######")

with open("CH-9/practice/file.txt", "w") as f:
    f.write(content_new)