Laba2
========================
### Інсталюю pipenv та всі необхідні бібліотеки .

### Створюю app.py та test.py 
### Запускаю pytest - результат успішний
###8) В app.py дописую функцію , яка провіряє час доби

    def home_work():
        s = str (datetime.now())
        t = int (s[11:13])
        if t >= 00 and t <= 12:
            return("Ніч")
        else:
            return("День")
            
###9) Тестую функцію home_work , резульат успішний
    def test_home_work(self):
        # Ваш захист
        self.assertEqual(home_work(), "День")
        
###10) Перенаправляю вивід команди pytest в файл result.txt , використовуючи команду:
    pytest test/test.py > result.txt