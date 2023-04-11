from typing import List

from main import get_words

class n_node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, val):
        self.children.append(n_node(val))

    def get_children(self):
        return self.children

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    # checks if a given sequence of words is in the trie starting at the current node
    def contains_words(self, words: List[str]) -> bool:
        # if there are no more words to check, return True
        if len(words) == 0:
            return True
        # if there are more words to check, check if the current node has a child with the first word as the value
        for child in self.children:
            if child.val == words[0]:
                # if the current node has a child with the first word as the value, recursively check if the child contains the rest of the words
                return child.contains(words[1:])
        # if the current node does not have a child with the first word as the value, return False
        return False

    # checks if a given sentence is in the trie starting at the current node
    def contains_sentence(self, sentence: str) -> bool:
        # check if the current node contains the words
        return self.contains_words(get_words(sentence))

    def __str__(self):
        return str(f'[{self.val} {", ".join([str(child) for child in self.children])}]')