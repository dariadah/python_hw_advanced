from django.conf import settings
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import path
from urllib.parse import urlparse



# Конфигурация, не нужно редактировать
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['']
        }]
    )


def random_key():
	return base56.encode(randint(0, 0x7fffff))

    """
    про base56 подсказали здесь http://qaru.site/questions/16756428/base56-conversion-etc
    Случайный короткий ключ, состоящий из цифр и букв.
    Минимальная длина ключа - 5 символов. Для генерации случайных
    последовательностей вы можете воспользоваться библиотекой random.
    """
    


def index(request):
    """
    При запросе методом GET, отдаем HTML страницу (шаблон index.html) с формой
    с одним полем url типа text (отредактируйте шаблон, дополните форму).

    При отправке формы методом POST извлекаем url из request.POST и
    делаем следующее:

    1. Проверяем URL. Допускаются следующие схемы: http, https, ftp

    Если URL не прошел проверку - отобразите на нашей странице с формой
    сообщение о том, какие схемы поддерживаются.

    Если URL прошел проверку:

    2. Создаем случайный короткий ключ, состоящий из цифр и букв
    (функция random_key).

    3. Сохраняем URL в кеш со сгенерированным ключом:

    cache.add(key, url)

    4. Отдаем ту же страницу с формой и дополнительно отображаем на ней
    кликабельную короткую ссылку (HTML тег 'a') вида
    http://localhost:8000/<key>
    """
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        context = {}
        url = request.POST.get('url')
        result = urlparse(url)
        if result.scheme in ALLOWED_SCHEMES:
            key = random_key()
            cache.add(key, url)
            context['url'] = key
            return render(request, 'index.html', context)
        else:
            context['message'] = 'Please, enter another format'
            return render(request, 'index.html', context)


def redirect_view(request, key):
    """
    Функция обрабатывает сокращенный URL вида http://localhost:8000/<key>
    Ищем ключ в кеше (cache.get). Если ключ не найден,
    редиректим на главную страницу (/). Если найден,
    редиректим на полный URL, сохраненный под данным ключом.
    """
 	pass


def stats(request, key):
    """
    Статистика кликов на сокращенные ссылки.
    В теле ответа функция возращает количество
    переходов по данному коду.
    """
    pass


urlpatterns = [
    path('', index),
    path(r'stats/<key>', stats),
    path(r'<key>', redirect_view),
]


if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
