import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    print(f'File name: {file}')
    with open(file) as open_file:
        read_file = open_file.read()

    # Removing punctuation
    file_without_punctuation = read_file.translate(str.maketrans('', '', string.punctuation))

    # Lowercasing all characters
    file_lowercased = file_without_punctuation.lower()

    # Split long string into list of strings (where every index is a word)
    file_split_into_list = str.split(file_lowercased)

    # Removing STOP_WORDS from the file
    file_scrubbed = [word for word in file_split_into_list if word not in STOP_WORDS]

    # Fill dictionary with word counts
    word_count = {}
    for word in file_scrubbed:
        if word_count.get(word) == None:
            word_count[word] = 1
        else:
            word_count[word] += 1

    # Sorting
    sorted_list = sorted(word_count.items(), key=lambda x:x[1], reverse = True)

    #Printing
    for word in sorted_list:
        print(f'{" " * (20 - len(word[0]))} {word[0]} | {word[1]} {"*" * word[1]}')
    
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)