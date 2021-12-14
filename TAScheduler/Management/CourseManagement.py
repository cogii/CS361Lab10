# createCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# editCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTa)
# deleteCourse(courseName)
# populateSearchClass(searchPromp)  should change class to course
# displayAllCourse()
from TAScheduler.models import *


class CourseManagement(object):

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Creates a course
    # Side-effects: Course is created and added inside the database
    # Course Name(in) - Name of the course
    # Course Time(in) - Time of the course
    # Course Days(in) - Days of the course
    # Course Hours(in) - Hours of the course
    # Course Instructor(in) - Instructor of the course
    # Course TA(in) -TA of the course
    @staticmethod
    def createCourse(Id, courseName, courseLocation, courseDays, courseHours, courseInstructor, courseTAs, courseLabs):
        CourseManagement.inputErrorChecker(Id, courseName, courseLocation, courseDays, courseHours, courseInstructor,
                                             courseTAs, courseLabs)

        Course.objects.create(courseID=Id, name=courseName, location=courseLocation,
                              hours=courseHours, days=courseDays, instructor=courseInstructor, TAs=courseTAs,
                              labs=courseLabs)
        return "Course was created"

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Edits a course
    # Side-effects: Course is edited inside the database
    # Course Name(in) - Name of the course
    # Course Time(in) - Time of the course
    # Course Days(in) - Days of the course
    # Course Hours(in) - Hours of the course
    # Course Instructor(in) - Instructor of the course
    # Course TA(in) -TA of the course
    @staticmethod
    def editCourse(Id, courseName, courseLocation, courseDays, courseHours, courseInstructor, courseTAs, courseLabs):
        CourseManagement.inputErrorChecker(Id, courseName, courseLocation, courseDays, courseHours, courseInstructor,
                                             courseTAs, courseLabs)
        if not (Course.objects.filter(courseId=Id).exists()):
            raise TypeError("This course does not exist")

        editedCourse = Course.objects.get(courseId=Id)

        editedCourse.name = courseName
        editedCourse.location = courseLocation
        editedCourse.hours = courseHours
        editedCourse.days = courseDays
        editedCourse.instructor = courseInstructor
        editedCourse.TAs = courseTAs
        editedCourse.labs = courseLabs

        return "The course was successfully edited"

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Deletes a course
    # Side-effects: Course is deleted and removed from the database
    # Course Name(in) - Name of the course
    @staticmethod
    def deleteCourse(Id):
        if not (isinstance(Id, int)):
            raise TypeError("Id entered is not of type int")

        retMsg = "Course has been successfully deleted"
        if not (Course.objects.filter(courseId=Id).exists()):
            retMsg = "This Course being deleted does not exist"
        else:
            Course.objects.filter(courseId=Id).delete()

        return retMsg

    # Preconditions: The user has to have been instantiated
    # The searchPrompt is an existing course assignment name
    # Postconditions: Course assignments are populated
    # Side-effects: None
    # Search Prompt(in): Course Name you are searching for
    @staticmethod
    def populateSearchClass(Id):
        if not (isinstance(Id, int)):
            raise TypeError("Id entered is not of type int")

        if not (Course.objects.filter(courseId=Id).exists()):
            retMsg = "This course being deleted does not exist"
        else:
            retMsg = {
                'Found Course': Course.objects.get(courseId=Id)
            }

        return retMsg

    # Preconditions: The user has to have been instantiated
    # There are courses to display
    # Postconditions: All courses are displayed
    # Side-effects: None
    @staticmethod
    def displayAllCourse():
        allCourses = Course.objects.all()

        data = {
            'All Courses': allCourses
        }

        return allCourses

    @staticmethod
    def inputErrorChecker(Id=0, courseName="", courseLocation="", courseDays="", courseHours="", courseInstructor=None, courseTAs=None,
                            courseLabs=None):
        if not (isinstance(Id, int)):
            raise TypeError("Id entered is not of type int")
        if not (isinstance(courseName, str)):
            raise TypeError("Course name entered is not of type str")
        if not (isinstance(courseLocation, str)):
            raise TypeError("Course location entered is not of type str")
        if not (isinstance(courseDays, str)):
            raise TypeError("Course hours entered is not of type str")
        if not (isinstance(courseHours, str)):
            raise TypeError("Course days entered is not of type str")
        if not(courseInstructor is None):
            if not (isinstance(courseInstructor, UserProfile)):
                raise TypeError("Course instructor entered is not of type User")
            if courseInstructor.userType != "INSTRUCTOR":
                raise TypeError("Course instructor's type is not of type INSTRUCTOR")
        if not(courseTAs is None):
            for TA in courseTAs:
                if not (isinstance(TA, UserProfile)):
                    raise TypeError("Course TA entered is not of type User")
                if TA.userType != "TA":
                    raise TypeError("Course TA's type is not of type TA")
        if not(courseLabs is None):
            for lab in courseLabs:
                if not(isinstance(lab, Lab)):
                    raise TypeError("Course lab entered is not of type Lab")

