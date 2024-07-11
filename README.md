# stock_Project
## Introduce
YFinance API를 사용하여 주식정보를 DB에 저장하여 이를 웹사이트에서 차트형태로 볼 수 있는 기능을 구현하는 것이 목표입니다.

## Main Function
1. YFinance를 설치하여 YFinance에서 데이터를 가져올 준비를 합니다.
> pip install yfinance

2. 가져온 데이터를 DataFrame으로 만들어 CSV파일로 저장합니다. 여기서 DataFrame은 Pandas를 사용합니다.
> python manage.py import_yf_api Start_date End_date

3. CSV파일의 내용을 DB에 저장합니다.
> python manage.py import_csv

4. CSV파일을 삭제합니다. CSV파일의 내용이 DB에 저장되어있기 때문에 물리적으로 가지고있을 이유가 없습니다.
> python manage.py delete_csv

5. DB의 내용을 차트로 표현합니다.

6. Login, Logout, SignUP 기능을 추가하여 사용자 계정이 있는 사람만이 접근 가능하도록 합니다.

7. 주식 가격을 Open, High, Low, Close, AdjClose, Volume 6가지로 표현합니다.

8. 주식 정보는 차트로 표현하며 이는 월별 평균을 1년 주기로 나타냅니다.

## Requirement
|기술|이름|
|:-:|:-:|
|Language|Python 3.8|
|DataFrame|Pandas|
|Data|YFinance|
|BE|Django|
|FE|Html, CSS, JS|
|DB|SQLite3|

## Web Application Screenshots
> python manage.py runserver
### Login
![image](https://github.com/kdk0411/stock_Project/assets/99461483/4e683a92-5ae8-4c20-a72a-552092294656)
### SignUp
![image](https://github.com/kdk0411/stock_Project/assets/99461483/f6bead1c-b7f4-4af5-a443-d79985fdbb09)
### Main
![image](https://github.com/kdk0411/stock_Project/assets/99461483/cce9c427-1efb-40b2-b6e1-9bab5d22eb3c)
### Detail
![image](https://github.com/kdk0411/stock_Project/assets/99461483/261edf70-10ee-49f0-a373-abf949819d66)


