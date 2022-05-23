import pandas as pd
csv = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')


asATuple = [(key, value) for key, value in csv.items()]
asADict = {key:value for key, value in csv.items()}
asAList = [[key, value] for key, value in csv.items()]


print(asATuple)
print(asADict)
print(asAList)

