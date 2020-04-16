def designerPdfViewer(h,word):
    a,i,j=97,0,0
    c,l=[],[]
    while(i<len(h)):
        c.append(chr(a))
        c.append(h[i])
        l.append(c)
        a+=1
        c=[]
        i+=1
    i=0
    c=[]
    while(i<len(word)):
        if(word[i]==l[j][0]):
            c.append(l[j][1])
            i+=1
            j=0
        else:
            j+=1
        
    return max(c)*len(word)
        