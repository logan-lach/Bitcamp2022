from .planetterp_data import *
from .testudo import profGetter

rmp_data = pickle.load(open("rmp_object.obj", "rb" ))

def rank_prof_per_class(courseID):

    available_profs = []
    for item in profGetter(courseID):
        if courseNumber == item['course_number']:
            available_profs = item['professors']
            break

    values = []
    for prof in available_profs:
        prof_rmp_rating = rmp_data.SearchProfessor(prof)
        prof_pt_rating = professor(prof, ratings=True)
        total_reviews = prof_rmp_rating['tNumRatings'] + len(prof_pt_rating['ratings'])
        value = ((prof_rmp_rating['overall_rating'] - 3.0) * (prof_rmp_rating['tNumRatings']/total_reviews) + (prof_pt_rating['average_rating']-3.0) * (len(prof_pt_rating['ratings'])/total_reviews))
        values.append((value, prof))

    return sorted(values)





def rank_classes_per_dept(deptID):

    rankings = []
    for item in courses(deptID):
        ranking = rank_prof_per_class(deptID + item['course_number'])
        rankings.append((item['course_number'], rank_prof_per_class(deptID + item['course_number'])))








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



