import textwrap
def wrap_lines(filename, width):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        wrapped_lines = []
        for line in lines:
            wrapped = textwrap.fill(line, width, subsequent_indent=' ', break_long_words=False)
            wrapped_lines.append(wrapped)

        with open(filename, 'w') as file:
            file.writelines(wrapped_lines)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    width = int(input("Enter the width for line wrapping: "))

    wrap_lines(filename, width)
    print(f"Lines in '{filename}' have been wrapped at width {width}.")
