# Problem 1 (Easy) — unique_sorted_words(text)
# Return a list of unique words from text, normalized to lowercase, punctuation removed, sorted alphabetically.

# Problem 2 (Medium) — slugify(text)
# Create a URL slug from text: lowercase, replace whitespace with -, remove punctuation, collapse multiple -, 
# trim leading/trailing hyphens.

# Problem 3 (Hard) — simple template replacer (mini templating)
# Implement render_template(template: str, context: dict) -> str that replaces {{key}} tokens with # str(context[key]). 
# Should:
# Replace multiple tokens
# Leave tokens unchanged if key missing (or provide optional default argument)
# Avoid catastrophic repeated replacements (don't call .replace repeatedly over the whole string if unnecessary)