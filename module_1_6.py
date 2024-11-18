myDict = {"Mike" : 2007}
print("Dict: ",myDict)
myDict.update({"max" : 2000, "Anton" : 2005 })
a = myDict.pop("Anton")
print("Existing value: ",myDict.get("Mike"))
print("Not existing value: ",myDict.get('Alex'))
print("Deleted value: ",a)

print("Modified dictionary: ",myDict)


print("-------------------------------------------------------------------")

mySet = {0,1,2,3,4,5,5.5,6,(12,34,56),7,8,9,True,5,7,5.5,2,True,"abc",1,9,"abc",6,8,3}
print("Set: ",mySet)
mySet.add(65)
mySet.discard(0)
print('Modified set: ',mySet)