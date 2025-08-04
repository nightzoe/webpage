from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')




def forpage(request):
    items = [
        {'name': 'หน้าหลัก', 'url': 'home'},
        {'name': 'เกี่ยวกับ', 'url': 'about'},
        {'name': 'ติดต่อ', 'url': 'contact'},
        {'name': 'For Page', 'url': 'for_page'},
    ]
    count = range(1, 11)
    return render(request, 'for.html', {'items': items, 'count': count})





