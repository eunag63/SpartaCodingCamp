#f-string
name = '홍길동'
age = '30'

hello = '제 이름은 '+name+'이구요'
helle = f'제 이름은 {name}입니다. 나이는 {age}입니다.'
print(helle)

#datetime 함수
from datetime import datetime

today = datetime.now()
mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
mytimo = today.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
print(mytimo)

#파일 이름 짓기
filename = f'file-{mytime}'