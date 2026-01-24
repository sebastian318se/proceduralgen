import engine
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Galapo Terrain Engine")

        # Container = Main Window Widget; Vertical (Box) Grid
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)       

        # Button Grid Over Graph View
        labels = ["1", "2"]
        bLayout = self.buttonGrid(labels)
        layout.addWidget(bLayout)

        # Main Window -- Place matplotlib terrain plot
        plch = QLabel('Insert plt')
        plch.setAlignment(Qt.AlignCenter)
        layout.addWidget(plch)
        
        canvas = FigureCanvasQTAgg(fig)
        canvas.draw_idle()
        layout.addWidget(canvas)

        genButton = QPushButton('Butoon')
        layout.addWidget(genButton)

        # Button Grid Under Graph View
        labels = ["1", "2", "3", "4"] 
        bLayout = self.buttonGrid(labels)
        layout.addWidget(bLayout)
       

    def buttonGrid(self, labels, columns = 2):

        container = QWidget()
        layout = QGridLayout(container)

        for i, text in enumerate(labels):
            x = (i // columns) # Two labels per row
            y = (i % columns) # Go down a row whenever remainder is 1
            button = QPushButton(text)
            layout.addWidget(button, x, y)

        return container

world = engine.TerrainEngine(
    height = 200,
    width = 200,

    periodX= 4,
    periodY = 4,

    seed = 0,
    dimension = "3D",
    water_level= 0
    )
fig = Figure()

if world.dimension == "3D":
    ax = fig.add_subplot(111, projection = "3d")
else:
    ax = fig.add_subplot(111)
    
# Break engine generate() into gen() and draw() to call directly from ui code and plot correctly. draw into qt axes
# (Make axes passed as arguments so it works both as standalone and ui appl. w/o dupe code)
# QT should know to update the plot because its axes are being used on the drawing code.
# canvas.draw_idle() to update it

app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()