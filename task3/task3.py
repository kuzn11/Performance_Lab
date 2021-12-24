import json
import sys

def id_and_values_data(d2):
    lst=[]
    for item1 in d2['values']:
        lst.append(next(item1['value'] for item3 in d2['values'] if 'value' in item1))

    lst1 = []
    for item1 in d2['values']:
        lst1.append(next(item1['id'] for item3 in d2['values'] if 'id' in item1))

    id_and_values = {}
    for i in range(len(lst)):
        id_and_values[lst1[i]] = lst[i]
    return(id_and_values)

def inserting_values(d):
    id = 0
    for k, v in d.items():
        if isinstance(v, dict):
          inserting_values(v)
        elif isinstance(v, list):
            for item in v:
                inserting_values(item)
        else:
            if k == 'id':
                id = v
            if k == 'value':
                for key, value in id_and_values_data(data2).items():
                    if id == key and v =='':
                        d['value'] = value
    return(d)

if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 2:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    else:
        names = input()
        file1, file2 = names.split(' ')
    with open(file1, 'r') as f1:
        data1 = json.load(f1)

    with open(file2, 'r') as f2:
        data2 = json.load(f2)

    id_and_values_data(data2)
    inserting_values(data1)
    print(data1)

    with open("reoprt.json", "w") as f3:
        json.dump(data1, f3)