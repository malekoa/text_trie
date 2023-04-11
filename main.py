# Author: Malek Azadegan

import re
from typing import List
from nary_tree import n_node

# takes a body of text and returns a list of sentences
def get_sentences(text) -> List[str]:
    sentences = []
    # regex to match sentences
    pattern = re.compile(r'[^.!?]+[.!?]')
    # split text into sentences
    for sentence in pattern.findall(text):
        sentences.append(sentence)
    # remove leading and trailing whitespace
    sentences = [sentence.strip() for sentence in sentences]
    # convert sentences to lowercase
    sentences = [sentence.lower() for sentence in sentences]
    return sentences

# splits a sentence into words
def get_words(sentence) -> List[str]:
    words = []
    # regex to match words
    pattern = re.compile(r'\w+')
    # split sentence into words
    for word in pattern.findall(sentence):
        words.append(word)
    # remove leading and trailing whitespace
    words = [word.strip() for word in words]
    return words

# takes a tree root and a list of sentences which are lists of strings
def build_trie(root: n_node, sentences: List[List[str]]) -> None:
    # if sentences is empty, return 
    if len(sentences) == 0:
        return
    # if sentences is not empty, then get the set of first words of all sentences.
    first_words = set([sentence[0] for sentence in sentences])
    # create a dictionary to store the sentences that start with each first word
    first_word_sentences = {}
    # for each first word, create a list of sentences that start with that first word (excluding the first word) 
    print(f'sentences: {sentences}')
    for first_word in first_words:
        first_word_sentences[first_word] = [sentence[1:] for sentence in sentences if sentence[0] == first_word and len(sentence) > 1]
    # for each first word, add a child to the root with the first word as the value
    for first_word in first_words:
        root.add_child(first_word)
    # for each child of the root, recursively build a trie from the sentences that start with that first word
    for child in root.get_children():
        build_trie(child, first_word_sentences[child.get_val()])
    return root

# takes a body of text and returns a trie
def get_trie(text: str) -> n_node:
    # split text into sentences
    sentences = get_sentences(text)
    # split each sentence into words
    split_sentences = []
    for sentence in sentences:
        split_sentences.append(get_words(sentence))
    # add 'END' to the end of each sentence
    for sentence in split_sentences:
        sentence.append('ø')
    # create a tree root
    root = n_node('root')
    # build a trie from the split sentences
    build_trie(root, split_sentences)
    return root

if __name__ == '__main__':
    # lorem ipsum text
    lorem = "I woke up early this morning. After I woke up, I brushed my teeth. Then I went to the bathroom to wash my face. After washing my face, I got dressed for work. I had a quick breakfast before leaving the house. Then I walked to the train station to catch my train. I always take the same train to work every day. The train ride is usually about 30 minutes long. I like to read a book or listen to music during my commute. Once I arrive at the station, I walk to my office building. I work on the 6th floor of the building. My workday usually starts at 9am. I spend most of my day at my desk, working on my computer. Sometimes I have meetings with my colleagues. At lunchtime, I usually eat at the same cafe down the street. After work, I take the same train home and unwind for the evening."

    # get a trie from the lorem text
    trie = get_trie(lorem)

    # print the trie
    print(trie)