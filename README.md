### Description
파이썬에서 gspread library를 사용해서 실험 기록을 자동화해보자!

### Prerequisie

먼저 google cloud api key를 발급 받아야 함!

1. [gspread 사용법 사이트](https://greeksharifa.github.io/references/2023/04/10/gspread-usage/#google_vignette)를 참고해서 먼저 키를 발급 받기
2. 1을 완료하면 api key가 담긴 json 파일을 하나 다운 받을 수 있음.
3. 이를 path='~/.config/gspread/service_account.json'에 추가.
4. google spread sheet에서 json file에 있는 client_email을 입력해 사용자 추가.

그리고 나서, gspread library를 설치해주자
```
pip install gspread
```
자세한 사용법은 * 이 파일을: https://github.com/OnedayOneyeah/gspread_tutorial/blob/main/gspread_tutorial.ipynb<http://example.com/> 참조:)
