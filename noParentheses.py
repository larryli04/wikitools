import copy

def noParentheses(string):
    if("(" not in string):
        return string
    else:
        pcounter = 1

    string = "" + str(string)

    start = string.index("(")
    end = 0
    for i in range(start+1, len(string)):
        if string[i] == "(":
            pcounter += 1
        elif string[i] == ")":
            pcounter -= 1
        
        if pcounter == 0:
            end = i
            break


    return string[0:start] + string[end+1:]


def noBracket(string):


    string = string.replace("\n", "")
    pcounter = 1

    string = "" + str(string)

    start = string.index("{")

    end = 0
    for i in range(start+1, len(string)):
        if string[i] == "{":
            pcounter += 1
        elif string[i] == "}":
            pcounter -= 1
        
        if pcounter == 0:
            end = i

            break
        # print(pcounter)


    
    return string[:start] + string[end+1:]

def noApos(string):
    try:
        index = string.index(r"'''")
    except:
        # print("No bold text found, probably a redirect")
        return string, True # pass something that says its a redirect
    # print(string)
    return string[index:], False

def flink(string):

    pcounter = 1

    string = "" + str(string)

    start = string.index("[")

    end = 0
    for i in range(start+1, len(string)):
        if string[i] == "[":
            pcounter += 1
        elif string[i] == "]":
            pcounter -= 1
        
        if pcounter == 0:
            end = i

            break
        # print(pcounter)

    return string[start+2:end-1]

def link(string):
    return string[2:-2]

def redirect(string):
    return flink(string[9:])

def clean(string):
    s = string
    if(string[0] == "#"):
        return None, True

    while(len(s) != 0 and s[0]=="{"):

        s = noBracket(s)
        # print(s[:2000])


    # get rid of newlines
    s = s.replace("\n", "")

    # start at bold text
    # print(noApos(string)[:50])
    return noApos(string)




# print()
# print(noBracket(t))
# print("-----------------------------------------------------------------")
# print(noBracket(noBracket(t)))
# print("-----------------------------------------------------------------")
# print(noBracket(noBracket(noBracket(t))))
# print("-----------------------------------------------------------------")
# print(noBracket(noBracket(noBracket(noBracket(t)))))




# print(clean(r"{{short description|Political philosophy and movement}}{{other uses}}{{redirect2|Anarchist|Anarchists|other uses|Anarchist (disambiguation)}}{{distinguish|Anarchy}}{{pp-semi-indef}}{{good article}}{{use British English|date=August 2021}}{{use dmy dates|date=August 2021}}{{anarchism sidebar}}{{basic forms of government}}"))