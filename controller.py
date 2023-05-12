from view import *
from PyQt5.QtWidgets import *
import os

class Controller(QMainWindow, Ui_MainWindow):


    #stores value to determin operation to use when submit is clicked
    operation_value = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.submit_button.clicked.connect(lambda: self.submit_clicked())
        self.confirm_button.clicked.connect(lambda: self.confirm_clicked())
        self.restart_button.clicked.connect(lambda: self.restart_clicked())





    def restart_clicked(self):

        #hides and resets everything
        self.input_line1.hide()
        self.input_line2.hide()
        self.explanation_label.setText("")
        self.file_name_label.setText("")
        self.file_name_input.hide()
        self.submit_button.hide()
        self.input_line1_label.setText("")
        self.input_line2_label.setText("")
        self.restart_button.hide()

        #resets radiobuttons
        self.cat_ears_button.show()
        self.exponents_button.show()
        self.alien_ears_button.show()
        self.confirm_button.show()



        #clears user inputs
        self.input_line1.clear()
        self.input_line2.clear()
        self.file_name_input.clear()

        #clears error messages
        self.error_label.setText('')



    def submit_clicked(self):
        if self.operation_value == 1:

            try:

                #stores values
                base_value = int(self.input_line1.text())
                exponent_value = int(self.input_line2.text())

                #opens file
                file_name = self.file_name_input.text().strip().replace(' ', '')

                #runs recursion on values
                def pow(x,y):
                    if y == 1:
                        return x
                    elif y > 1:
                        return x * pow(x, y-1)

                #calls recursion function
                result = pow(base_value,exponent_value)





                #wrties recursion result to specified text file
                with open(f'{file_name}.txt', 'a') as f:
                    f.write(f'Operation: Exponents\nResult: {result}\n\n')
                    

                    
            except ValueError:
                self.error_label.setText('Enter Integers only')



        elif self.operation_value == 2:

            try:

                #retreives num of cats
                cats = int(self.input_line1.text())

                #retrieve file name
                file_name = self.file_name_input.text().strip().replace(' ', '')

                #cat ears recursion function
                def cat_ears(n):
                    if n == 0:
                        return 0
                    elif n == 1:
                        return 2
                    elif n > 1:
                        return 2 + cat_ears(n-1)

                #evaluates with recursion function
                result = cat_ears(cats)

                
                #writes result to file
                with open(f'{file_name}.txt', 'a') as f:
                    f.write(f'Operation: Cat Ears\nResult: {result}\n\n')


            except ValueError:
                self.error_label.setText('Enter Integers only')


        elif self.operation_value == 3:

            try:

                #retrieves alien value
                aliens = int(self.input_line1.text())


                #retrive file name
                file_name = self.file_name_input.text().strip().replace(' ', '')


                #recursion function for alien ears
                def alien_ears(n):
                    if n == 1:
                        return 3
                    else:
                        if n % 2 == 1:
                            return 3 + alien_ears(n - 1)
                        elif n % 2 == 0:
                            return 2 + alien_ears(n - 1)

                result = alien_ears(aliens)

                #writes result to file
                with open(f'{file_name}.txt', 'a') as f:
                    f.write(f'Operation: Alien Ears\nResult: {result}\n\n')

            except ValueError:
                self.error_label.setText('Enter Integers only')






    def confirm_clicked(self):
        if self.exponents_button.isChecked():


            #displays lables and input lines according to input
            self.explanation_label.setText('Provide 2 numbers\n(Integers Only)')
            self.input_line1.show()
            self.input_line2.show()
            self.input_line1_label.setText('Base')
            self.input_line2_label.setText('Exponent')
            self.input_line1_label.show()
            self.input_line2_label.show()

            #displays file output
            self.file_name_label.setText('        Input file name to export result to\n        (will be stored at .txt)')
            self.file_name_input.show()



            #hides radio buttons to not allow reselection without a clear button push
            self.alien_ears_button.hide()
            self.exponents_button.hide()
            self.cat_ears_button.hide()
            self.confirm_button.hide()

            #shows second set of buttons
            self.submit_button.show()
            self.restart_button.show()


            #sets operation_value
            self.operation_value = 1



        elif self.cat_ears_button.isChecked():

            self.input_line2.hide()
            self.input_line2_label.hide()
            
            #sets insructions for input line
            self.explanation_label.setText('Provde number of\ncats to calculate\ntotal ear count (Integers Only)')
            self.input_line1.show()
            self.input_line1_label.setText('# of Cats')





            #sets file name input field
            self.file_name_label.setText('        Input file name to export result to (.txt only)')
            self.file_name_input.show()

            #shows second set of buttons
            self.submit_button.show()
            self.restart_button.show()


            #hides radio buttons to not allow reselection without a clear button push
            self.alien_ears_button.hide()
            self.exponents_button.hide()
            self.cat_ears_button.hide()
            self.confirm_button.hide()

            self.submit_button.show()
            self.restart_button.show()

            #sets operation_value
            self.operation_value = 2






        elif self.alien_ears_button.isChecked():


            #hides buttons
            self.cat_ears_button.hide()
            self.alien_ears_button.hide()
            self.exponents_button.hide()
            self.confirm_button.hide()


            #hides other input fields
            self.input_line2.hide()
            self.input_line2_label.hide()


            #sets label texts
            self.explanation_label.setText('Provide number of\naliens to calculate\ntotal ear count (Integers Only)')
            self.input_line1_label.setText('# of Aliens')
            self.input_line1.show()


            #set file input text
            self.file_name_label.setText('        Input file name to export result to (.txt only)')
            self.file_name_input.show()


            #show second set of buttons
            self.submit_button.show()
            self.restart_button.show()


            #sets operation_value
            self.operation_value = 3





