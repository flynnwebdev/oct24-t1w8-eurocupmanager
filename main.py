from file_operations import load_matches, save_matches
from match_operations import display_matches

spam = load_matches('matches.json')
display_matches(spam)

