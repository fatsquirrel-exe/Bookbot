dict = {} #do not remove, used for initialise_dict()

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(f"Num of words: {wordcount(text)}")
    initialise_dict(text)
    print(charCount(text))

def get_text(book_path):
    with open(book_path) as f:
        return f.read()
def wordcount(words):
    count = 0
    for word in words.split():
        count += 1
    return count

def charCount(text):
    for words in text.split():
        for word in words:
            lowered = word.lower()
            dict[lowered] += 1
    return dict
    
            
def initialise_dict(text):   #get all possible char, add key and value pair
    characters = set()
    for word in text.split():
        for char in word:
            lowered = char.lower()
            characters.add(lowered)
    for i in characters:
        dict[i] = 0
    return dict

main()