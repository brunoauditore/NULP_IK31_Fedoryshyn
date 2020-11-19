import logging
def my_def(A):
        for i in range(100):
            if A:
                if i % 2 == 0:
                    print(i)
            else:
                if i % 2 != 0:
                    print(i)


#### Функція з помилкою

def eror(x,z):
    try:
        y = x+z
        return y
        logging.info("Без помилок")
    except Exception as e:
        logging.error(e)





