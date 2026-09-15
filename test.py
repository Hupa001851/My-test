def merge_list(li1,li2):
    ln1=len(li1);ln2=len(li2)
    li3=[]
    i=0;j=0
    while(i<ln1 and j<ln2):
        if li1[i]<li2[j]:
            li3.append(li1[i]);i+=1
        else: li3.append(li2[j]);j+=1
    while(i<ln1):
        li3.append(li1[i]);i+=1
    while(j<ln2):
            li3.append(li2[j]);j+=1
    return li3
if __name__=='__main__':
    li1=[1,5,2,4,5,2,3,7,9,5]
    li2=[8,3,5,6,7,2,2,4,6,7]
    li3=merge_list(li1,li2)
    print(li3)