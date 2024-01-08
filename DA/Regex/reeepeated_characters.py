"""
Reeepeated characters
Back to your sentiment analysis! Your next task is to replace elongated words that appear in the tweets. We define an elongated word as a word that contains a repeating character twice or more times. e.g. "Awesoooome".

Replacing those words is very important since a classifier will treat them as a different term from the source words lowering their frequency.

To find them, you will use capturing groups and reference them back using numbers. E.g \4.

If you want to find a match for Awesoooome. You first need to capture Awes. Then, match o and reference the same character back, and then, me.

The list sentiment_analysis, containing the text of three tweets, and the re module are loaded in your session. You can use print() to view the data in the IPython Shell.
"""

import re 

sentiment_analysis = ['@marykatherine_q i know! I heard it this morning and wondered the same thing. Moscooooooow is so behind the times',
 'Staying at a friends house...neighborrrrrrrs are so loud-having a party',
 'Just woke up an already have read some e-mail']
 
# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"


for tweet in sentiment_analysis:
	# Find if there is a match in each tweet 
	match_elongated = re.search(regex_elongated, tweet)
    
	if match_elongated:
		# Assign the captured group zero 
		elongated_word = match_elongated.group(0)
        
		# Complete the format method to print the word
		print("Elongated word found: {word}".format(word=elongated_word))
	else:
		print("No elongated word found") 