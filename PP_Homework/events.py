from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def description(self):
        return f"{self.name} on {self.date}"

    @abstractmethod
    def is_event_on_holiday(self):
        pass

class ThanksgivingEvent(Event):
    def is_event_on_holiday(self):
        return True

class RegularEvent(Event):
    def is_event_on_holiday(self):
        return False

thanksgiving_party = ThanksgivingEvent("Thanksgiving Party", "November 25")
programming_class = RegularEvent("Programming Class", "November 26")

print(thanksgiving_party.description())
print(f"Is the {thanksgiving_party.name} on a holiday? {thanksgiving_party.is_event_on_holiday()}")
print(programming_class.description())
print(f"Is the {programming_class.name} on a holiday? {programming_class.is_event_on_holiday()}")
