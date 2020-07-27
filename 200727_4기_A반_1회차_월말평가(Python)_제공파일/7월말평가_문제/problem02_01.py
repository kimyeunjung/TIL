import json


def check(data):
    
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            a = []
            if data[i][j] >= 37.5:
                a.append(data[i][j])
                print(a)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True
