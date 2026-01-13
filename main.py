import sys
import random
import time
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QDialog
from PyQt5.QtGui import QMovie, QFont
from PyQt5.QtCore import Qt, QTimer, QTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.random_num_dialogs = []

        self.setWindowTitle("KotApp")
        self.setStyleSheet("background-color: #0B0F64;")

        self.title = QLabel("Welcome to KotApp!", self)
        self.title.setGeometry(280, 90, 700, 60)
        self.title.setFont(QFont("Comic Sans MS", 36))
        self.title.setStyleSheet("color: #B2B5F5;")

        self.subtitle = QLabel("It's Pointless!", self)
        self.subtitle.setGeometry(455, 160, 700, 40)
        self.subtitle.setFont(QFont("Comic Sans MS", 18))
        self.subtitle.setStyleSheet("color: #B2B5F5;")

        self.ver = QLabel("Public Beta 3", self)
        self.ver.setGeometry(1770, 1020, 200, 60)
        self.ver.setFont(QFont("Comic Sans MS", 12))
        self.ver.setStyleSheet("color: #B2B5F5")

        self.img = QLabel(self)
        self.img.setGeometry(50, 50, 200, 200)
        self.img.setStyleSheet("border: 3px solid #B2B5F5;"
                               "border-radius: 5px;")

        self.gif = QMovie("assets/img/kottaniec.gif")
        self.img.setMovie(self.gif)
        self.gif.start()
        self.img.setScaledContents(True)

        c_button = QPushButton("Window Spammer", self)
        c_button.setGeometry(1390, 50, 200, 50)
        c_button.setStyleSheet("background-color: #B2B5F5; color: #0B0F64; font-size: 18px; font-weight: bold;")
        c_button.clicked.connect(self.window_spam)

        self.a1_button = QPushButton("Music 1", self)
        self.a1_button.setGeometry(1600, 50, 100, 50)
        self.a1_button.setStyleSheet("background-color: #B2B5F5; color: #0B0F64; font-size: 18px; font-weight: bold;")
        self.a1_button.clicked.connect(self.music_1)

        self.a2_button = QPushButton("Music 2", self)
        self.a2_button.setGeometry(1710, 50, 100, 50)
        self.a2_button.setStyleSheet("background-color: #B2B5F5; color: #0B0F64; font-size: 18px; font-weight: bold;")
        self.a2_button.clicked.connect(self.music_2)

        self.m_button = QPushButton("🔊", self)
        self.m_button.setGeometry(1820, 50, 50, 50)
        self.m_button.setStyleSheet("background-color: #B2B5F5; color: #0B0F64; font-size: 18px; font-weight: bold;")
        self.m_button.clicked.connect(self.music_on_off)

        self.time_label = QLabel(self)
        self.time_label.setGeometry(50, 920, 550, 110)
        self.time_label.setFont(QFont("Comic Sans MS", 76))
        self.time_label.setStyleSheet("color: #B2B5F5")

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1)

        self.update_time()

    def rnum_spawn(self):
        rnum = RandomNum()
        rnum.move(random.randint(0, 1800), random.randint(0, 1800))
        rnum.show()
        self.random_num_dialogs.append(rnum)

    def window_spam(self):
        self.sender().hide()

        pygame.mixer.music.stop()
        pygame.mixer.music.load("assets/audio/garythargy.mp3")
        pygame.mixer.music.play(-1)

        self.gif.stop()
        self.gif = QMovie("assets/img/kotmad.gif")
        self.img.setMovie(self.gif)
        self.gif.start()

        self.title.setText("ok")
        self.subtitle.setText("enjoy a bunch of windows now")

        self.rnum_timer = QTimer(self)
        self.rnum_timer.timeout.connect(self.rnum_spawn)
        self.rnum_timer.start(500)

    def music_on_off(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

            self.m_button.setText("🔈")
        else:
            pygame.mixer.music.unpause()

            self.m_button.setText("🔊")

    def music_1(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("assets/audio/alone.mp3")
        pygame.mixer.music.play(-1)

    def music_2(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("assets/audio/tiburtina.mp3")
        pygame.mixer.music.play(-1)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

class RandomNum(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("no")
        self.setGeometry(0, 0, random.randint(50, 300), random.randint(50, 300))

        random_num = random.randint(0, 676)
        random_num_str = str(random_num)

        label = QLabel(random_num_str, self)

        self.show()

        QTimer.singleShot(3000, self.close)

def main():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/audio/alone.mp3")
    pygame.mixer.music.play(-1)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()