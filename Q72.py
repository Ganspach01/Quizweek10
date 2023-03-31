#Grace Anspach
def hash_spam(x,y):
    index=0
    total=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            total+=1
            index>=4
            return this tweet will be considered as a spam!
        else:
            return None
    return index

print(hash_spam("This is a #complex string and has a # in it","#"))
