import csv
import os
import time

# majority of code stolen from
# https://github.com/BigchillRK/Zoom-Meeting-and-Recording/blob/master/zoom_record_template1.py
import pyperclip
from pymsgbox import prompt


def join_zoom(meet_id: str, password: str = None):
    zoom = f"zoommtg://zoom.us/join?confno={meet_id}"

    if password:
        pyperclip.copy(password)
        print('')
        print('copied password to clipboard')

    os.system(f'start {zoom}')


def load_details():
    creds = []

    try:
        details = csv.reader(open('details.csv'))
        for detail in details:
            if len(detail) > 0:  # csv saving with a blank line between creds for some reason. oh well.
                creds.append(detail)
    except FileNotFoundError:
        data = prompt(
            text='Please copy paste below the contents from '
                 '"Zoom Meeting Join Details.pdf" sent in an email on 17th April by Mr Brown.',
            title='No teacher Zoom credentials on record')

        for line in data.split('\n'):
            parts = line.split(' ')
            if len(parts) < 3:
                continue
            teacher = ' '.join(parts[0:2])
            password = parts.pop()
            meeting_id = ' '.join(parts[2:])
            meeting_id = meeting_id.replace('-', '').replace(' ', '')
            teacher_last_name = teacher.split(' ')[1]
            creds.append([teacher, meeting_id, password])

        with open('details.csv', mode='w') as details_file:
            details_writer = csv.writer(details_file)
            for cred in creds:
                details_writer.writerow(cred)

    creds = sorted(creds, key=lambda teacher: teacher[0].split(' ')[1])

    teacher_details = []

    for cred in creds:
        teacher_details.append({'teacher': cred[0], 'id': cred[1], 'pword': cred[2]})

    return teacher_details


teacher_details = load_details()

while True:
    for count, teacher in enumerate(teacher_details):
        print(f"{count}: {teacher['teacher']}")
    print("x: to quit")
    print('')
    print('Enter the number of the teacher:')
    teacher = input().lower()
    if teacher == 'x':
        break
    try:
        teacher_i = int(teacher)
    except Exception as e:
        print('must be a number')
        print('')
        print('')
        continue
    my_teacher = teacher_details[teacher_i]
    join_zoom(my_teacher['id'], my_teacher['pword'])
    print('press enter to look up another Zoom meeting to join. Enter X to quit.')
    result = input()
    if result == 'x':
        break
