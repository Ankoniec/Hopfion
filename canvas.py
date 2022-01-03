from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from simulation import Simulation
import numpy as np


class SimulationChart(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, 
                azimuth:int=30, elevation:int=30) -> object:

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(projection='3d')
        FigureCanvas.__init__(self, fig)
        self.electric_field = None
        self.magnetic_field = None
        self.azimuth = azimuth
        self.elevation = elevation
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        

    def camera_update(self, azimuth:int, elevation:int) -> None:
        self.azimuth = azimuth
        self.elevation = elevation
        self.axes.view_init(self.azimuth,self.elevation)
        self.draw()


    def sim1_init_figure(self, draw_magnetic:bool=False, draw_electric:bool=False, 
                        init_time:float=0, time_label:object=None, time_slider:object=None,
                        start_button:object=None, stop_button:object=None,
                        azimuth_slider:object=None, elevation_slider:object=None) -> None:
        
        self.time_label = time_label
        self.time_slider = time_slider
        self.start_button = start_button
        self.stop_button = stop_button
        self.azimuth_slider = azimuth_slider
        self.elevation_slider = elevation_slider
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.azimuth_slider.setEnabled(False)
        self.elevation_slider.setEnabled(False)

        self.axes.cla()

        if draw_electric:
            self.electric_field = Simulation(1,-1,1,init_time,'electric')
            EX, EY, EZ = self.electric_field.field_line()
            self.axes.plot(EX,EY,EZ,'teal')
        else:
            self.electric_field = None

        if draw_magnetic:
            self.magnetic_field = Simulation(1,-1,1,init_time,'magnetic')
            BX, BY, BZ = self.magnetic_field.field_line()
            self.axes.plot(BX,BY,BZ,'black')
        else:
            self.magnetic_field = None

        self.axes.view_init(self.azimuth,self.elevation)
        self.draw()
        self.start_time()


    def start_time(self) -> None:
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(10)


    def update_figure(self) -> None:
        self.axes.cla()

        if self.electric_field != None:
            self.time_label.setText(str(self.electric_field.t))
            self.time_slider.setValue(int(self.electric_field.t/0.05))
            EX, EY, EZ = self.electric_field.field_line()
            self.axes.plot(EX,EY,EZ,'teal')
            if self.electric_field.t >= 10.0:
                self.stop_time()
                self.electric_field = None
            
        if self.magnetic_field != None:
            self.time_label.setText(str(self.magnetic_field.t))
            self.time_slider.setValue(int(self.magnetic_field.t/0.05))
            BX, BY, BZ = self.magnetic_field.field_line()
            self.axes.plot(BX,BY,BZ,'black')
            if self.magnetic_field.t >= 10.0:
                self.stop_time()
                self.magnetic_field = None

        self.axes.view_init(self.azimuth,self.elevation)
        self.draw()


    def stop_time(self) -> None:
        try:
            self.timer.stop()
        except AttributeError:
            pass

        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.azimuth_slider.setEnabled(True)
        self.elevation_slider.setEnabled(True)



    def sim2_init_figure(self, draw_magnetic:bool=False, draw_electric:bool=False,
                        init_time:float=0, lines:int=20) -> None:

        theta = np.linspace(0,2*np.pi-2*np.pi/lines,lines)
        self.axes.cla()

        if draw_magnetic==True:
            for th in theta:
                BX, BY, BZ = Simulation(np.cos(th),np.sin(th),1,init_time,'magnetic').field_line()
                self.axes.plot(BX,BY,BZ,'black',alpha=0.6)

        if draw_electric==True:
            for th in theta:
                EX, EY, EZ = Simulation(1,np.sin(th),np.cos(th),init_time,'electric').field_line()
                self.axes.plot(EX,EY,EZ,'teal',alpha=0.6)
                
        self.axes.view_init(self.azimuth,self.elevation)
        self.draw()