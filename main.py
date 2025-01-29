# def main func
def main():
    # set book path variable
    book_path = "books/frankenstein.txt"
    # set text variable using text func
    text = get_book_text(book_path)
    # variable to store count of words from count func
    num_words = get_num_words(text)
    # variable to store counts per letter
    char_counts = get_count_chars(text)
    # variable for list of ordered char/count dicts
    sorted_counts = order_char_counts(char_counts)
    # print total word count stmts
    print(f"{num_words} found in the document\n")
    # loop through sorted counts for final print stmts
    for char in sorted_counts:
        print(f"The '{char['char']}' character was found '{char['count']}' times")

# func splits text file into individual words, then counts length
def get_num_words(text):
    words = text.split()
    return len(words)

# func opens .txt file and saves it to variable
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
# func to get dict of count per character
def get_count_chars(text):
    #empty dict to hold letter counts
    letter_counts = {}
    #conver string to all lower case
    lower_string = text.lower()

    for l in lower_string:
        ## METHOD 2 (GK with setdefault funct)
        letter_counts[l] = letter_counts.setdefault(l, 0) + 1
    else:
        letter_counts[l] += 1

    return letter_counts

    ## METHOD 1 - more basic method 
    #     if l in letter_counts:
    #         letter_counts[l] += 1
    #     else:
    #         letter_counts[l] = 1
    # return letter_counts

def order_char_counts(counts):
    # filter out special chars
    filtered_chars = {k: v for k, v in counts.items() if k.isalpha()}
    # split dict into list of dicts per char
    listed_dicts = [{'char':key, 'count':value} for key, value in filtered_chars.items()]
    # sort list of dicts 
    sorted_list = sorted(listed_dicts, key = lambda x: x['char'])
    
    return sorted_list


main()

