import pandas as pd

data = pd.read_csv('data.csv')
a = data.loc[:, ['Name', 'Education']]
b = data.loc[:, ['Name', 'Age']]
a = a[a.duplicated()].drop_duplicates()
b = b[b.duplicated()].drop_duplicates()

c = pd.concat([a,b])
print("\nFinding Values :\n")    
print(c['Name'].value_counts()+1)

def pattern(filename,col):
    import csv
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        Dict = {}
        temp = ''
        for row in reader:
            for i in row[col]:
                if i.isupper():
                    temp = temp + 'X'
                elif i.islower():
                    temp = temp + 'x'
                elif i.isnumeric():
                    temp = temp + '9'
                else:
                    temp = temp + i
            if temp in Dict:
                Dict[temp] += 1
            else:
                Dict[temp] = 1
            temp = ""
    return(Dict)


print("\nFinding Patterns :\n")    
print("Name: ", pattern('data.csv','Name'))
print("Age: ", pattern('data.csv','Age'))
print("Education: ", pattern('data.csv','Education'))