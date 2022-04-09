from .planetterp_data import *

def rank_prof_per_class(courseID, courseNumber):



def rank_classes_per_dept(deptID, requirements=None, amount):

    all_courses = courses(deptID)


    """
    for all classes offered:
        get best prof for class
        return max
    
    """


    """

    Algorithm:

    1.) Class Rating (Average GPA)
        - Average > 2.8: 1.5
        - 2.8 > Average > 2.5: 0
        - Average < 2.5: -1.5
    2.) Professor Rating
        - Factors
            - Number of Reviews
            - Overall Rating
            - Rating Class
            - Potential Sentiment Analysis?
        2 lists

        Professor Rating Formula returns int:
            1.) ((planetterp_rating - 3.0) * (# from planetterp/# total) + (rmp_rating - 3.0) * (# from rmp/ # total)) + (# total reviews
            2.) Get rid of 3.0 value
            ((Number of Reviews * .10) * abs(3.0-professor_rating)) +
    3.) Building
        - Factors
            - Distance from classes


    """



