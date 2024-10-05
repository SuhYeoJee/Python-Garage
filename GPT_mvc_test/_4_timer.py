import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QThread, pyqtSignal

# Model
class Model:
    def long_running_task(self):
        sleep_time = random.randint(1, 10)  # 1초에서 10초 사이의 랜덤한 시간
        time.sleep(sleep_time)  # 랜덤 시간 동안 작업 시뮬레이션
        return f"작업 완료! (소요 시간: {sleep_time}초)"

# Worker Thread
class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self):
        result = self.model.long_running_task()
        self.finished.emit(result)

# View
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MVC Example")
        
        self.label = QLabel("버튼을 눌러 작업 시작")
        self.button = QPushButton("작업 시작")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Connect button click to start_task method
        self.view.button.clicked.connect(self.start_task)
        
        # Connect worker's finished signal to update the view
        self.worker = None

    def start_task(self):
        self.view.label.setText("작업 중...")
        self.worker = Worker(self.model)
        self.worker.finished.connect(self.on_finished)
        self.worker.start()

    def on_finished(self, result):
        self.view.label.setText(result)

# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = Model()
    view = MainWindow()
    controller = Controller(model, view)

    view.show()
    sys.exit(app.exec_())
