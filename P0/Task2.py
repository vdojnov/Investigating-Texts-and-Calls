"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
unique_nums = []
time_on_phone = {}

for call in calls:
    if call[0] not in unique_nums:
        unique_nums.append(call[0])
        time_on_phone[call[0]] = int(call[3])
    else:
        time_on_phone[call[0]] += int(call[3])

    if call[1] not in unique_nums:
        unique_nums.append(call[1])
        time_on_phone[call[1]] = int(call[3])
    else:
        time_on_phone[call[1]] += int(call[3])

max_time = 0
telephone = ''
for number in time_on_phone:
    if max_time < int(time_on_phone[number]):
        max_time = time_on_phone[number]
        telephone = number

phrase = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone, max_time)
print(phrase)


