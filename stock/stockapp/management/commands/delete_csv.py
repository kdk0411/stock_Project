import os
import glob
from django.core.management.base import BaseCommand

# Command -> python manage.py delete_csv


class Command(BaseCommand):
	help = 'CSV 파일을 삭제합니다.'

	csv_folder_path = 'C:\\Users\\Administrator\\Desktop\\stock_Project\\stock_data'

	def handle(self, *args, **kwargs):
		csv_path = self.csv_folder_path
		if os.path.isdir(csv_path):
			file_pattern = os.path.join(csv_path, '*.csv')
			csv_files = glob.glob(file_pattern)

			if not csv_files:
				self.stdout.write(self.style.ERROR("CSV 파일을 찾을 수 없습니다."))
				return
			for csv_file in csv_files:
				self.delete_file(csv_file)

		elif os.path.isfile(csv_path):
			self.delete_file(csv_path)
		else:
			self.stdout.write(self.style.ERROR("옳바른 CSV파일의 경로를 입력하세요."))

	def delete_file(self, csv_file):
		try:
			os.remove(csv_file)
			self.stdout.write(self.style.SUCCESS(f'{csv_file} 파일 삭제 완료'))
		except FileNotFoundError:
			self.stdout.write(self.style.ERROR(f'{csv_file}을 찾을 수 없습니다.'))
		except Exception as e:
			self.stdout.write(self.style.ERROR(f'{csv_file}을 삭제하는 동안 알 수 없는 ERROR가 발생했습니다. : {e}'))