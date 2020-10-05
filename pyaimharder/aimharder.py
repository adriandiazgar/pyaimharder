import calendar
from datetime import datetime, timedelta

import requests
from more_itertools import always_iterable, first

from models import DaySchedule, BookPlan
from pyaimharder import settings


class BookingError(Exception):
    pass


class AimHarder:
    def __init__(self, email, password, box_name):
        self.session = requests.Session()
        self.email = email
        self.password = password
        settings.set_box(box_name)
        # self.login()
        self.cookies = None

    def login(self):
        resp = self.session.post(
            settings.LOGIN,
            data={"login": "Log in", "mail": self.email, "pw": self.password},
        )
        self.cookies = resp.cookies
        resp.raise_for_status()

    def get_classes_for_day(self, day):
        target_day = self.__get_target_day(day)
        resp = self.session.get(
            settings.CLASSES,
            params={"day": target_day, "familyId": "", "box": settings.BOX_ID},
        )
        return DaySchedule.from_resp(resp)

    def __get_target_day(self, day):
        return day.strftime("%Y%m%d")

    def book_class(self, _class):
        """
        Book a class, when booking success the response contains
        "bookState":
            - OK: 1
            - Already booked: -12
            - Not found: -2
        :param _class: class obejct
        :type _class: Class
        :return:
        :raises BookingError:
        """
        if not _class.bookable:
            raise BookingError(
                "Class is not yet bookable, only books with 3 days in advance are accepted"
            )
        if not _class.full:
            raise BookingError(
                "Class is full!! max: {}, booked: {}".format(
                    _class.max_people, _class.booked_people
                )
            )

        target_day = self.__get_target_day(_class.datetime_time)

        response = self.session.post(
            settings.BOOK,
            data={
                "id": _class.class_id,
                "day": target_day,
                "insist": 0,
                "familiId": "",
            },
        )

        if response.status_code == 200 and response.json()["bookState"] == 1:
            print(
                "Session booked for {} on {} at {}".format(
                    self.email, target_day, _class.time
                )
            )
        else:
            print(
                "Found a matching session for {} on {} but something went wrong".format(
                    self.email, target_day
                )
            )
            raise BookingError("Error while booking: {}".format(response.json()))

    def get_class_by_weekday_and_time(self, weekday, time):
        target_date = datetime.today() + timedelta(days=weekday % 7)
        dayplan = self.get_classes_for_day(target_date)
        return first(always_iterable(filter(lambda c: c.time == time, dayplan.classes)))

    def process_book_list(self, books_plan_list):
        "Process only nex 3 days!!"
        for book_plan in books_plan_list:
            if (
                book_plan.bookable
                and abs(book_plan.day - datetime.now().weekday()) == 3
            ):  # Book only 3 days in advance
                _class = self.get_class_by_weekday_and_time(
                    book_plan.day, book_plan.timeid
                )
                if _class:
                    self.book_class(_class)
                else:
                    BookingError("Class not found!")


if __name__ == "__main__":
    pass
    # Example ussage
    # client = AimHarder(
    #     email="email@youremail.com", password="yourpassword", box_name="castelldefels"
    # )
    # classes = client.get_classes_for_day(day=datetime.today() + timedelta(days=3))
    # books_plan_list = [
    #     BookPlan(day=calendar.MONDAY, timeid="07:00 - 08:00"),
    #     BookPlan(day=calendar.TUESDAY, timeid="07:00 - 08:00"),
    #     BookPlan(day=calendar.WEDNESDAY, timeid="07:00 - 08:00"),
    #     BookPlan(day=calendar.THURSDAY, timeid="07:00 - 08:00"),
    #     BookPlan(day=calendar.FRIDAY, timeid="07:00 - 08:00"),
    #     BookPlan(day=calendar.SATURDAY, timeid="07:00 - 08:00"),
    #     BookPlan(day=calendar.SUNDAY, timeid="07:00 - 08:00"),
    # ]
    # client.process_book_list(books_plan_list)
