from stats import get_num_words 
from stats import get_num_letters 
from stats import sort_letters 
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read() 


    path = sys.argv[1] 
    len(sys.argv) != 2 
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    count = get_num_words(text)

    char_counts = get_num_letters(text)
    

    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {filepath}...") 
    print("----------- Word Count ----------") 
    
    print(f"Found {count} total words") 

    sorted_chars = sort_letters(char_counts) 

    print("--------- Character Count -------") 
    for ch in sorted_chars: 
        if ch["char"].isalpha(): 
            print(f"{ch['char']}: {ch['num']}") 
    print("============= END ===============") 

print(sys.argv)

main() 



