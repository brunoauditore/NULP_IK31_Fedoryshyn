# Laba3

### 1) Ініціалізую середовище та встановлюю django 
    pipenv --python 3.7
    pipenv install django
    
### 2) Створюю django проект та запускаю його
    pipenv run django-admin startproject my_site
    pipenv run python manage.py runserver
   
### 3) Створюю темплейт додатку 
    pipenv run python manage.py startapp main
    
### 4) Редагую main/views.py 

    def main(request):
        return render(request, 'main.html', {'parameter': "test"})
    
    
    def health(request):
        response = {
            'servername': 'lab server',
            'random': random.randint(0, 256),
            'datetime': datetime.now().isoformat(),
            'url': request.build_absolute_uri(),
    
            'server_iinfo': {
                'system': os.name,
                'srv_pid': os.getpid(),
                'user': os.getlogin(),
            },
    
            'client_info': {
                'user agent': request.META['HTTP_USER_AGENT'],
                'remote addr': request.META['REMOTE_ADDR'],
                'remote host': request.META['REMOTE_HOST'],
            }
        }
    
    
        return JsonResponse(response)
        
        
### 5) Створюю monitoring.py та редагую 

    logging.basicConfig(
        filename="server.log",
        filemode='a',
        level=logging.INFO,
        format='{levelname} {asctime} {name} : {message}',
        style='{'
    )
    log = logging.getLogger(__name__)
    
    
    def main(url):
        while True:
            try:
                r = requests.get(url)
                data = json.loads(r.content)
                logging.info("Сервер доступний. Час на сервері: %s", data['date'])
                logging.info("Запитувана сторінка: : %s", data['current_page'])
                logging.info("Відповідь сервера місти наступні поля:")
                for key in data.keys():
                    logging.info("Ключ: %s, Значення: %s", key, data[key])
            except requests.exceptions.ConnectionError as e:
                    logging.error("Помилка: " + str(e))
    
            time.sleep(60)
    
    
    if __name__ == '__main__':
        main("http://localhost:8000/health")

### 6) Редагую файл Pipfile , щоб спростити запуск:
    
    [scripts]
    server = "python3 manage.py runserver 0.0.0.0:8000"