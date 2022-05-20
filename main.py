from cgitb import small
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from nerdle_gui import Ui_MainWindow

from collections import Counter
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.labels = [[self.label11, self.label12, self.label13, self.label14, self.label15, self.label16, self.label17, self.label18],
                       [self.label21, self.label22, self.label23, self.label24, self.label25, self.label26, self.label27, self.label28],
                       [self.label31, self.label32, self.label33, self.label34, self.label35, self.label36, self.label37, self.label38],
                       [self.label41, self.label42, self.label43, self.label44, self.label45, self.label46, self.label47, self.label48],
                       [self.label51, self.label52, self.label53, self.label54, self.label55, self.label56, self.label57, self.label58],
                       [self.label61, self.label62, self.label63, self.label64, self.label65, self.label66, self.label67, self.label68]]

        
        self.row = 0
        self.col = 0
        self.result = "11+11=22"
        self.input_str = ""
        self.game_state = "running"

        self.big_border()


    def wirte_num_2_label(self, num):
        self.labels[self.row][self.col].setText(str(num))
        self.next_col()

    def next_col(self):
        if self.col < 7:
            self.small_border()
            self.col += 1
            self.big_border()


    def number_button(self):
        if self.game_state == "running":
            nr_text = self.sender().text()
            self.wirte_num_2_label(nr_text)
    
    def operator_button(self):
        if self.game_state == "running":
            op_text = self.sender().text()
            self.wirte_num_2_label(op_text)

    def enter_button(self):

        validator = True
        # check for empty labels
        for i in self.labels[self.row]:
            if i.text() == "":
                validator = False
                break

        if validator:

            self.check_input()
        
    def check_input(self):
        self.input_str = ""

        for i in self.labels[self.row]:
            self.input_str = self.input_str + i.text()

        split_input_str = self.input_str.split("=")

        if eval(split_input_str[0]) == int(split_input_str[1]):
            self.check_input_right_numbers()
            if self.input_str == self.result:
                self.game_state = "finished"
                return False # If this is the right string the game should stop
            else:
                if self.check_for_last_row():
                    self.game_running()
                else:
                    dialog = QMessageBox(self)
                    dialog.setWindowTitle("Error")
                    dialog.setText("No guesses left!")
                    dialog.exec()
        else:
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Error")
            dialog.setText("That guess doesn't compute")
            dialog.exec()
    
    def game_running(self):
        self.row += 1
        self.col = 0
        self.small_border()
        self.big_border()


    def check_input_right_numbers(self):
        num_amount_dict = Counter(self.result)

        j = 0
        for i in self.input_str:
            if num_amount_dict[i] > 0:
                self.labels[self.row][j].setStyleSheet("background-color: yellow")
                num_amount_dict[i] -= 1
            else:
                self.labels[self.row][j].setStyleSheet("background-color: red")
            j += 1

        self.check_input_right_position(self.input_str)

    def check_input_right_position(self, right_numbers):
        for i in range(len(self.labels[self.row])):
            #print(right_numbers[i])
            if right_numbers[i] == self.result[i]:
                self.labels[self.row][i].setStyleSheet("background-color : green")

    def check_for_last_row(self):
        if self.row == 5:
            self.game_state = "game over"
            return False
        else:
            return True

    def deltete_button(self):
        if self.game_state == "running":
            if self.col == 7 and self.labels[self.row][self.col].text() != "":
                self.labels[self.row][self.col].clear()
            elif self.col > 0:
                self.small_border()
                self.col -= 1
                self.big_border()
                self.labels[self.row][self.col].clear()

    def small_border(self):
        self.labels[self.row][self.col].setStyleSheet("border: 1px solid black")

    def big_border(self):
        self.labels[self.row][self.col].setStyleSheet("border: 3px solid black")


        
app = QApplication()
win = MyWindow()

app.exec()