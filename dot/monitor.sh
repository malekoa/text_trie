#!/bin/bash

# Set the path to the dot command
DOT="/usr/local/bin/dot"

# Watch for changes to the get_trie.gv file
fswatch -o get_trie.gv | while read file; do
    # Execute the dot command to generate the SVG file
    dot -Tsvg get_trie.gv -o get_trie.svg
done