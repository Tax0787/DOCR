import matplotlib.pyplot as plt

x = 20
y = int(x * (2 ** (1/2)))

linewidth = 1 / 32

xp, yp = 1080, 720

ppi = xp * yp / inch
dpi = 1200

plt.figure(dpi = dpi)

for line in range(y):
    plt.plot([i for i in range(x)], [line for _ in range(x)], color = 'k', linewidth = linewidth)
    
for line in range(x):
    const = line
    yg = [i for i in range(y)]
    f = lambda y : const
    x= list(map(f, yg))
    plt.plot(x, yg, color = 'k', linewidth = linewidth)


ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

plt.grid(True)

plt.show()

#plt.savefig(input('save src : '))