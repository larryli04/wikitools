from re import L
from traceback import print_list
import wikipedia
from bs4 import BeautifulSoup

from noParentheses import noParentheses

# wikipedia.random(# of pages)
#Clicking on the first non-parenthesized, non-italicized link

def getFirstLink(start):
    page = wikipedia.WikipediaPage(start)
    
    soup = BeautifulSoup(page.html(), 'html.parser') # create soup object

    text = str(soup.select_one("div > p > a[href]").parent) # first block of paragraph text
    p = noParentheses(text) # take out parenthetical block

    l = p.index("title=") # find first link

    linkName = ""
    quote = False
    i = l+7
    while(quote == False): # get the page title of link
        char = p[i]
        linkName += char
        
        if(p[i+1] == '"'):
            quote = True
        i+=1

        
    return linkName

def printPath(list):
    out = ""
    for i in range(len(list)-1):
        out += list[i] + "->"
    
    out += list[-1]
    return out



if __name__ == "__main__":
    
    current = input()
    path = [current]
    path.append(getFirstLink(current))

    while(getFirstLink(current) != "Philosophy"):
        current = getFirstLink(current)
        path.append(getFirstLink(current))
        print(printPath(path))
    print(printPath(path))
