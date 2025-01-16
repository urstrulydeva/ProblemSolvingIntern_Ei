def CheckForMajorityElement(array):
    n=len(array)
    MajorityCount=0
    MajorityElement=None
    for i in array:
        if MajorityCount==0:
            MajorityElement=i
            MajorityCount=1
        elif MajorityElement==i:
            MajorityCount+=1
        elif MajorityElement!=i:
            MajorityCount-=1
    
    count=0
    for i in array:
        if i==MajorityElement:
            count+=1
    if count>=(n/2):
        return MajorityElement
    return -1

array=[1,2,2,2,3,4]
ans=CheckForMajorityElement(array)
print(ans)
