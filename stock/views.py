from django.shortcuts import render

from stock.models import Stock
from stock.forms import StockForm


def stock(request):
    stock_ = Stock.objects.all()

    context_dict = {
        'stock_': stock_
    }

    return render(
        request=request,
        context=context_dict,
        template_name="stock/stock_list.html"
    )


def stock_form(request):
    if request.method == 'POST':
        stock_form = StockForm(request.POST)
        if stock_form.is_valid():
            data = stock_form.cleaned_data
            stock = Stock(
                name=data['piece'],
                due_date=data['add_date'],
                is_delivered=data['is_available'],
            )
            stock.save()

            stock_ = Stock.objects.all()
            context_dict = {
                'stock_': stock_
            }
            return render(
                request=request,
                context=context_dict,
                template_name="stock/stock_list.html"
            )

    stock_form = StockForm(request.POST)
    context_dict = {
        'stock_form': stock_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='stock/stock_form.html'
    )
