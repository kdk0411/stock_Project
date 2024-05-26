import csv
import os
import glob
from django.core.management.base import BaseCommand
from stockapp.models import Stock


# 명령어로 사용 -> python manage.py read_csv_yfinance csv 파일 디렉토리 경로
class Command(BaseCommand):
    help = 'CSV 파일을 DB로 이전합니다.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_path = kwargs['csv_file']
        if os.path.isdir(csv_path):
            file_pattern = os.path.join(csv_path, '*.csv')
            csv_files = glob.glob(file_pattern)

            if not csv_files:
                self.stdout.write(self.style.ERROR('Do Not Fount CSV Files in the directory'))
                return
            for csv_file in csv_files:
                self.process_file(csv_file)
        elif os.path.isfile(csv_path):
            self.process_file(csv_path)
        else:
            self.stdout.write(self.style.ERROR('Please enter a valid CSV file or directory path.'))

    def process_file(self, csv_file):
        try:
            self.import_data(csv_file)
            self.stdout.write(self.style.SUCCESS(f'{csv_file} 파일 이전 완료'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'{csv_file} not found. Please check the file again.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unknown error occurred while processing {csv_file}: {e}'))

    def import_data(self, csv_file):
        with open(csv_file, 'r', encoding='UTF8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.create_stock(row)

    def create_stock(self, data):
        try:
            Stock.objects.create(
                date=data['Date'],
                stock_id=data['ticker'],
                Open=data['Open'],
                High=data['High'],
                Low=data['Low'],
                Close=data['Close'],
                AdjClose=data['AdjClose'],
                Volume=data['Volume'],
            )
        except Exception as e:
            self.handle_error(data, e)

    def handle_error(self, data, exception):
        self.stdout.write(self.style.ERROR(f'Error: {data}'))
        self.stdout.write(self.style.ERROR(f'Error detail: {exception}'))
