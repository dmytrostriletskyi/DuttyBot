def display_schedule(lessons):
    if len(lessons) == 0:
        return 'Пары отсутствуют.'

    result = ''
    for lesson in lessons:
        output = '{0} пара | {1}  | {2} — {3}\n'.format(lesson['lesson_order'], lesson['lesson_classroom'],
                                                        lesson['lesson_title'], lesson['lesson_teacher'])
        result += output

    return result
