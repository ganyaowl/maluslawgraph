import matplotlib.pyplot as plt

oy = []
ox = []
for i in range(10):
    x, y = map(float, input().split(";"))
    if 0 <= x <= 1 and 0 <= y <= 50:
        ox.append(x)
        oy.append(y)

fig, ax = plt.subplots()
ax.plot(ox, oy, label="<I> = f( cos(a)^2 )")
ax.legend()

plt.show()
