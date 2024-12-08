import sys
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QPushButton, QDateEdit, QMessageBox)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QPalette, QColor, QMovie

class AgeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age-O-Meter")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #f0f0f0;")
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Title
        title = QLabel("Age-O-Meter")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Date selection
        date_layout = QHBoxLayout()
        date_label = QLabel("Select your birthdate:")
        date_label.setFont(QFont('Arial', 12))
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setMaximumDate(QDate.currentDate())
        self.date_edit.setDisplayFormat("dd/MM/yyyy")
        date_layout.addWidget(date_label)
        date_layout.addWidget(self.date_edit)
        layout.addLayout(date_layout)
        
        # Calculate button
        self.calc_button = QPushButton("Calculate Age")
        self.calc_button.setFont(QFont('Arial', 12))
        self.calc_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.calc_button.clicked.connect(self.calculate_age)
        layout.addWidget(self.calc_button)
        
        # Result label
        self.result_label = QLabel()
        self.result_label.setFont(QFont('Arial', 12))
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)
        
        # Animation label
        self.animation_label = QLabel()
        self.animation_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.animation_label)
        
        self.movie = None
        
    def calculate_age(self):
        birth_date = self.date_edit.date().toPyDate()
        today = datetime.now().date()
        
        if birth_date > today:
            QMessageBox.warning(self, "Invalid Date", "Birth date cannot be in the future!")
            return
            
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day
        
        if days < 0:
            months -= 1
            days += 30
        if months < 0:
            years -= 1
            months += 12
            
        age_str = f"You are {years} years, {months} months, and {days} days old"
        self.result_label.setText(age_str)
        
        # Update animation based on age
        if self.movie:
            self.movie.stop()
        
        if years < 2:
            gif_path = "assets/baby.gif"
        elif years < 13:
            gif_path = "assets/child.gif"
        elif years < 20:
            gif_path = "assets/teen.gif"
        elif years < 60:
            gif_path = "assets/adult.gif"
        else:
            gif_path = "assets/elderly.gif"
            
        self.movie = QMovie(gif_path)
        self.animation_label.setMovie(self.movie)
        self.movie.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = AgeCalculator()
    calculator.show()
    sys.exit(app.exec_())
