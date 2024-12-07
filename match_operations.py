def display_matches(matches):
    try:
        for m in matches:
            print(f'{m['Date']}: {m['Team A']} {m['Score A']} - {m['Score B']} {m['Team B']}')
    except KeyError as e:
        print(f'Error displaying matches: Missing key {e}')

