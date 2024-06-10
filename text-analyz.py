import re

def analyze_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    words = text.split()
    word_count = len(words)

    char_count = len(text)

    sentences = re.split(r'[.!?]+', text)
    sentence_count = len(sentences)

    return word_count, char_count, sentence_count

file_path = 'text_file.txt'
word_count, char_count, sentence_count = analyze_text(file_path)

print(f"Word count: {word_count}")
print(f"Character count: {char_count}")
print(f"Sentence count: {sentence_count}")