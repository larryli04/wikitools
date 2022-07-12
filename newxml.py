from types import NoneType
from lxml import etree
from pprint import pprint
import json
from noParentheses import flink, clean, redirect
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
errors = {}
xmldump = iterate_xml(xmlfile)

# to get the next page, do
print(page := next(xmldump)) # site info

# print(clean(next(xmldump).find(f"{tag_thing}revision").findtext(f"{tag_thing}text"))[:500]) # first page
# print(clean(next(xmldump).find(f"{tag_thing}revision").findtext(f"{tag_thing}text"))[:500])
# print(clean(next(xmldump).find(f"{tag_thing}revision").findtext(f"{tag_thing}text"))[:500])
# print(clean(next(xmldump).find(f"{tag_thing}revision").findtext(f"{tag_thing}text"))[:500])
articles = 10000000
start = time.time()

# jump = 16790000
# # jump to section
# for _ in range(jump):
#     next(xmldump)
# print(f"jumped to {jump}th entry")

try:
    article=0
    while page != None:
        page = next(xmldump)
        article+=1

        if(article % 10000 == 0):
            print(article)
            print(page.sourceline)
            json_object = json.dumps(errors, indent = 2)
            with open(f"errors/errors{article}.json", "w") as outfile:
                json.dump(json_object, outfile)


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


        # print(title.sourceline)
        # print(title.text)

        if(":" in title.text):
            if("Template:" in title.text or "File:" in title.text or "Wikipedia:" in title.text or "MediaWiki:" in title.text or "image:" in title.text or "Draft:" in title.text or "Portal:" in title.text or "Category" in title.text or "Help:" in title.text or "Module:" in title.text or "TimedText:" in title.text):    
                # print(f"{title.text} ignored (Files and templates not supported)")
                # firstlink[title.text] = None
                continue
        if("(disambiguation)" in title.text):
            continue
        if("List of railway stations" in title.text or "List of" in title.text):
            continue
        if("{{wiktionary redirect" in pagetext):
            continue



        try:
            text, redir = clean(pagetext)
        except:
            print(pagetext)
        if(redir == 69):
            continue
        elif(redir == 42):
            print(f"{title.text} not working (42)")
            print("sourceline", title.sourceline)
            print("attempted link:" ,flink(text))
            print("first bit of text:", text[:100])
        elif(redir == True):
            # ignore redirects

            firstlink[title.text] = redirect(text)
            pass
        else:
            # find the first link
            try:
                if(len(flink(text)) > 254):
                    print(f"{title.text} not working")
                    print("sourceline", title.sourceline)
                    print("attempted link:" ,flink(text))
                    print("first bit of text:", pagetext[:200])
                    print("clean output", clean(pagetext)[:200])
                    firstlink[title.text] = None
                else:
                    # print(title.text)
                    # print(title.sourceline)
                    try:
                        firstlink[title.text] = flink(text)
                    except:
                        print(title.text)
            except:
                print(f"{title.text} not supported")
                errors[title.text] = {"title": title.text, "text": pagetext}
                
                # print("first bit of text:", pagetext)
                firstlink[title.text] = None
                
            # add to data structure
            

            pass
except StopIteration as e:
    print("Done")

end = time.time()


print(f"finished building dict in {end-start} seconds")
print(f"dict has {len(firstlink)} entries") # about 80% entries
if(page == None):
    print("Somehow finished all entries without an error")
else:
    print(f"Total time estimated to be {(6500000/articles)*(end-start)/60} minutes")

# now we have data structure, export it
json_object = json.dumps(firstlink, indent = 2)
with open("wikilinks.json", "w") as outfile:
    json.dump(json_object, outfile)

json_object = json.dumps(errors, indent = 2)
with open("errors.json", "w") as outfile:
    json.dump(json_object, outfile)


# before you do the whole thing ,make sure to have the json readable
# ignore parentheses