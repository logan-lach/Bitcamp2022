from planetterp_data import *
from testudo import profGetter
import pickle
from generate_rmp_data import RateMyProfScraper

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






if __name__ == "__main__":
    """
    Algorithm Idea:
    
    Read input for required classes
    Read input for departments you'd like to take extra classes in (And how much)
    
    Example input:
        Which classes are you required to take next semester?:
            CMSC420
            (Later, check if they are valid course codes)
        What other classes would you like to take?
            CMSC, 1
            MATH, 1
            HIST, 2
            
    We'll rank in given order. 
    Let's get the best classes for our required classes now. 
    
    """

    required = []
    user_input = None
    while user_input != "Done":
        user_input = input("Enter which classes you are required to take next semester (Enter 'Done' when finished): ")
        required.append(user_input)

    required.pop()
    extra = []
    user_input = None
    while True:
        user_input = input("Enter the department you'd like to take electives in (Enter 'Done' when finished): ")
        if user_input == "Done":
            break
        amt = input("Enter the amount of courses you'd like to take in this department")
        extra.append((user_input, amt))

    for r_class in required:
        print(rank_prof_per_class(r_class))




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



