def main():
    livro = 'books/frankenstein.txt'
    text = read_file(livro)
    palavras = count_words(text)
    caracteres = count_characters(text)
    caracteres_ordenados = dict_to_ordered_list(caracteres)

    print(f"--- Begin report of {livro} ---")
    print(f"{palavras} words found in the document")
 
    for char in caracteres_ordenados:
        if not char["char"].isalpha():
            continue
            
        print(f"The '{char['char']}' character was found {char['num']} times")
    print(f"--- End report ---")


def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(file):
    words = file.split()
    return len(words)

def count_characters(file):
    characters = {}
    string = file.lower()
    for char in string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(item):
    return item["num"]

def dict_to_ordered_list(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char": ch, "num": dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()