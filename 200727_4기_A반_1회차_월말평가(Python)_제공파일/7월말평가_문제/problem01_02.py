import json

def title_length(movie):
    return len(movie['title'])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(title_length(movie)) 
    # => 4