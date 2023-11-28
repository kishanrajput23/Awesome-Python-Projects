def greedyknapsack(items, max_weight):
    items.sort(key=lambda x: x[1]/x[0])
    result = []
    for item in items:
        if max_weight - item[1] >= 0:
            result.append(item)
            max_weight -= item[1]
    return result 
Weights = [int(item) for item in input("Enter the weight of items : ").split()]
Values = [int(item) for item in input("Enter the value of items : ").split()]
max_weight = int(input("Enter the max weight : "))
items=[]
for x in range(len(Weights)):
    items.append((Weights[x],Values[x]))
#items = [[6, 6], [10, 2], [3, 1],[5,8],[1,3],[3,5]]
print(greedyknapsack(items, max_weight))
s=greedyknapsack(items, max_weight)
sum=0
for x in s:
    sum+=x[0]
print("Optimal value = "+str(sum))


