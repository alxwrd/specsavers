import maya
import specsavers

from specsavers.api import Api


class Appointment:
    api = Api

    def __init__(self, id_, start_time, end_time):
        self.id = id_
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        datetime = self.start_time.datetime()

        return "<Appointment date='{date}', time='{time}'>".format(
                date=datetime.strftime("%b %d"),
                time=datetime.strftime("%H:%M"))

    def book(self, details):
        ...


class AppointmentType:
    AdultEyeTest = 2000
    ChildEyeTest = 2001
    ContactLensAfterCare = 2002
    ContactLensTrial = 2003
