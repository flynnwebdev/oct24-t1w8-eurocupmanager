from file_operations import load_matches, save_matches

spam = load_matches('matches.json')
spam[0]['Score A'] = 3
save_matches('debug.json', spam)
