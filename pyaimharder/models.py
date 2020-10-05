import json
from datetime import datetime

from six.moves.urllib import parse


class BookPlan:
    def __init__(self, day, timeid):
        self.day = day
        self.timeid = timeid

    @property
    def bookable(self):
        todays_weekday = datetime.now().weekday()
        return abs(self.day - todays_weekday) <= 3  # days in advance


class DaySchedule:
    def __init__(self, day, timetable, bookings, **kwargs):
        self.day = day
        self.classes = [Class.from_resp(day, booking) for booking in bookings]

    @classmethod
    def from_resp(cls, resp):
        resp_json = resp.json()
        resp_json["day"] = datetime.strptime(
            parse.parse_qs(resp.url)["day"].pop(), "%Y%m%d"
        )
        return cls(**resp_json)

    def __repr__(self):
        return json.dumps(self.__dict__, sort_keys=True, default=str)


class Class:
    def __init__(self, class_id, day, time, max_people, booked_people, coach_name):
        # time cast to timestamp from "time" (07:00 - 08:00)
        # booked_people == ocupation (cast to int)
        # max_people == limit (cast to int)
        # coach_name == coachName
        self.class_id = class_id
        parsed_start_time = time.split("-")[0].strip().split(":")
        self.time = time
        self.datetime_time = day.replace(
            hour=int(parsed_start_time[0]), minute=int(parsed_start_time[1])
        )
        self.max_people = max_people
        self.booked_people = booked_people
        self.coach_name = coach_name

    @property
    def bookable(self):
        todays_weekday = datetime.now().weekday()
        self.datetime_time.weekday()
        return not self.full and (
            abs(self.datetime_time.weekday() - todays_weekday) <= 3
        )  # days in advance

    @property
    def full(self):
        return self.max_people <= self.booked_people

    @classmethod
    def from_resp(cls, day, resp):
        return cls(
            class_id=resp["id"],
            day=day,
            time=resp["time"],
            max_people=resp["limit"],
            booked_people=resp["ocupation"],
            coach_name=resp["coachName"],
        )

    def __repr__(self):
        return json.dumps(self.__dict__, sort_keys=True, default=str)
