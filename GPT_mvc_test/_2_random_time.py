import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
import time

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

        self.model = Model()
        self.worker = None

        self.init_ui()

    def init_ui(self):
        self.label = QLabel("버튼을 눌러 작업 시작")
        self.button = QPushButton("작업 시작")
        self.button.clicked.connect(self.start_task)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_task(self):
        self.label.setText("작업 중...")
        self.worker = Worker(self.model)
        self.worker.finished.connect(self.on_finished)
        self.worker.start()

    def on_finished(self, result):
        self.label.setText(result)

# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
