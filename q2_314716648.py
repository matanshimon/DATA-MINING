def revword(word: str) -> str:
    return word[::-1].lower()

def countword():
    str= open("text.txt", "r")
    my_count = 0
    for line in str:
        list_words = line.split(" ")
        if len(list_words) == 1:
            first_word = list_words[0].lower().strip()
        else:
            for x in list_words:
                word = revword(x).strip()
                if word == first_word:
                    my_count += 1
    print(my_count)


