import re

def main():
    inputFile = openFile()
    lines = readLines(inputFile)
    num = 0;

    for line in lines:
        # extract digits from the line into a list
        digits = re.findall(r'\d', line)
        length = len(digits)
        
        if (length < 1):
            continue
        elif (length == 1):
            num += int(digits[0] + digits[0])
        else:
            num += int(digits[0] + digits[length - 1])

    print(num);
    closeFile(inputFile)

def openFile():
    return open('input.txt')

def readLines(file):
    fileLines = [];
    for line in file:
        fileLines.append(line.replace('\n', ''));
    return fileLines;

def closeFile(file):
    file.close()

main()