import sys
import numpy as np
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QLabel

class GazeInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gaze Interface')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create buttons for each application
        keyboard_button = QPushButton('Virtual Keyboard')
        services_button = QPushButton('Services')
        help_button = QPushButton('Help')
        contact_button = QPushButton('Contact')
        messages_button = QPushButton('Messages')

        # Add buttons to the layout
        layout.addWidget(keyboard_button)
        layout.addWidget(services_button)
        layout.addWidget(help_button)
        layout.addWidget(contact_button)
        layout.addWidget(messages_button)

        # Connect button clicks to actions
        keyboard_button.clicked.connect(self.open_keyboard)
        services_button.clicked.connect(self.open_services)
        help_button.clicked.connect(self.open_help)
        contact_button.clicked.connect(self.open_contact)
        messages_button.clicked.connect(self.open_messages)
        
        self.pointer_label = QLabel(self)
        self.pointer_label.setPixmap(QPixmap('pointer.png'))  # Remplacez 'pointer.png' par l'image de votre choix
        self.pointer_label.setGeometry(0, 0, 50, 50)  # Réglez la taille du pointeur comme vous le souhaitez

        # Initialisez la détection des yeux
        self.cap = cv2.VideoCapture(0)  # Utilisez la webcam par défaut (vous pouvez ajuster l'index si nécessaire)

        # Créez une minuterie pour mettre à jour la position du pointeur
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_gaze)
        self.timer.start(50)  # Mettez à jour toutes les 50 millisecondes (ajustez si nécessaire)
    def update_gaze(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Chargez le classificateur en cascade pour les yeux
            eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

            # Détectez les yeux dans l'image
            eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            if len(eyes) > 0:
                # Prenez le premier œil détecté
                x, y, w, h = eyes[0]

                # Calculez la position du pointeur en fonction de l'emplacement de l'œil
                gaze_x = x + w // 2
                gaze_y = y + h // 2

                # Mettez à jour la position du pointeur sur l'interface
                self.pointer_label.move(gaze_x, gaze_y)

    def closeEvent(self, event):
        self.cap.release()  # Libérez la webcam lorsque l'application est fermée
        event.accept()


    def open_keyboard(self):
        # Implement action for the virtual keyboard
        print('Opening Virtual Keyboard')

    def open_services(self):
        # Implement action for services
        print('Opening Services')

    def open_help(self):
        # Implement action for help
        print('Opening Help')

    def open_contact(self):
        # Implement action for contact
        print('Opening Contact')

    def open_messages(self):
        # Implement action for messages
        print('Opening Messages')

def main():
    app = QApplication(sys.argv)
    interface = GazeInterface()
    interface.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
