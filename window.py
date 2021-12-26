from PyQt5 import QtCore, QtWidgets
from canvas import SimulationChart
import matplotlib
matplotlib.use('Qt5Agg')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow:object) -> None:
        MainWindow.setObjectName("Hopfion")
        MainWindow.resize(750, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.chart_widget = QtWidgets.QWidget(MainWindow)
        self.chart_widget.setGeometry(QtCore.QRect(335, 20, 400, 400))
        self.chart_widget.setObjectName("chart_widget")
        self.chart = SimulationChart(self.chart_widget,width=4,height=4, dpi=100)

        self.create_buttons()
        self.create_sliders()
        self.create_labels()
        self.create_lines()
        self.connect_buttons()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def create_buttons(self):
        self.simtype1_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.simtype1_radioButton.setGeometry(QtCore.QRect(30, 50, 300, 17))
        self.simtype1_radioButton.setObjectName("simtype1_radioButton")
        self.simtype2_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.simtype2_radioButton.setGeometry(QtCore.QRect(30, 70, 300, 17))
        self.simtype2_radioButton.setObjectName("simtype2_radioButton")

        self.electricfield_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.electricfield_checkBox.setGeometry(QtCore.QRect(40, 100, 111, 17))
        self.electricfield_checkBox.setObjectName("electricfield_checkBox")
        self.magneticfield_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.magneticfield_checkBox.setGeometry(QtCore.QRect(160, 100, 131, 17))
        self.magneticfield_checkBox.setObjectName("magneticfield_checkBox")

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(15, 360, 140, 50))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(165, 360, 140, 50))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setEnabled(False)
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(10, 10, 20, 20))
        self.infoButton.setObjectName("infoButton")
        

    def create_sliders(self):
        self.timeSlider = QtWidgets.QSlider(self.centralwidget)
        self.timeSlider.setGeometry(QtCore.QRect(70, 140, 201, 22))
        self.timeSlider.setMaximum(200)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.linesSlider = QtWidgets.QSlider(self.centralwidget)
        self.linesSlider.setGeometry(QtCore.QRect(70, 180, 201, 22))
        self.linesSlider.setMaximum(40)
        self.linesSlider.setOrientation(QtCore.Qt.Horizontal)
        self.linesSlider.setObjectName("elevationSlider")
        self.linesSlider.setValue(20)

        self.azimuthSlider = QtWidgets.QSlider(self.centralwidget)
        self.azimuthSlider.setGeometry(QtCore.QRect(70, 270, 201, 22))
        self.azimuthSlider.setMaximum(360)
        self.azimuthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.azimuthSlider.setObjectName("azimuthSlider")
        self.azimuthSlider.setValue(30)
        self.elevationSlider = QtWidgets.QSlider(self.centralwidget)
        self.elevationSlider.setGeometry(QtCore.QRect(70, 310, 201, 22))
        self.elevationSlider.setMaximum(180)
        self.elevationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.elevationSlider.setObjectName("elevationSlider")
        self.elevationSlider.setValue(30)


    def create_labels(self):
        self.timeNumber_label = QtWidgets.QLabel(self.centralwidget)
        self.timeNumber_label.setGeometry(QtCore.QRect(280, 138, 21, 23))
        self.timeNumber_label.setObjectName("timeNumber")
        self.linesNumber_label = QtWidgets.QLabel(self.centralwidget)
        self.linesNumber_label.setGeometry(QtCore.QRect(280, 178, 100, 23))
        self.linesNumber_label.setObjectName("linesNumber")
        self.aziNumber_label = QtWidgets.QLabel(self.centralwidget)
        self.aziNumber_label.setGeometry(QtCore.QRect(280, 270, 100, 23))
        self.aziNumber_label.setObjectName("aziNumber")
        self.elevNumber_label = QtWidgets.QLabel(self.centralwidget)
        self.elevNumber_label.setGeometry(QtCore.QRect(280, 308, 100, 23))
        self.elevNumber_label.setObjectName("elevNumber")

        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(30, 138, 100, 21))
        self.time_label.setObjectName("time_label")
        self.lines_label = QtWidgets.QLabel(self.centralwidget)
        self.lines_label.setGeometry(QtCore.QRect(30, 178, 100, 21))
        self.lines_label.setObjectName("lines_label")
        self.azimuth_label = QtWidgets.QLabel(self.centralwidget)
        self.azimuth_label.setGeometry(QtCore.QRect(20, 268, 100, 16))
        self.azimuth_label.setObjectName("azimuth_label")
        self.elevation_label = QtWidgets.QLabel(self.centralwidget)
        self.elevation_label.setGeometry(QtCore.QRect(10, 308, 100, 16))
        self.elevation_label.setObjectName("elevation_label")
        self.camposition_label = QtWidgets.QLabel(self.centralwidget)
        self.camposition_label.setGeometry(QtCore.QRect(110, 230, 150, 16))
        self.camposition_label.setObjectName("camposition_label")
        self.settings_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_label.setGeometry(QtCore.QRect(110, 20, 150, 16))
        self.settings_label.setObjectName("settings_label")


    def create_lines(self):
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(310, 10, 20, 420))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(90, 240, 131, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 30, 131, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")


    def connect_buttons(self):
        self.timeSlider.valueChanged.connect(self.update_slider_labels)
        self.linesSlider.valueChanged.connect(self.update_slider_labels)
        self.azimuthSlider.valueChanged.connect(self.update_slider_labels)
        self.elevationSlider.valueChanged.connect(self.update_slider_labels)
        self.startButton.clicked.connect(self.start_simulation)
        self.stopButton.clicked.connect(self.stop_simulation)
        self.infoButton.clicked.connect(self.display_info)
        self.simtype1_radioButton.clicked.connect(self.disable_sim2)
        self.simtype2_radioButton.clicked.connect(self.enable_sim2)


    def retranslateUi(self, MainWindow:object) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hopfion"))
        self.electricfield_checkBox.setText(_translate("MainWindow", "electric field (blue)"))
        self.magneticfield_checkBox.setText(_translate("MainWindow", "magnetic field (black)"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.infoButton.setText(_translate("MainWindow", "?"))
        self.timeNumber_label.setText(_translate("MainWindow", "0"))
        self.linesNumber_label.setText(_translate("MainWindow", "20"))
        self.aziNumber_label.setText(_translate("MainWindow", "30"))
        self.elevNumber_label.setText(_translate("MainWindow", "30"))
        self.time_label.setText(_translate("MainWindow", "time"))
        self.lines_label.setText(_translate("MainWindow", "lines"))
        self.azimuth_label.setText(_translate("MainWindow", "azimuth"))
        self.elevation_label.setText(_translate("MainWindow", "elevation"))
        self.camposition_label.setText(_translate("MainWindow", "Camera's position"))
        self.settings_label.setText(_translate("MainWindow", "Simulation's settings"))
        self.simtype1_radioButton.setText(_translate("MainWindow", "time evolution of a single field line"))
        self.simtype2_radioButton.setText(_translate("MainWindow", "field lines in a given time"))


    def disable_sim2(self):
        self.linesSlider.setEnabled(False)
        self.stopButton.setEnabled(False)


    def enable_sim2(self):
        self.linesSlider.setEnabled(True)
        self.stopButton.setEnabled(False)


    def update_slider_labels(self):
        self.timeNumber_label.setText(str(self.timeSlider.value()*0.05))
        self.linesNumber_label.setText(str(self.linesSlider.value()))
        self.aziNumber_label.setText(str(self.azimuthSlider.value()))
        self.elevNumber_label.setText(str(self.elevationSlider.value()))
        self.chart.camera_update(self.azimuthSlider.value(),self.elevationSlider.value())


    def start_simulation(self):

        if self.simtype1_radioButton.isChecked():

            self.chart.sim1_init_figure(
                self.magneticfield_checkBox.isChecked(),
                self.electricfield_checkBox.isChecked(),
                self.timeSlider.value()*0.05,
                self.timeNumber_label,
                self.timeSlider,
                self.startButton,
                self.stopButton,
                self.azimuthSlider,
                self.elevationSlider
            )

        elif self.simtype2_radioButton.isChecked():

            self.chart.sim2_init_figure(
                self.magneticfield_checkBox.isChecked(),
                self.electricfield_checkBox.isChecked(),
                self.timeSlider.value()*0.05,
                self.linesSlider.value()
            )
            
        else:
            self.display_message()


    def stop_simulation(self):
        self.chart.stop_time()
    

    def display_message(self):
        self.message = QtWidgets.QMessageBox()
        self.message.setIcon(QtWidgets.QMessageBox.Warning)
        self.message.setWindowTitle("Warning")
        self.message.setText("Please choose a simulation mode.")
        self.message.exec()


    def display_info(self) -> None:
        self.info = QtWidgets.QMessageBox()
        self.info.setIcon(QtWidgets.QMessageBox.Information)
        self.info.setWindowTitle("Hopfion - information")
        self.info.setText(
            "Application made in order to visualize time evolution of a knotted electromagnetic field which is a topologically non-trivial solution to Maxwell equations in a vacuum."+"\n"+
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+
            "The program works in two different modes:\n 1. time evolution of a single field line - visualization of chosen field as an animation. User can choose time when the simulation starts and watch how the field line change from that moment."+'\n'+
            "2. field lines in a given time - enables the user to choose how many lines to draw and calculates them at the given time, so we can observe how the electric and magnetic field looks like in general.\n\n"+ 
            "Please notice that when choosing time over 5 seconds, the simulation needs more time to calculate field lines as they are getting bigger. Also, the more lines we want to draw, the longer it will take to calculate them.\n"+
            "In worst cases it can take up to one minute to show the calculated field (for example if we choose both electric and magnetic field at time of 10 seconds and 40 lines each)\n\n"+
            "User can choose position of the camera in both variants by changing azimuth and elevation."
            )
        self.info.exec()