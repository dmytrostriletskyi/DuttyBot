from additional_data import faculty_list
import telebot


class Keyboard:
    def __init__(self, bot):
        self.bot = bot

    def get_all_faculties(self, message):
        faculty_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        faculty_markup.row('Вернуться назад')
        for faculty in faculty_list:
            faculty_markup.row(faculty)
        self.bot.send_message(message.from_user.id, 'Выберите факультет:', reply_markup=faculty_markup)

    def stable_six_courses(self, message):
        course_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        course_markup.row('Вернуться назад')
        course_markup.row('1 курс', '4 курс')
        course_markup.row('2 курс', '5 курс')
        course_markup.row('3 курс', '6 курс')
        self.bot.send_message(message.from_user.id, 'Выберите курс:', reply_markup=course_markup)

    def stable_one_course(self, message):
        course_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        course_markup.row('Вернуться назад')
        course_markup.row('1 курс')
        self.bot.send_message(message.from_user.id, 'Выберите курс:', reply_markup=course_markup)

    def stable_three_courses(self, message):
        course_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        course_markup.row('Вернуться назад')
        course_markup.row('3 курс')
        course_markup.row('6 курс')
        course_markup.row('7 курс')
        self.bot.send_message(message.from_user.id, 'Выберите курс:', reply_markup=course_markup)

    def group_list_by_faculty_and_group(self, groups_list, message):
        length = len(groups_list)
        edge = (length + 1) // 2
        length -= 1

        group_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        group_markup.row('Вернуться назад')
        for i in range(0, edge):
            if groups_list[i] == groups_list[length - i]:
                group_markup.row(groups_list[i])
                break
            group_markup.row(groups_list[i], groups_list[length - i])
        self.bot.send_message(message.from_user.id, 'Выберите группу:', reply_markup=group_markup)

    def get_schedule(self, message):
        date_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        date_markup.row("На сегодня", "На завтра")
        date_markup.row('Подписаться на эту группу')
        date_markup.row('Главное меню', 'Вернуться назад')
        self.bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=date_markup)

    def main_menu(self, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Получить расписание")
        user_markup.row("Получить расписание по подписке")
        user_markup.row("Время пар")
        user_markup.row('Обновления', 'Обратная связь')
        self.bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)
