from django.shortcuts import render
from .models import Operation
from django.shortcuts import redirect

# Create your views here.

def home(request):
    result = None
    num1 = num2 = operator = ''

    if request.method == 'POST':
        try:
            #Define the variables that will be visible in the home page
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operator = request.POST.get('operator')

            #Apply the specified operation and save it into a result variable
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                result = 'Invalid operator'

            #Save the record as an object if the result is valid
            if isinstance(result, (int, float)):
                Operation.objects.create(
                    num1 = num1,
                    num2 = num2,
                    operator = operator,
                    result = result
                )

        #Return exception if the input is not valid
        except Exception as e:
            result = f'Error: {str(e)}'

    #Populate the HTML template with the variables
    context = {
        'title': 'Home page',
        'message': 'Welcome to the home page!',
        'result': result,
        'num1': num1,
        'num2': num2,
        'operator': operator,
    }
    return render(request, 'pages/home.html', context)

def history(request):
    operations = Operation.objects.all().order_by('-timestamp')

    #Clear records if the clear button is pressed and reload the page
    if request.method == 'POST':
        Operation.objects.all().delete()
        return redirect('history')

    return render(request, 'pages/history.html', {'operations': operations})

def about(request):
    context = {
        'title': 'About page',
        'message': 'This website is created with Django!',
    }
    return render(request, 'pages/about.html', context)