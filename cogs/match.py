from fuzzywuzzy import fuzz
from fuzzywuzzy import process

f = open("names.txt",'r')
file = f.readlines()

choices = []
for x in file:
    choices.append(x.strip("\n"))

#print(file)
while True:
    f = input("Enter: ")

    a=[]
    b=[]
    c=[]
    a.append(f)
    for x in process.extract(f, choices, scorer=fuzz.token_sort_ratio, limit = 10):
       a.append(x)
    for x in process.extract(f, choices, scorer=fuzz.token_set_ratio, limit = 10):
        b.append(x)
    for x in process.extract(f, choices, limit = 10):
        c.append(x)


    print(b)
    print(c)


    matched = {}
    for x, match in enumerate(b,1):
        #print(match[1])
        if match[1] == 100:
            matched.update({x:match[0]})
            #print(match[0])
    exact = len(matched)
    #close = []
    counter = exact+1
    for match in (c):
        if match[1] >= 90:
            if not match[0] in matched.values():
                matched.update({counter:match[0]})
                counter += 1

    if exact == 1:
        print(matched[1])
    elif exact >1:
        print("Possible matches found:")
        for x in range(1,exact+1):
            m = matched[x]
            i = m.find("query")
            print(str(x) + ": " + m[:i] + "**" + m[i:i+len(query)] + "**" + m[i+len(query):])

    if len(matched) > exact:
        if exact == 0:
            print("No matches found. ")
        print("Maybe you meant:")
        for x in range(exact+1, len(matched)+1):
            #print(x)
            print(str(x) + ": " + matched[x])



    """
    for x in process.extractWithoutOrder(f, choices, scorer=fuzz.token_sort_ratio, score_cutoff=90):
       a.append(x)
    for x in process.extractWithoutOrder(f, choices, scorer=fuzz.token_set_ratio, score_cutoff=90):
        b.append(x)
    for x in process.extractWithoutOrder(f, choices, score_cutoff=90):
    """
    #print(a)


    #print(matched)
    #print(close)
