def get_num_words(text):
    num_words = len(text.split())
    return num_words 

 
def get_num_letters(text):
    counts = {}
    for ch in text.lower():
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    return counts 

def sort_on(dict_item):
    return dict_item["num"]


def sort_letters(counts): 
    words = [] 
    for ch, num in counts.items(): 
        word = {"char": ch, "num": num} 
        words.append(word) 

    words.sort(reverse=True, key=sort_on) 
    return words

