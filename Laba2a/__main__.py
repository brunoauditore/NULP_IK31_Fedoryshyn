from modules import common

print("Перша константа", False)
print(abs(-12.5), f"є рівним {abs(12.5)}")
A = True
if A:
    print("A = True")
else:
    print("A = False")

B = False

try:
    print("Що буде , якщо число поділити на False - ")
    10/B
except Exception as e:
    print(e)
finally:
    print("finally завжди виконається")

with open("README.md", "r") as f:
    for line in f:
        print(line)


this_lambda = lambda x , y: x+y
print(this_lambda(4,3), "Лямбда - це анонімна функція , зазвичай її розумно використовувати , коли вона потрібне лише раз , або два")

#common.my_def(True)
common.eror(3,4)
