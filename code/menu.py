import pyqtgraph as pg

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from math import sqrt, floor

from constants import OBJECTS, Gravity
from design import Ui_MainWindow


def fix_time(time):
    if sorted(time, reverse=True) == time:
        return time
    del time[1]
    return fix_time(time)


class TheLawOfUniversalGravitation(QMainWindow, Ui_MainWindow):
    def __init__(self):
        pg.setConfigOption('background', '#f7f8fb')
        pg.setConfigOption('foreground', 'k')
        self.pen = pg.mkPen(color='#000', width=3)
        super().__init__()
        super().setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('data/Gravity.ico'))

        for i in OBJECTS.keys():
            self.planet.addItem(i)
        self.planet.setCurrentText('Земля')

        self.pushButton.clicked.connect(self.run)

        self.clear()

    def run(self):
        self.clear()
        m, r = OBJECTS[self.planet.currentText()]
        g = round(Gravity * (m / (r ** 2)), 2)
        weight = self.weight.text()
        height = self.height_n.text()

        if not weight:
            self.statusbar.showMessage('Введите массу!')
        else:
            weight = abs(float(weight))
            self.weight_n.display(round(g * weight, 5))

            if height:
                height = abs(float(height))
                time = sqrt((2 * height) / g)
                self.total_time.display(round(time, 5))
                self.max_speed.display(round(time * g, 5))
                self.power.display(Gravity * ((m * weight) / (r + height) ** 2))

                time_sp = [round(time, 2)] + [float(i / 2) for i in range(floor(time + 1) * 2)][::-1]
                time_sp = fix_time(time_sp)
                y1 = [float(g * i) for i in time_sp]
                y2 = [(g * (i ** 2)) / 2 for i in time_sp]
                self.speed.plot(time_sp, y1, pen=self.pen)
                self.length.plot(time_sp, y2, pen=self.pen)

    def clear(self):
        self.power.display('')
        self.total_time.display('')
        self.weight_n.display('')
        self.max_speed.display('')
        self.speed.clear()
        self.length.clear()
        self.statusbar.clearMessage()
