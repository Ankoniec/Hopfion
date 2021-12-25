from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from simulation import Simulation
import numpy as np


class SimulationChart(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100) -> object:
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(projection='3d')
        FigureCanvas.__init__(self, fig)
        self.electric_field = None
        self.magnetic_field = None
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        

    def camera_update(self, azimuth:int, elevation:int) -> None:
        self.axes.view_init(azimuth,elevation)
        self.draw()


    def sim1_init_figure(self, draw_magnetic:bool=False, draw_electric:bool=False,
                        init_time:float=0, azimuth:int=30, elevation:int=30, 
                        time_label:object=None, time_slider:object=None,
                        start_button:object=None, stop_button:object=None) -> None:
        
        self.azi = azimuth
        self.elev = elevation
        self.time_label = time_label
        self.time_slider = time_slider
        self.start_button = start_button
        self.stop_button = stop_button

        if draw_magnetic==True:
            self.magnetic_field = Simulation(1,-1,1,init_time,'magnetic')
            BX, BY, BZ = self.magnetic_field.field_line()
            self.axes.plot(BX,BY,BZ,'black')

        if draw_electric==True:
            self.electric_field = Simulation(1,-1,1,init_time,'electric')
            EX, EY, EZ = self.electric_field.field_line()
            self.axes.plot(EX,EY,EZ,'teal') 

        self.axes.view_init(self.azi,self.elev)
        self.draw()
        self.start_sim1_time()


    def start_sim1_time(self) -> None:
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(10)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)


    def update_figure(self) -> None:
        self.axes.cla()
        if self.electric_field:
            self.time_label.setText(str(self.electric_field.t))
            self.time_slider.setValue(int(self.electric_field.t/0.05))
            EX, EY, EZ = self.electric_field.field_line()
            self.axes.plot(EX,EY,EZ,'teal')
            if self.electric_field.t >= 10.0:
                self.stop_time()
            
        if self.magnetic_field:
            self.time_label.setText(str(self.magnetic_field.t))
            self.time_slider.setValue(int(self.magnetic_field.t/0.05))
            BX, BY, BZ = self.magnetic_field.field_line()
            self.axes.plot(BX,BY,BZ,'black')
            if self.magnetic_field.t >= 10.0:
                self.stop_time()

        self.axes.view_init(self.azi,self.elev)
        self.draw()


    def stop_time(self) -> None:
        try:
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
        except AttributeError:
            pass


    def sim2_init_figure(self, draw_magnetic:bool=False, draw_electric:bool=False,
                        init_time:float=0, azimuth:int=30, elevation:int=30, lines:int=20,
                        start_button:object=None, stop_button:object=None) -> None:

        theta = np.linspace(0,2*np.pi-2*np.pi/lines,lines)
        self.axes.cla()
        self.start_button = start_button
        self.stop_button = stop_button
        self.start_sim2_time()

        if draw_magnetic==True:
            for th in theta:
                BX, BY, BZ = Simulation(np.cos(th),np.sin(th),1,init_time,'magnetic').field_line()
                self.axes.plot(BX,BY,BZ,'black',alpha=0.6)

        if draw_electric==True:
            for th in theta:
                EX, EY, EZ = Simulation(1,np.sin(th),np.cos(th),init_time,'electric').field_line()
                self.axes.plot(EX,EY,EZ,'teal',alpha=0.6)
                
        self.axes.view_init(azimuth,elevation)
        self.draw()
        self.stop_time()


    def start_sim2_time(self) -> None:
        self.timer = QtCore.QTimer(self)
        self.timer.start(10)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)