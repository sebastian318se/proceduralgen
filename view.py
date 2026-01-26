import engine
from PySide6.QtWidgets import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
import time

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.fig = Figure()
        self.setWindowTitle("Galapago Terrain Engine")

        # Container = Main Window Widget; Vertical (Box) Grid
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)       

        # Button Grid Over Graph View
        labels = ["1", "2"]
        bLayout = self.buttonGrid(labels)
        layout.addWidget(bLayout)

        # Main Window
        self.canvas = FigureCanvasQTAgg(fig)
        self.canvas.draw_idle()
        layout.addWidget(self.canvas)

        genButton = QPushButton('Generate Terrain')
        genButton.clicked.connect(self.updateRender)    
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
    
    def updateRender(self):
        
        global ax
        global fig
        
        world = engine.TerrainEngine(
        height = 200,
        width = 200,

        periodX= 4,
        periodY = 4,

        dimension = "3D",
        water_level= 0
        )

        try:
            ax.clear()
            ax.remove()

        except NameError:
            pass
        
        if world.dimension == "3D":
            ax = fig.add_subplot(111, projection = "3d")
        else:
            ax = fig.add_subplot(111)

        world.generate()
        world.draw(ax, self.fig)
        self.canvas.draw_idle()

fig = Figure()

app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()

# Set all properties in engine code as view code also depending on user input?
# Every widget as its own bit of code or optimize?