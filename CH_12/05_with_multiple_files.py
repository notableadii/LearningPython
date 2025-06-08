with(
    open("CH-12/05_with_multiple_files.py", "r") as file1,
    open("CH-12/04_merge_dict.py", "r") as file2
):
    content1 = file1.read()
    content2 = file2.read()
    print("Content of file1:\n")
    print(content1)
    print("\nContent of file2:\n")
    print(content2)