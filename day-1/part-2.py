import re

def main():
    inputFile = openFile()
    lines = readLines(inputFile)
    num = 0;
    number_strings = dict(one = "1", two = "2", three = "3", four = "4", five = "5", six = "6", seven = "7", eight = "8", nine = "9");

    for line in lines:
        regex = re.compile(r'.*?(\d|one|two|three|four|five|six|seven|eight|nine)(?:.*(\d|one|two|three|four|five|six|seven|eight|nine))?')
        # extract digits from the line into a list
        digits = regex.findall(line)
        first_digit = number_strings.get(digits[0][0], digits[0][0])
        second_digit = number_strings.get(digits[-1][1], digits[-1][1])
        
        if (len(second_digit) < 1):
            second_digit = first_digit
        num += int(first_digit + second_digit)

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