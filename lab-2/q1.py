def count_words(sentence):

    word_count = {}
    words = sentence.split()

    for word in words:

        word = word.strip(".,!?\"'()[]{}:;")

        if word in word_count:

            word_count[word] += 1
        else:

            word_count[word] = 1

    return word_count


sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print("Word count in the sentence:")
c = 0
for word, count in word_count.items():
    c += count
    print(f"{word}: {count}")

print("total words :", c)
