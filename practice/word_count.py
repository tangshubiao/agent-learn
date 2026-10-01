text = "the cat and the dog and the bird"

def word_count(text):
    words = text.split()
    result = {}
    for w in words:
        if w in result:
            result[w] = result[w] + 1
        else:
            result[w] = 1
    return result


print(word_count("the cat"))

print(word_count(text))