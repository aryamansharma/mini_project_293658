def dic(word):

    import json
    from difflib import get_close_matches
    data = json.load(open("data.json"))

    w = word.lower()
    lis = get_close_matches(w,data.keys(), n = 1, cutoff = 0.8)
     
    if w in data:
        return data[w]
    
    elif w.title() in data:
        return data[w.title()]
    
    elif w.upper() in data:
        return data[w.upper()]
    
    elif len(lis) > 0:
        
        yn = input("did you mean %s instead , Enter [y] if Yes or [n] if No : \n" %lis[0])
        
        yn1 = yn.lower()
        
        if yn1 == 'y':
            return data[lis[0]]

        elif yn1 == 'n':
            return "the word doesnt exists. double check it"
        
        else:
            return "we didnt understand. please check your ans."
        
    else:
        return "word not found"

def out():
    output = dic(input("Enter your word : "))
    if type(output) == list:
        for item in output:
            print(item,"\n")
    else:
        print(output)

out()