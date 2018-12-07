import re


# badchars = re.compile(r"[\d\-.]*")
badchars = "0123456789-&/'."

with open("words.txt", "r") as file:
    with open("newwords.txt", "w") as newfile:
        for line in file:
            for character in line:
                if character in badchars:
                    break
            else:
                newfile.write(line)

