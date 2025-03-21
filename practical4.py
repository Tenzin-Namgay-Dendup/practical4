def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


content = read_file('sample.txt')


def count_unique_words(content):
    words = content.split()
    unique_words = set(words)
    return len(unique_words)


def find_longest_word(content):
    words = content.split()
    longest_word = max(words, key=len)
    return longest_word


def count_word_occurrences(content, target_word):
    words = content.lower().split()
    target_word = target_word.lower()
    return words.count(target_word)


def calculate_percentage_longer_than_average(content):
    words = content.split()
    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)

    longer_words_count = sum(1 for word in words if len(word) > average_length)
    percentage = (longer_words_count / len(words)) * 100
    return percentage
        

if __name__ == "_main_":

    unique_word_count = count_unique_words(content)
    longest_word = find_longest_word(content)
    specific_word_count = count_word_occurrences(content, "is")
    percentage_longer_than_average = calculate_percentage_longer_than_average(
        content)

    print(f"Number of unique words: {unique_word_count}")
    print(f"Longest word: {longest_word}")
    print(f"Occurrences of the word 'is': {specific_word_count}")
    print(
        f"Percentage of words longer than average: {percentage_longer_than_average:.2f}%")

