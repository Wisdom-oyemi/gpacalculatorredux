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

    ''' 
        Use as reference for grades  
            case 'A' | 'a':
                grade = 4
            case 'B' | 'b':
                grade = 3
            case 'C' | 'c':
                grade = 2
            case _:
                grade = 0
    '''

    # Format: Subject; [credits, grade]
    student_grades["MATH 181"] = [3, 4] # A
    student_grades["MUTG 012"] = [1, 4] # A
    student_grades["MUTH 111"] = [1, 4] # A
    student_grades["CSCI 136"] = [3, 4] # A
    student_grades["CSCI 213"] = [1, 4] # A
    student_grades["CSCI 201"] = [3, 3] # B
    student_grades["ENGW 105"] = [3, 4] # A

    total_credits = 15
    

    Jovan = Student(student_grades, total_credits)

    Jovan.print_grades()
    Jovan.calc_gpa()
    Jovan.print_gpa()






