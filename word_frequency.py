import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

STOP_PUNCTUATION = [
    '.', ',', '/', ';', '[', ']', '`', '-', '=', '<', '>', '?', ':', '"', '{', '}', 
    '|', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'
]


def print_word_freq(file):
    print(f'File name: {file}')
    with open(file) as open_file:
        read_file = open_file.read()
        # print(f'read_file:\n{read_file})

    # Removing punctuation
    file_without_punctuation = read_file.translate(str.maketrans('', '', string.punctuation))
    # print(f'file_without_punctuation:\n{file_without_punctuation}')

    # Lowercasing all characters
    file_lowercased = file_without_punctuation.lower()
    # print(f'file_lowercased:\n{file_lowercased}')

    # Split long string into list of strings (where every index is a word)
    file_split_into_list = str.split(file_lowercased)
    # print(f'file_split_into_list:\n{file_split_into_list}')
    # print(f'file_split_into_list is type:{type(file_split_into_list)}')

    # Removing STOP_WORDS from the file
    file_scrubbed = [word for word in file_split_into_list if word not in STOP_WORDS]
    print(f'file_scrubbed:\n{file_scrubbed}')

    # Fill dictionary with word counts
    word_count = {}
    

    



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