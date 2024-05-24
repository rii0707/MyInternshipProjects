sentence=input("enter your sentence:\n")
print("-------------------------------------")
print("Your sentence:",sentence,"\n")
sentence=sentence.replace(',',' ').lower().split()
wc={}
for word in sentence:
    if word in wc.keys():
        wc[word]+=1
    else:
        wc[word]=1
print("--------------------------------------")
print("number of word counted:\n")
print(wc)