import json

def over(movie):
    if movie['user_rating'] >= 8:
        return True
    else:
        return False

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # => True