# Combine loops and conditionals to classify a 
# list of test scores and student ids into a 
# data structure program and passing and failing
# student ids
# 


#dictionary of student_id--> score
student_score={
    "1": 80,
    "2": 78,
    "3" : 56,
    "4": 43,
    "5": 90,
    "6": 75,
    "7": 89,
    "8": 67
}

MIN_PASSING_SCORE=70

def is_passiing_score(score):
    '''returns the true is the score is passing'''
    return score > MIN_PASSING_SCORE

def build_pass_fail_dictionary(scores):
    '''Build dictionary of passing and failing student id lists'''

    # Initilize a dictionary with passing and listing keys
    # and empty lists for values
    pass_fail_ditionary={       
        "passing":[],
        "failing":[]
    }

    # for each student id, look up its correpsonoding score
    # and evaluate if it is a passing score, if it is a passing
    # append to the passing list, otherwise, append to the failing list

    for student_id in student_score:
        if is_passiing_score(scores[student_id]):
            pass_fail_ditionary["passing"].append(student_id)
        else:
            pass_fail_ditionary["failing"].append(student_id)
    return pass_fail_ditionary

report=build_pass_fail_dictionary(student_score)
print(report)
