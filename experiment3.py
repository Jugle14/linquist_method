from json import load
import matplotlib.pyplot as plt
import matplotlib as mpl

def x_y_maker(dic):
    xs = []
    ys = []
    
    for key, value in dic.items():
        xs.append(int(key))

        try:
            percent = value['length'] / value['times'] 
        except ZeroDivisionError:
            percent = 0
        
        ys.append(percent)

    return xs, ys

with open('average_keys_per_length.json', 'r') as r:
    dic = load(r)

dpi = 80

figure = plt.figure(dpi=dpi, figsize = (1012/dpi, 768/dpi))
mpl.rcParams.update({"font.size": 10})   #!!!!

plt.title("Ефективність метода Лінквіста для української мови")
plt.xlabel("Довжина зашифрованого тексту")
plt.ylabel("Середня кількість ключів")

xs, ys = x_y_maker(dic)

y_max = int(max(ys))+1

ax = plt.axes()
ax.yaxis.grid(True)
ax.xaxis.grid(True)
plt.yticks([1, 3] + list(range(0, y_max))[::2])
plt.xticks(xs[:-11:10] + [xs[-1]])

plt.plot(xs, ys, linestyle = 'solid')


#figure.savefig("results.png")
plt.xlim(1, xs[-1])
plt.show()
