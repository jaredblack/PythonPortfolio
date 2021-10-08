# For a given member list pulled from LCR (lcr.churchofjesuschrist.org)
# Formats phone numbers into a consistent format, designed specifically for Albanian phone numbers
# Input: uf.txt
# Output: f.txt

import re


def format():
    uf = open("uf.txt", "r")
    f = open("f.txt", "w")

    for num in uf:
        if len(num) < 5:
            num = "\n"
            print("here")
        else:
            print(len(num))
            if not num.isnumeric():
                num = re.sub("[^0-9]", "", num)
            if num[0] == "0":
                num = num[0:3] + " " + num[3:6] + " " + num[6:]
            if num[0] == "6" or num[0] == "5":
                num = "0" + num[0:2] + " " + num[2:5] + " " + num[5:] + "\n"
            elif num[0] == "3":
                num = "0" + num[3:5] + " " + num[5:8] + " " + num[8:] + "\n"
            else:
                num = num + "\n"
        f.write(num)

    f.close()

if __name__ == '__main__':
    format()
