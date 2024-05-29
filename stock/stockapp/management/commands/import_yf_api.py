import yfinance as yf
from django.core.management.base import BaseCommand
import os

# Command -> python manage.py import_yf_api 2024-01-01 2024-05-29


class Command(BaseCommand):
    help = '주식 정보를 가져옵니다.'

    def add_arguments(self, parser):
        parser.add_argument('start', type=str, help='데이터 시작 날짜 (YYYY-MM-DD)')
        parser.add_argument('end', type=str, help='데이터 종료 날짜 (YYYY-MM-DD)')

    symbols = ['005930.KS', 'AAPL', 'TSLA', '000660.KS', '373220.KS', '005380.KS', '000270.KS', '035720.KS', '035420.KS']
    cols = ['Date', 'ticker', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

    def handle(self, *args, **kwargs):
        start_date = kwargs['start']
        end_date = kwargs['end']

        output_dir = 'C:\\Users\\Administrator\\Desktop\\stock_Project\\stock_data'
        os.makedirs(output_dir, exist_ok=True)  # 디렉토리가 없으면 생성

        for symbol in self.symbols:
            try:
                df = yf.download(symbol, start=start_date, end=end_date)
                df.reset_index(inplace=True)
                df['ticker'] = symbol
                df = df[self.cols]
                file_path = os.path.join(output_dir, f'{symbol}.csv')
                df.to_csv(file_path, index=False)
                self.stdout.write(self.style.SUCCESS(f'Successfully downloaded data for {symbol}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error downloading data for {symbol}: {e}'))
