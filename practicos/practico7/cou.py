
exampleDict = {'first': 3, 'second': 4, 'third': 2, 'fourth': 1}
sortedDict = dict(sorted(exampleDict.items(), key=lambda x: x[1]))
print(sortedDict)

valores = {5:200, 3:10000, 4:15000} 
valores_ord = dict(sorted(valores.items()))
print(valores_ord)