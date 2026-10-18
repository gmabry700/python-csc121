def main():
    with open("alice.txt", "r") as file:
        contents = file.readlines()     # returns individual lines as a list

    # get chapter 1 and write it to a new file
    chapter1 = contents[52:272]
    # print(contents)
    # print(chapter1)
    with open("chapter1.txt", "w") as f:
        # f.write("Chapter I.")
        f.writelines(chapter1)

main()