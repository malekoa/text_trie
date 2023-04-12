# Text Trie

Build a trie from a text file. Allows quick lookup of sentences in a text file. 

## Installation

```bash
pip install textrie
```

## Functionality

The `get_trie` function takes a string input which contains a body of text with sentences separated by common sentence-ending punctuation marks. It returns a trie in the form of an n-ary tree. The tree is built such that each branch in the tree is a sentence. The nodes along the branches are words in the sentence. The leaves of the tree are the end of the sentence. Each sentence from the body of text has a corresponding branch in the trie.

## Example

```python 
from textrie import get_trie

# create a trie from a text file
with open('text.txt', 'r') as f:
    text = f.read()
    trie = get_trie(text)

    # check if a sentence is present in the text
    sentence = 'This is a sentence.'
    trie.has(sentence) # returns a boolean
```

## Reason for existence

I wanted to make a script that made a finite state machine that would generate all and only the sentences in some body of text. A trie is a good data structure for this. Turns out it's also useful for searching for sentences in a body of text so I made it do that too.