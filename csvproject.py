def getDictForPerson(my_tweet_history):
    mydict = {}
    
    if(type(my_tweet_history) is not str):
        print("not string")
        return
    fullPatternID = '{"created_at": (.*?)\\n{"created_at"'
    count =0
    #print(type(my_tweet_history))
    listOfTweets = re.findall(fullPatternID, my_tweet_history)
    
    for i in listOfTweets:


        currID = re.search('"id": (.*?)\,', i).group(1)

        currURL = re.search('media_url": "(.*?)\",', i)
        if currURL is None:
            mydict[currID] = "None"

        else:
            mydict[currID] = currURL.group(1)
            #print(currURL.group(1))
            #print(currURL.group(1))
        #print(type(currURL))
        count+=1

    #print(newlist)
    #print(count)
    return mydict
def downloadDict(mydict, id):
    #print("downloading user ",id)
    if(mydict is None):
        return
    workingDir = "C:/Users/david/Desktop/mediaProject"
    path = os.path.join(workingDir, id)
    if(os.path.isdir(path)):
        return
    os.mkdir(path)
    for key, value in mydict.items():
        if value != "None":
            
            #print(key, "has images", value)
            fullpath = os.path.join(path,key)
            r = requests.get(value)
            if r.status_code ==404:
                print("404")
            elif r.status_code ==403:
                print("403")
            
            else:
                urllib.request.urlretrieve(value, fullpath)
        else:
            pass
            #print(key," has no images")
count = 0

for i in df["UserID"]:
    tweet_history = df.iloc[count]["TweetHistory"]
    #print("on id: ",i)
    currdict = getDictForPerson(tweet_history)
    
    stringI = str(i)
    downloadDict(currdict,stringI)
    #print("COUNT")
    print(count)
    count+=1
