# datetime
# date, time, datetime, timedelta
from datetime import datetime, date, time, timedelta
import time

# now = datetime.now()
# print("Current date and time:", now)

# print("Year:", now.year)
# print("Month:", now.month)
# print("Hour:", now.hour)
# print("Minute:", now.minute)

# custom_date = date(2024, 12, 25)
# print("Custom Date:", custom_date)

# custom_time = time(15, 30, 45)
# print("Custom Time:", custom_time)

# custom_datetime = datetime(2024, 12, 25, 15, 30, 45)
# print("Custom Datetime:", custom_datetime)

# now = datetime.now()
# formatted_date = now.strftime("%Y/%m/%d")
# formatted_time = now.strftime("%H:%M:%S")
# print(formatted_time)
# print(now.strftime("%A"))
# print(now.strftime("%B"))

# date_string = "2024-12-25 15:30:45"
# parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print("Parsed Datetime:", parsed_date)
# print(type(parsed_date))

# delta1 = timedelta(days=5)
# delta2 = timedelta(hours=2, minutes=30)
# delta3 = timedelta(weeks=1, days=2, hours=3)
# print("Delta 1:", delta1)
# print("Delta 2:", delta2)
# print("Delta 3:", delta3)

# now = datetime.now()

# future_date = now + timedelta(days=5)
# past_date = now - timedelta(days=5)
# print(now)
# print(future_date)
# print(past_date)

# event_date = datetime(2024, 12, 31)
# today = datetime.now()

# difference = event_date - today
# print("Time left:", difference.total_seconds())

# print("Wait for 3 seconds...")
# time.sleep(3)
# print("Done!")

# current_time = time.time()
# print(current_time)
# print(time.ctime(current_time))

start_time = time.time()

for i in range(1000000):
    pass

end_time = time.time()

print("Execution time:", end_time - start_time)