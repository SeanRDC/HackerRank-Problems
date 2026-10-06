# Subclasses HTMLParser so that every start tag and empty tag prints its name followed
# by each attribute and value, while end tags are ignored.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def print_elements(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_starttag(self, tag, attrs):
        self.print_elements(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self.print_elements(tag, attrs)

    def handle_endtag(self, tag):
        pass

m = MyHTMLParser()
user_input = "".join([input() for _ in range(int(input()))])
m.feed(user_input)