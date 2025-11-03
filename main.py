from pyscript import display, document

def calculate(evt=None):  # Accept the event argument
    # INFO
    fname = document.getElementById("fname").value 
    lname = document.getElementById("lname").value

    # GRADES
    math = float(document.getElementById("math").value )
    science = float(document.getElementById("science").value )
    english = float(document.getElementById("english").value )
    filipino = float(document.getElementById("filipino").value )
    pe = float(document.getElementById("pe").value )

    # SUBJECTS UNITS
    subjects = ("Math", "Science", "English", "Filipino", "PE")
    grades = (math, science, english, filipino, pe)
    units = (5, 5, 5, 3, 1)

    # COMBINE
    sub1, sub2, sub3, sub4, sub5 = subjects
    grade1, grade2, grade3, grade4, grade5 = grades
    unit1, unit2, unit3, unit4, unit5 = units

    # DISPLAY
    display(f"{fname} {lname}'s Grades:", target='output')
    display(f"{sub1} ({unit1} units): {grade1}", target='output')
    display(f"{sub2} ({unit2} units): {grade2}", target='output')
    display(f"{sub3} ({unit3} units): {grade3}", target='output')
    display(f"{sub4} ({unit4} units): {grade4}", target='output')
    display(f"{sub5} ({unit5} units): {grade5}", target='output')

    # GWA
    weighted_sum = grade1*unit1 + grade2*unit2 + grade3*unit3 + grade4*unit4 + grade5*unit5
    total_units = unit1 + unit2 + unit3 + unit4 + unit5
    gwa = weighted_sum / total_units

    display(f"General Weighted Average (GWA): {gwa:.2f}", target='output')
