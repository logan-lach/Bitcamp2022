import requests
from bs4 import BeautifulSoup

class courseFields:
    sections=[]
    def __init__(self):
        pass

    def fieldGetter(self, courseID):
        url = 'https://api.umd.io/v1/courses/sections?course_id='+courseID
        r = requests.get(url).json()
        self.sections = r

    def profGetter(self):
        instructors = set()
        for i in self.sections:
            instructors.add(i['instructors'][0])
        return instructors

    # def timeGetter(__self__):
    #     timeslots = {}
    #     for i in sections:
    #         timeslots['class'] = {}
    #         meetings = i['meetings']

    #         if len(meetings) == 1:
    #             for j in i['meetings'][0]:

fields420 = courseFields()
fields420.fieldGetter('CMSC420')
print(fields420.profGetter())
