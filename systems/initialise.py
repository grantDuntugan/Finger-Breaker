from english_words import english_words_lower_alpha_set

def create_wordlib(num_words):
    my_set = []
    counter = 0
    for val in english_words_lower_alpha_set:
        my_set.append(val)
        counter += 1
        if (counter > num_words):
            break
    return my_set