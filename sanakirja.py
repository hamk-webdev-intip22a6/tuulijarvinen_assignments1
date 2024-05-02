import json
import os


def load_dictionary(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: Unable to decode JSON file.")
        return {}

def save_dictionary(dictionary, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(dictionary, file, indent=4)
    except IOError:
        print("Error: Unable to save dictionary.")


def main():
    file_name = "dictionary.json"
    dictionary = load_dictionary(file_name)

    while True:
        
        word = input("Enter a word to search (or press Enter to exit): ").strip().lower()

        if not word:
            print("Exiting the application.")
            break

        translation = dictionary.get(word)
        if translation:
            print(f"Translation: {translation}")
        else:
            definition = input("Word not found. Please input a definition: ").strip()
            if definition:
                dictionary[word] = definition
                print("Word added to dictionary.")

    save_dictionary(dictionary, file_name)
    default_dictionary = {
        "koira": "dog",
        "kissa": "cat",
        "maito": "milk",
        "kahvi": "coffee",
        "suklaa": "chocolate"
     }

if __name__ == "__main__":
    main()
