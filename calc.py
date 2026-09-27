'''
Program to calculate a Howard Student's GPA, based upon their current classes 
with respective credit values, and the grade they expect/get in each course
'''

class Student():
    def __init__(self, grades: dict, total_credits: float):
        self._grades = grades
        self._gpa_calc = dict()
        self._creds = total_credits

    def print_grades(self):
        '''Returns the subject and grades for each'''
        print(self._grades)

    def calc_gpa(self):
        '''Calculates gpa for the student object'''
        sum = 0
        gpa: float = 0
        for key in self._grades.keys():
            weight = self._grades[key][0] * self._grades[key][1]
            self._gpa_calc[key] = weight
        
        for key in self._gpa_calc.keys():
            sum += self._gpa_calc[key]
        
        gpa = sum / self._creds
        self._gpa = gpa

    def print_gpa(self):
        '''Returns GPA for student'''
        print(f"Current student's GPA: {self._gpa:.2f}")

            


if __name__ == "__main__":
    student_grades = dict()

    run = True
    n = 0
    total_credits = 0

    while run == True:
        n += 1
        sub_name = input(f"\nEnter the name of subject {n}: ")
        credit = int(input(f"\nEnter the credit value for the subject: "))
        grade = input(f"\nEnter the grade (expected or actual): ")
        match grade:    
            case 'A' | 'a':
                grade = 4
            case 'B' | 'b':
                grade = 3
            case 'C' | 'c':
                grade = 2
            case _:
                grade = 0

        student_grades[sub_name] = [credit, grade]
        total_credits += credit

        run = True if input("\nContinue? (y/n)").lower().strip() == 'y' else False

    Jovan = Student(student_grades, total_credits)

    Jovan.print_grades()
    Jovan.calc_gpa()
    Jovan.print_gpa()






