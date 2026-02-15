class WeekDayError(Exception):
    pass


class Weeker:
    __weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day_of_week):
        if day_of_week not in self.__weeks:
            raise WeekDayError('sorry i can serve you request')
        self.__day_of_week = day_of_week

    def add_days(self, n):
        current_day = self.__weeks.index(self.__day_of_week)
        next_day = current_day
        for elt in range(n):
            next_day +=  1

            if next_day > 6:
                next_day = 0
        self.__day_of_week = self.__weeks[next_day]

    def subtract_days(self, n):
        current_day = self.__weeks.index(self.__day_of_week)
        previous_day = current_day
        for elt in range(n):
            previous_day -= 1
            if previous_day < 0:
                previous_day = 6
        self.__day_of_week = self.__weeks[previous_day]
        
    def __str__(self):
        return self.__day_of_week

    
if __name__ == '__main__':
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")

# Expected output

# Mon
# Tue
# Sun
# Sorry, I can't serve your request.