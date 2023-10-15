def create_file(filename):
    lines = [
        "This is the first line.",
        "Here comes the second line.",
        "Line number three right here.",
        "Fourth line is about to start.",
        "We're at the fifth line now.",
        "Number six has arrived.",
        "Seventh line is on its way.",
        "Finally, the eighth line!"
    ]

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')


def process_file(filename):
    line_lengths = {}
    letter_frequencies = {}

    with open("sample.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):

            line_lengths[i] = len(line.strip())

            for char in line:
                if char.isalpha():
                    char = char.lower()
                    if char in letter_frequencies:
                        letter_frequencies[char] += 1
                    else:
                        letter_frequencies[char] = 1
    print("Dictionary 1 - Line Numbers and Total Lengths:")
    print(line_lengths)

    print("\nDictionary 2 - Letter Frequencies:")
    print(letter_frequencies)


filename = 'sample.txt'
create_file(filename)
process_file(filename)
