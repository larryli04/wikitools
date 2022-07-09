from types import NoneType
from lxml import etree
from pprint import pprint
import json
from noParentheses import flink, noBracket, clean, redirect
import time

xmlfile = 'dump.xml'

def iterate_xml(xmlfile):
    doc = etree.iterparse(xmlfile, events=('start', 'end'))
    _, root = next(doc)
    start_tag = None
    for event, element in doc:
        if event == 'start' and start_tag is None:
            start_tag = element.tag
        if event == 'end' and element.tag == start_tag:
            yield element
            start_tag = None
            root.clear()

tag_thing = r"{http://www.mediawiki.org/xml/export-0.10/}"

firstlink = {}

xmldump = iterate_xml(xmlfile)

# to get the next page, do
print(next(xmldump)) # site info

# print(clean(next(xmldump).find(f"{tag_thing}revision").findtext(f"{tag_thing}text"))[:500]) # first page
# print(clean(next(xmldump).find(f"{tag_thing}revision").findtext(f"{tag_thing}text"))[:500])
# print(clean(next(xmldump).find(f"{tag_thing}revision").findtext(f"{tag_thing}text"))[:500])
# print(clean(next(xmldump).find(f"{tag_thing}revision").findtext(f"{tag_thing}text"))[:500])

start = time.time()
for _ in range(100000):
    page = next(xmldump)

    revision = page.find("revision")
    if(type(revision) == NoneType):
        revision = page.find(f"{tag_thing}revision")

        # pagetext = page.find(f"{tag_thing}revision").findtext(f"{tag_thing}text")

    pagetext = revision.findtext(f"{tag_thing}text")
    if(type(pagetext) == NoneType):
        pagetext = revision.findtext("text")
  

    title = page.find(f"{tag_thing}title") # get title text
    if(type(title) == NoneType):
        title = page.find("title")

    print(title.sourceline)
    print(title.text)

    if("Template:" in title.text):
        print(f"{title.text} not supported")
        firstlink[title.text] = None
        continue


    text, redir = clean(pagetext)

    if(redir == True):

        # firstlink[title] = redirect(text)
        pass
    else:
        # find the first link
        try:
            if(len(flink(text)) > 254):
                print(f"{title.text} not working")
                print("sourceline", title.sourceline)
                print("attempted link:" ,flink(text))
                print("first bit of text:", text[:100])
                firstlink[title.text] = None
            else:
                # print(title.text)
                # print(title.sourceline)
                firstlink[title.text] = flink(text)
        except:
            print(f"{title.text} not supported")
            firstlink[title.text] = None
        # add to data structure
        pass

end = time.time()

print(f"finished building dict in {end-start} seconds")
# now we have data structure, export it
json_object = json.dumps(firstlink, indent = 2)
with open("wikilinks.json", "w") as outfile:
    json.dump(json_object, outfile)


# before you do the whole thing ,make sure to have the json readable
# ignore parentheses