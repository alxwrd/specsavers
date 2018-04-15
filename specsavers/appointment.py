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
        return f"<Appointment time={self.start_time}>"

    def book(self, details):
        ...


class AppointmentType:
    AdultEyeTest = 2000
    ChildEyeTest = 2001
    ContactLensAfterCare = 2002
    ContactLensTrial = 2003
