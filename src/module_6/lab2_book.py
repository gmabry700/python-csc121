def main():
    with open("alice.txt", "r") as file:
        contents = file.readlines()     # returns individual lines as a list

    # get chapter 1 and write it to a new file
    chapter1 = contents[52:272]
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)

main()