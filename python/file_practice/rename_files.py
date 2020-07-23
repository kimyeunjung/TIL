import os

os.chdir(r'C:\Users\aclass\TIL\python\file_practice\dummy') #여기 경로로 이동

file_names = os.listdir('.') #  현재 경로(괄호안에 경로 적어야함) 에 있는 모든 파일의 목록을  file_name으로 리스트로 가져온다.

print(file_names)


for file_name in file_names:
    os.rename(file_name, f'SAMSUNG_{file_name}')