
from urllib.request import urlopen
from urllib.error import URLError
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

def load_url(url):
    if not url:
        raise ValueError("URL cannot be empty")
    
    try:
        response = urlopen(url)
        content = response.read().decode('utf-8')
        return content
    except (URLError, UnicodeDecodeError):
        return None

def count_dangerous_words(text):
    dangerous_words = ["bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism"]
    count = 0
    for word in dangerous_words:
        count += text.lower().count(word)
    return count

def main():
    url = input("Give me a valid URL to download: ")
    content = load_url(url)
    if content:
        num_dangerous_words = count_dangerous_words(content)
        print("Number of dangerous words:", num_dangerous_words)
        path = input("Give me a valid path to save the contents: ")
        if path:
            save_content(content, path)
        else:
            print("Path cannot be empty.")
    else:
        print("non-text content or error loading URL")

def save_content(content, path):
    try:
        with open(path, 'w') as file:
            file.write(content)
        print("Saving succeeded to:", path)
    except Exception as e:
        print("Saving failed:", e)

if __name__ == "__main__":
    main()
