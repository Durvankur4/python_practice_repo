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
# import string

# PUNCT = string.punctuation

# def url_slug(url_text : str)-> str:
#     url = []
#     table = str.maketrans("","",string.punctuation)
#     url = url_text.translate(table)
#     return "-".join(url.lower().split())

# print(url_slug("stjisg ao!jd  Sk ??? aa"));


# Simplified Problem — Replace {{key}} with UPPERCASE Key
# Write a function:
# def shout_keys(template: str) -> str:
# It should find all occurrences of {{something}} and replace them with the UPPERCASE version of the text inside the braces.
# Example:
# "Hello {{name}}, welcome to {{place}}!"
# → "Hello NAME, welcome to PLACE!"
# Rules (much simpler than the real Problem 3):
# Don’t worry about missing keys or lookup tables.
# Don’t evaluate or fetch anything — just uppercase the inner text.
# Token format: {{ key }} or {{key}} or even {{ key }} → all valid.
# Key must be alphabetic only (letters a-z).

# def shout_keys(template: str) -> str:
#     out = []
#     i = 0
#     n = len(template)

#     while i < n:
#         # Detect {{
#         if i+1 < n and template[i] == "{" and template[i+1] == "{" :
#             i += 2
#             start = i
#             inner = []

#             while i+1 < n and not (template[i] == "}" and template[i+1] == "}"):
#                 i+= 1
            
#             inner = template[start:i].strip()
#             out.append(inner.upper())
#             i+=2
            
            
#         else:
#             out.append(template[i])
#             i+=1

#     return "".join(out)
# print(shout_keys("apple {{apple}} apple {{banaan}}"))



# Problem 3 (Hard) — simple template replacer (mini templating)
# Implement render_template(template: str, context: dict) -> str that replaces {{key}} tokens with # str(context[key]). 
# Should:
# Replace multiple tokens
# Leave tokens unchanged if key missing (or provide optional default argument)
# Avoid catastrophic repeated replacements (don't call .replace repeatedly over the whole string if unnecessary)
 
# def render_template(template: str, context: dict) -> str :  
#     i=0 
#     out =[]
#     n= len(template)
#     while i < n:
        
#         if i+1<n and template[i]=="{" and template[i+1]== "{" :
#             i+=2
#             start = i
            
            
#             while i+1<n and not( template[i]=="}" and template[i+1]== "}") :
#                 i+=1
            
#             key = template[start:i]
#             out.append(context.get(key))
#             i+=2

#         else:
#             out.append(template[i])
#             i+=1

#     print(context,out)
#     return "".join(out)



# print(render_template("apple : {{1}} , banana : {{2}} , 50Rs : {{50Rs}}",{"1":"50Rs","2":"100Rs","50Rs" : "Cucumber"}))