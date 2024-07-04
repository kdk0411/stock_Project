from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Avg

from .forms import CreateUserForm
from .models import Stock
import calendar
import json

def main_page(request):
    return render(request, 'main_page.html')


@login_required
def stock_detail(request, stock_id):
    selected_year = request.GET.get('year', '2022')  # 기본값은 2022년

    try:
        # 최근 날짜 기준으로 해당 주식 종목 데이터 가져오기
        latest_data = Stock.objects.filter(stock_id=stock_id).latest('date')

        # 선택된 연도 각 달의 평균 데이터 계산
        monthly_avg_data = []
        for month in range(1, 13):
            first_day = f'{selected_year}-{month:02d}-01'
            last_day = f'{selected_year}-{month:02d}-{calendar.monthrange(int(selected_year), month)[1]}'
            avg_data = Stock.objects.filter(
                stock_id=stock_id,
                date__range=[first_day, last_day]
            ).aggregate(
                Avg('Open'), Avg('High'), Avg('Low'), Avg('Close'), Avg('AdjClose'), Avg('Volume')
            )

            monthly_avg_data.append({
                'month': month,
                'Open': avg_data['Open__avg'] or 0,
                'High': avg_data['High__avg'] or 0,
                'Low': avg_data['Low__avg'] or 0,
                'Close': avg_data['Close__avg'] or 0,
                'AdjClose': avg_data['AdjClose__avg'] or 0,
                'Volume': avg_data['Volume__avg'] or 0
            })

        context = {
            'stock_id': stock_id,
            'latest_data': latest_data,
            'monthly_avg_data': json.dumps(monthly_avg_data),
            'selected_year': selected_year,
        }
        return render(request, 'stock_detail.html', context)

    except Stock.DoesNotExist:
        return render(request, 'stock_detail.html', {'error': '주식 데이터를 찾을 수 없습니다.'})


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registration/Signup.html', context)


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/Login.html'

    def get_success_url(self):
        return reverse_lazy('stock:main_page')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('stock:login')


