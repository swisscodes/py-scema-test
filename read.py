import json
from textwrap import indent


if __name__ == "__main__":
    with open('data/data_1.json') as f:
        data = json.load(f)
    
    
    def reader(data, result=None):
        if not result:
            result={}
        if isinstance(data, dict):
            dataArr = data.keys()
        else:
            dataArr = data
        itemlength = len(dataArr)
        while(itemlength > 0):
            for i, v in enumerate(dataArr):
                if isinstance(v, list): # i could add a generic iter here but not enough time
                    reader(v, result)
                elif isinstance(data[v], dict): # specifically check for object so we can add it to result
                    result[v] = data[v]
                    reader(data[v], result)
                if(isinstance(result, list)):
                    result[itemlength-1] = type(data[v]).__name__ 
                else:
                    data[v] = type(data[v]).__name__
                itemlength-=1

        with open('schema.json', 'w') as f:
            json.dump(result, f)
            '''Here also we writing new always i could fix this but not enough time'''
        return result

    print(reader(data))