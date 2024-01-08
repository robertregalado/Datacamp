"""
Now, you want to perform some visualizations with your sentiment_analysis dataset. You are interested in the words surrounding python. You want to count how many times a specific word appears right before and after it.

Positive lookahead (?=) makes sure that first part of the expression is followed by the lookahead expression. Positive lookbehind (?<=) returns all matches that are preceded by the specified pattern.

The variable sentiment_analysis, containing the text of one tweet, and the re module are loaded in your session. You can use print() to view the data in the IPython Shell."""

import re 

# Positive lookahead
sentiment_analysis = 'You need excellent python skills to be a data scientist. Must be! Excellent python'

look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print("look_ahead: ", look_ahead)

"""
Get all the words that are preceded by the word python or Python in sentiment_analysis. Print out the words found.
"""

# Positive lookbehind

look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)

# Print out
print("look_behind: ", look_behind)