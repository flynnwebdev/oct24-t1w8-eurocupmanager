import json

def load_matches(path):
    """
    Load matches from a JSON file

    parameters:
        path: Path to the JSON file

    return:
        List of matches or an empty list if an error occurs
    """
    try:
        with open(path) as file:
            matches = json.load(file)

        return matches
    except FileNotFoundError:
        print(f'Error: The file "{path}" does not exist!')
        return []
    except json.decoder.JSONDecodeError:
        print(f'Error: The file "{path}" is not valid JSON!')
    except Exception as e:
        print(f'An unexpected error occured: {e}')
        return []


def save_matches(path, matches_list):
    try:
        with open(path, 'w') as file:
            json.dump(matches_list, file, indent=4)

        print(f'Matches successfully saved to {path}')
    except PermissionError:
        print(f'Error: Permission denied to write to {path}')
    except Exception as e:
        print(f'An unexpected error occured: {e}')
