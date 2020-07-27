import json
from pprint import pprint #pprint를 불러옴

def rotate(data):
    am = []
    pm = []
    for i in range(0, len(data)):
        for z in range(0, len(data[i])):
            if z == 0:
                am.append(data[i][0])
                          
            elif z == 1:
                pm.append(data[i][1])
                
    dic = {
        'am':am,
        'pm':pm
    }
    pprint(dic)
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }
