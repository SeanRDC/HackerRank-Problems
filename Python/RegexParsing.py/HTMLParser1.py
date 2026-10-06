# Subclasses HTMLParser to print 'Start', 'End', or 'Empty' for each tag it meets,
# together with the tag's attributes and values.

from html.parser import HTMLParser

class HackerRank(HTMLParser):
    def handle_starttag(self, start_tag, attrs):
        print(f"Start : {start_tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_endtag(self, end_tag):
        print(f"End   : {end_tag}")

    def handle_startendtag(self, setag, attrs):
        print(f"Empty : {setag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

hacker = HackerRank()
user_input = "".join([input() for _ in range(int(input()))])

hacker.feed(user_input)