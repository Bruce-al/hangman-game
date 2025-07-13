# Author: MBM
# Important Dates: 22/06/23, Mj, Md, 28/02/06, 01/03/04, 30/06/66, 21/06/67

import random
words = ['python', 'java', 'hangman']
word = random.choice(words)
guess = '_' * len(word)
print('Guess the word:', guess)