from django.shortcuts import render,redirect
from django.views import View
from .forms import ExpensesCategoryForm,ExpensesForm
from django.contrib import messages
from .models import Expenses,ExpensesCategory
# Create your views here.
class ExpenesCategoryView(View):
    template_name = 'expenses_category.html'

    def get(self,request):
        context = {
            'form':ExpensesCategoryForm(),
            'category': ExpensesCategory.objects.filter(user_id=request.user.id)
        }
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = ExpensesCategoryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS, "saved successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "sorry error occured")
            return redirect('dashboard')


class ExpensesAddView(View):
    template_name = 'add_expenses.html'
    def get(self,request):
        context = {
            'form': ExpensesForm(request.user.id)
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = ExpensesForm(request.user.id,request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"successfully added")
            return redirect('expenses')
        else:
            return render(request,self.template_name,context={'form':form})



class ExpenseView(View):
    template_name = 'expenses.html'

    def get(self,request):
        return render(request,self.template_name)

    def get(self,request):
        context = {
            'all':Expenses.objects.all()
        }
        return render(request,self.template_name,context)