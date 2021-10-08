# Switch left and right side of sentence separated by '-'
# Application in developing an English language grammar packet for Albanian students

def switch():
    t = open("text-to-switch.txt", "r")
    ntf = open("new-text.txt", "w")
    nt = []
    for line in t:
        if "-" in line:
            nt.append(str.rstrip(line.split("-")
                    [1]) + " - " + line.split("-")[0] + "\n")

    for line in nt:
        ntf.write(line)
    ntf.close()

if __name__ == '__main__':
    switch()