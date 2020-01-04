from json import load
import matplotlib.pyplot as plt
import matplotlib as mpl

def x_y_maker(dic, step):
    xs = []
    ys = []
    
    count = 0
    for key, value in dic.items():
        xs.append(int(key))

        try:
            percent = value['param'][step] / (value['false'] + value['param'][step]) * 100
        except ZeroDivisionError:
            percent = 0
        
        ys.append(percent)
        
        if percent == 100:
            count += 1
        else:
            count = 0
        
        if count == 10:
            break

    return xs, ys

language = str(input('write "en" or "ua">>>'))

with open('results_2_'+language+'.json', 'r') as r:
    dic = load(r)

step_of_success = int(input('Write step of success>>>')) - 1
dpi = 80

figure = plt.figure(dpi=dpi, figsize = (1012/dpi, 768/dpi))
mpl.rcParams.update({"font.size": 10})   #!!!!

if language == 'en':
    plt.title("Ефективність метода Лінквіста для англійської мови")
else:
    plt.title("Ефективність метода Лінквіста для української мови")


plt.xlabel("Довжина зашифрованого тексту")
plt.ylabel("Процентаж успішного дешифрування")

xs, ys = x_y_maker(dic, step_of_success)

ax = plt.axes()
ax.yaxis.grid(True)
ax.xaxis.grid(True)
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.xticks(xs[:-11:10] + [xs[-1]])

plt.plot(xs, ys, linestyle = 'solid')


#figure.savefig("results.png")
plt.ylim(0, 100)
plt.xlim(0, xs[-1])
plt.show()
