from django.shortcuts import render,redirect
from django.views import View
from .forms import IncomeCateogyForm,IncomeFrom
from django.contrib import messages
from .models import IncomeCategory,Income
# Create your views here.
class IncomeCategoryView(View):
    template_name = 'income_category.html'

    def get(self,request):
        context = {
            'form':IncomeCateogyForm(),
            'category':IncomeCategory.objects.filter(user_id=request.user.id)
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = IncomeCateogyForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,"saved successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"sorry error occured")
            return redirect('dashboard')



class IncomeAddView(View):
    template_name = 'add_income.html'
    def get(self,request):
        context = {
            'form': IncomeFrom(id=request.user.id)
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = IncomeFrom(request.user.id,request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"successfully added")
            return redirect('income')
        else:
            return render(request,self.template_name,context={'form':form})

class IncomeView(View):
    template_name = 'income.html'

    def get(self,request):
        context = {
            'all':Income.objects.all()
        }
        return render(request,self.template_name,context)