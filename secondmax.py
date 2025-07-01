a=[2,3,9,6,7,34,23]
first=second=0
for i in range(len(a)):
    if(a[i]>first):
        second=first
        first=a[i]
    elif(a[i]<second and a[i]>first):
        second

print("first max is:",first,"\nsecond max is:",second)
