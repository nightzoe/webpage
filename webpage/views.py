from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')




def forpage(request):
    context = {}
    context['massage'] = 'วนซ้ำข้อมูล'

    if request.method == 'POST':
        count_str = request.POST.get('count')
        print('DEBUG: count_str =', count_str)
        context['debug_count_str'] = count_str
        try:
            number = int(count_str)
            if number > 0:
                table = []
                for i in range(1, 13):
                    table.append({'i': i, 'number': number, 'result': i * number})
                context['table'] = table
                context['number'] = number
            else:
                context['table'] = []
                context['number'] = None
                context['error'] = 'กรุณากรอกตัวเลขมากกว่า 0'
        except (TypeError, ValueError):
            context['table'] = []
            context['number'] = None
            context['error'] = 'กรุณากรอกตัวเลขที่ถูกต้อง'
    else:
        context['table'] = []
        context['number'] = None

    return render(request, 'for.html', context)





