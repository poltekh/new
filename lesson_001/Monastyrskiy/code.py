import os
import io
os.chdir('red_hat')
def f1(what_to,by_what):
    for roots, dirs,files in os.walk("."):
        for path in files:
            buff = []
            with open(path, encoding='utf-8') as f:
                for line in f:
                    res = line.replace(what_to,by_what,1)
                    print(res)
                    buff.append(res)
            with open(path, encoding='utf-8',mode="w") as R_file:
                R_file.writelines(buff)
f1('Чёрная Курточка','Красная Шапочка')



