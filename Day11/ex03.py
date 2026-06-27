'''
라이브러리
- 라이브러리란 여러 패키지와 모듈들을 모아놓은 것을 의미한다
파이썬에서는 기본적으로 제공되는 라이브러리와 pip 로 설치를 진행하여
사용하는 라이브러리가 있다

pip란
- 파이썬의 패키지를 설치하고 관리하는데 사용하는 패키지 매니저
사용방법
pip install 패키지명   => 라이브러리 설치시 사용
pip uninstall 패키지명  => 해당 라이브러리 제거시 사용
pip list => 현재 설치된 패키지 확인
pip install --upgrade 패키지명 => 현재 설치된 라이브러리 업데이트

pip install requests
- HTTP 요청을 보내고 응답을 받는데 사용되는 라이브러리

에러코드 종류
200 : 요청응답이 정상
400 : 요청이 잘못 됨 !!
403 : 권한없음
500 : 서버 오류
'''
import requests
url = "https://www.naver.com/"
# 해당 주소로 요청을 보내는 행위
response = requests.get(url);

if response.status_code == 200:
    html = response.text;
    print(html);
