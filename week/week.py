import calendar
import time

def animate_calendar(year, month):
  """Animates a calendar for the given year and month."""
  for day in range(1, calendar.monthrange(year, month)[1] + 1):
    print(calendar.day_abbr[calendar.weekday(year, month, day)])
    time.sleep(1)

if __name__ == "__main__":
  year = 2023
  month = 7
  animate_calendar(year, month)
