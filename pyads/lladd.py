from list import SingleLL
A = SingleLL()
A.append(1)
A.append(9)
A.append(7)

def toArr(slist):
    if(slist.nextNode == None):
        print(slist.value)
    else:
        recList(slist.nextNode)
recList(A.head)
