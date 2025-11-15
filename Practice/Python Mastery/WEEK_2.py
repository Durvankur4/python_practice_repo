# Problem 1 (Easy) — unique_sorted_words(text)
# Return a list of unique words from text, normalized to lowercase, punctuation removed, sorted alphabetically.


# import string
# PUNCT = string.punctuation

# def unique_sorted_words(text : str) -> list[str] :
#     words = []
    
#     for word in text.split() :
#         words.append(word.strip(PUNCT).lower())

#     unique = {w for w in words if w} #add w (for every w in words_list if it is truthy ie it exixt add w to unique)
#     #this make sure no "" gets added 
#     return sorted(unique)
    

# print(unique_sorted_words("unique_sorted_words apple aplle mabanfan aaa. agad! !!"))



# Problem 2 (Medium) — slugify(text)
# Create a URL slug from text: lowercase, replace whitespace with -, remove punctuation, collapse multiple -, 
# trim leading/trailing hyphens.
# import re
import string

PUNCT = string.punctuation

def url_slug(url_text : str)-> str:
    url = []
    table = str.maketrans("","",string.punctuation)
    url = url_text.translate(table)
    return "-".join(url.lower().split())

print(url_slug("stjisg ao!jd  Sk ??? aa"));

# Problem 3 (Hard) — simple template replacer (mini templating)
# Implement render_template(template: str, context: dict) -> str that replaces {{key}} tokens with # str(context[key]). 
# Should:
# Replace multiple tokens
# Leave tokens unchanged if key missing (or provide optional default argument)
# Avoid catastrophic repeated replacements (don't call .replace repeatedly over the whole string if unnecessary)