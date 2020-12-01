Laba2
========================
### Інсталюю pipenv та всі необхідні бібліотеки .

### Створюю app.py та test.py 
### Запускаю pytest - результат успішний
### 8) В app.py дописую функцію , яка провіряє час доби

    def home_work():
        s = str (datetime.now())
        t = int (s[11:13])
        if t >= 00 and t <= 12:
            return("Ніч")
        else:
            return("День")
            
### 9) Тестую функцію home_work , резульат успішний
    def test_home_work(self):
       # Ваш захист
       self.assertEqual(home_work(), "День")
        
### 10) Перенаправляю вивід команди pytest в файл result.txt , використовуючи команду:
    pytest test/test.py > result.txt
    
### 11) Роблю коміт
### 12) Створю файл Makefile та заповнюю його :
    help:
        @echo "---------------HELP-----------------"
    
    
    install:
        @echo "---------------INSTALL-----------------"
        @pipenv --python 3.8
        pipenv shell
        pipenv install requests
        pipenv install ntplib
        pipenv install pytest
    
    test:
        pytest test/test.py > result.txt
    run:
        python3 app.py > result_py.txt
    deploy:
        git add .
        git commit -m "make deploy commit"
        git push


### 13) Клоную git середовище та запускаю make, результат - створиося середовище та інсталювалися всі бібліотеки , після чого  був виконаний файл app.py , виконаний тест та деплой