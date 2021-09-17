import csv

def Clean(row):
    content = str(row)
    for char in badchars:
        content = content.replace(char, "")
    print(content)


badchars = ["(", ")", "-", " ", "[", "]", "'", "ï»¿",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]


with open('passthis.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        Clean(row)
        line_count += 1
    print(f'Processed {line_count} lines.')

