dict = {} #do not remove, used for initialise_dict()

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    initialise_dict(text)
    charCount(text)
    processed_dict = process_dict()
    processed_dict.sort(reverse=True, key=call_value)
    #key is callable object, inserts each item in process_dict
    #iterating through each item through the list
    #due to sort, then list is arranged according to values from call_value()
    
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount(text)} words found in the document")
    print("")
    for dictionary in processed_dict:
        name = dictionary["name"]
        num = dictionary["num"]
        if name.isalpha():
            print(f"The '{name}' character was found {num} times")
    print("")
    print("--- End Report ---")





def process_dict():
    list_dict = []
    for i in dict:
        temp_dict = {"name":i, "num":dict[i]}
        list_dict.append(temp_dict)
    return list_dict

def call_value(dict):
    return dict["num"]

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