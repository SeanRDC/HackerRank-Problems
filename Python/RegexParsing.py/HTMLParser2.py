# Subclasses HTMLParser to print every comment, labelled single-line or multi-line, and
# every piece of data that is not just a newline.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data == "\n":
            pass
        else:
            print(f">>> Data\n{data}")

    def handle_comment(self, data):
        if "\n" in data:
            print(f">>> Multi-line Comment\n{data}")
        else:
            print(f">>> Single-line Comment\n{data}")

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()