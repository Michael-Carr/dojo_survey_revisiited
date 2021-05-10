from django.shortcuts import render, redirect
COLORS = (
    'blue',
    'red',
    'yellow',
    'green',
    'pink'
)
GENDERS = (
    'male',
    'female',
    'other',
    'RNS',
    'yes'
)
# Create your views here.
def index(request):
    context = {
        'color': COLORS,
        'gender': GENDERS
    }
    return render(request,'form.html',context)
def process(request):
    if request.method == 'GET':
        return redirect ('/')
    request.session['result'] = {
        'user': request.POST[ 'username'],
        'col': request.POST[ 'color'],
        'gen': request.POST ['gender']
    }
    return redirect('/result')
def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'results.html', context)
