# coding=utf-8
import urllib
from bs4 import BeautifulSoup

class CrawlSplan:
    Base_URL = 'https://campus.verwaltung.uni-tuebingen.de/lsfpublic/rds?state=wsearchv&search=1&subdir=veranstaltung&treetype_einrichtung.eid=2&alias_pord.pordnr=r_zuordpos.pordnr&einrichtung.eid=641%2C642%2C666&expand_einrichtung.eid=y&veranstaltung.semester=20172&alias_pord.pordnr=r_zuordpos.pordnr&P_start=0&P_anzahl=500&P.sort=&_form=display'

    def get_courses(self):
        i = 0
        BaseURLHtml = urllib.urlopen(self.Base_URL)
        soup = BeautifulSoup(BaseURLHtml.read(), 'html.parser')
        for tableRow in soup.find_all(class_='regular'):
            if tableRow.string != 'mittel' and tableRow.string != 'lang':
                name = tableRow['title']
                course = Courses(tableRow['href'], name, '', '', '', '', '')
                course_html = BeautifulSoup(urllib.urlopen(tableRow['href']), 'html.parser')
                for basic_n_mod in course_html.findAll(class_="mod_n_basic"):
                    if 'basic_5' in basic_n_mod['headers']:
                        course.semester = basic_n_mod.string
                    elif 'basic_6' in basic_n_mod['headers']:
                        course.sws = basic_n_mod.string
                    elif 'basic_12' in basic_n_mod['headers']:
                        course.comment = basic_n_mod.string
                    elif 'basic_3' in basic_n_mod['headers']:
                        course.number = basic_n_mod.string

                tbody = course_html.findAll('table', summary="Übersicht über alle Veranstaltungstermine")
                for td in tbody.find_all('td'):
                    print td

                print tbodies.tr

                Courses.add_course(course)
                i += 1
                print repr(i) + " TableRow " + tableRow['href']

    def get_course_data(self, courseHTML):

        return ''

    def print_data(self):
        print self.CourseData


class Courses:
    CourseList = []

    def __init__(self, url_link, name, semester, comment, sws, time, number):
        self.TimeSchedule = []
        self.urllink = url_link
        self.name = name
        self.semester = semester
        self.comment = comment
        self.sws = sws
        self.time = time
        self.course_number = number
        self.add_course()

    def add_course(self):
        self.CourseList.append(self)

    def add_Time(self, time):
        self.TimeSchedule.append(self, time)


class Time:

    def __init__(self, day, time, rythm, room):
        self.day = day
        self.time = time
        self.rythm = rythm
        self.room = room

if __name__ == '__main__':
    crawler = CrawlSplan()
    crawler.get_courses()
