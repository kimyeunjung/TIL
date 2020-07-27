import json

def history(movie):
    d = "과거"
    if movie['overview'] == "f'{d}'"
        True
    else:
        False

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # => False