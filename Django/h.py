b = int(input('Введите '))

def saddle_point(a):
    count,last=0,0
    for i in a:
        if i.count(min(i)) == 1: #ищем мин
            m=i.index(min(i))
            col=[]
            for j in a:
                col.append(j[m]) #делаем список

            if col.count(max(col)) == 1 and min(i) == max(col): #смотрю похожи ли макс и мин

                result=(str(m), str(col.index(max(col)))) #записываю координаты если совпало
                count+=1
        if count > last: #печатаю, если новый ел
            last=count
            print (', '.join(result))
    if count == 0: #ошибка, если ниче нет
        print ('False')
print(saddle_point(b))