from tkinter.tix import DisplayStyle
import requests
from bs4 import BeautifulSoup


def fieldGetter(courseID):
    url = 'https://api.umd.io/v1/courses/sections?course_id='+courseID
    sections = requests.get(url).json()
    return sections

def profGetter(courseID):
    sections = fieldGetter(courseID)
    instructors = set()
    for i in sections:
        instructors.add(i['instructors'][0])
    return instructors

# def timeGetter(__self__):
#     timeslots = {}
#     for i in sections:
#         timeslots['class'] = {}
#         meetings = i['meetings']

#         if len(meetings) == 1:
#             for j in i['meetings'][0]:

print(profGetter('CMSC131'))

