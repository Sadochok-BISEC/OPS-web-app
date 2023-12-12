from django.shortcuts import render
# Create your views here.

data = {
    # In the form(on the right)
    'obj_message_titles':{
        'hello': 'Привет!',
        'about': 'О проекте',
        'contacts': 'Контакты',
    },
    'obj_contacts_info':{
        'txt_message':'Наше Веб-приложение, разработано по решению оптимизационных задач', # About.html call
        'author_name':'Автор: Ilya Bisec',
        'email':'Почта: ilya.borisov.bisec@gmail.com',
        'phone_number':'Телефон:(29)4911431 - Беларусь',
    },
    'obj_tab_titles':{
        # Generally
        'main_page':'Главная страница',
        'simplex_page':'Симплекс метод',
        'monte_page':'Монте-Карло метод',
        'about_page':'О проекте',
        'contacts_page':'Контакты',
        'exit_page':'Выйти',
    }
}

def home(request):
    return render(request, 'main/main.html', data)

def about(request):
    return render(request, 'main/about.html', data)

def contacts(request):
    return render(request, 'main/contacts.html', data)