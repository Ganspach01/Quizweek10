#Grace Anspach
def count_hashtag(x,y):
    index=0
    total=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            total+=1
            index+=1
        else:
            index+=1
    return index

print(count_hashtag("This is a #complex string and has a # in it","#"))
