# Made by Ganijon Tashamtov
# At the beginning don't forget to install matplotlib
# Just type in terminal: pip install matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

oy = []
ox = []

fig, ax = plt.subplots()

def submit(text):
    x, y = map(float, text.split(";"))
    if (0 > x)  or (x > 1) or (0 > y) or (y > 50):
        return
    ox.append(x)
    oy.append(y)
    ax.plot(ox, oy, '-go', label="<I> = f( cos(a)^2 )")
    text_box.set_val('')


axbox = plt.axes([0.15, 0.90, 0.8, 0.075]) #
text_box = TextBox(axbox, 'Add point', initial="0;0")
text_box.on_submit(submit)

ax.plot(ox, oy,'-go', label="<I> = f( cos(a)^2 )")
ax.legend()
plt.show()
