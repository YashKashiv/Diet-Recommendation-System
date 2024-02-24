import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class DietRecommendationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Diet Recommendation System")
        self.setGeometry(100, 100, 500, 500)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.image_label = QLabel(self)
        self.loadImage("img.jpg")
        layout.addWidget(self.image_label)

        self.label_weight = QLabel("Enter Weight (kg):")
        self.input_weight = QLineEdit(self)
        layout.addWidget(self.label_weight)
        layout.addWidget(self.input_weight)

        self.label_height = QLabel("Enter Height (cm):")
        self.input_height = QLineEdit(self)
        layout.addWidget(self.label_height)
        layout.addWidget(self.input_height)

        self.label_age = QLabel("Enter Age:")
        self.input_age = QLineEdit(self)
        layout.addWidget(self.label_age)
        layout.addWidget(self.input_age)

        self.label_veg_nonveg = QLabel("Select Diet:")
        self.radio_veg = QRadioButton("Vegetarian")
        self.radio_nonveg = QRadioButton("Non-Vegetarian")
        layout.addWidget(self.label_veg_nonveg)
        layout.addWidget(self.radio_veg)
        layout.addWidget(self.radio_nonveg)

        self.calculate_button = QPushButton("Calculate Diet")
        self.calculate_button.clicked.connect(self.calculateDiet)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.central_widget.setLayout(layout)

    def loadImage(self, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(200)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

    def calculateDiet(self):
        try:
            weight = float(self.input_weight.text())
            height = float(self.input_height.text())
            age = int(self.input_age.text())

            if self.radio_veg.isChecked():
                diet_type = "Vegetarian"
            elif self.radio_nonveg.isChecked():
                diet_type = "Non-Vegetarian"
            else:
                diet_type = "Unknown"

            if diet_type == "Vegetarian":
                bmr = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
            else:
                bmr = 66 + 13.7 * weight + 5 * height - 6.8 * age

            breakfast_calories = int(0.25 * bmr)
            lunch_calories = int(0.35 * bmr)
            dinner_calories = int(0.3 * bmr)
            snack_calories = int(0.1 * bmr)

            protein = int(0.15 * weight)
            carbohydrates = int(0.6 * bmr / 4)
            fiber = int(25)

            breakfast_protein = int(0.15 * protein)
            lunch_protein = int(0.4 * protein)
            dinner_protein = int(0.3 * protein)
            snack_protein = int(0.15 * protein)

            breakfast_carbs = int(0.4 * carbohydrates)
            lunch_carbs = int(0.4 * carbohydrates)
            dinner_carbs = int(0.3 * carbohydrates)
            snack_carbs = int(0.3 * carbohydrates)

            breakfast_fiber = int(0.3 * fiber)
            lunch_fiber = int(0.4 * fiber)
            dinner_fiber = int(0.3 * fiber)
            snack_fiber = int(0.2 * fiber)

            result_text = f"Caloric Intake: {int(bmr)} kcal/day\n\n"
            result_text += f"Breakfast: {breakfast_calories} kcal\n"
            result_text += f"  Protein: {breakfast_protein} g\n"
            result_text += f"  Carbohydrates: {breakfast_carbs} g\n"
            result_text += f"  Fiber: {breakfast_fiber} g\n"
            result_text += f"Lunch: {lunch_calories} kcal\n"
            result_text += f"  Protein: {lunch_protein} g\n"
            result_text += f"  Carbohydrates: {lunch_carbs} g\n"
            result_text += f"  Fiber: {lunch_fiber} g\n"
            result_text += f"Dinner: {dinner_calories} kcal\n"
            result_text += f"  Protein: {dinner_protein} g\n"
            result_text += f"  Carbohydrates: {dinner_carbs} g\n"
            result_text += f"  Fiber: {dinner_fiber} g\n"
            result_text += f"Snacks: {snack_calories} kcal\n"
            result_text += f"  Protein: {snack_protein} g\n"
            result_text += f"  Carbohydrates: {snack_carbs} g\n"
            result_text += f"  Fiber: {snack_fiber} g\n"

            self.result_label.setText(result_text)

        except Exception as e:
            self.result_label.setText("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DietRecommendationApp()
    window.show()
    sys.exit(app.exec_())
