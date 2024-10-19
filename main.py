def main():
    path = "books/frankenstein.txt"
    file_contents = fetch_book_content(path)
    no = count_words(file_contents)
    char_dict = count_characters(file_contents)
    print_report(no,char_dict,path)


def fetch_book_content(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    d={}
    s=set("abcdefghijklmnopqrstuvwxyz")
    for i in lower_text:
        if i in s:
            d[i] = d.get(i,0) + 1
    return d

def print_report(n,d,path):
    li = list(d.items())
    li.sort(reverse = True, key = lambda x : x[1])
    print("--- Begin report of", path, "---")
    print(n, "words found in the document")
    for i in li:
        print("The '", i[0], "' character was found", i[1], "times")

    print("--- End report ---")



main()
