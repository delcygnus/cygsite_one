from django.shortcuts import render

# statementapp view method.
def statementapp(request):
    return render(request, 'statementapp/statement.html')
