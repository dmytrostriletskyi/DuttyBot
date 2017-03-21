def message_handler_groups(bot, position, keyboard):
    @bot.message_handler(func=lambda mess: 'БСЗ-31' == mess.text or 'УБЗ-31' == mess.text or 'СТЗ-31' == mess.text or
                         'БСЗМ-61' == mess.text or 'ІМЗМ-61' == mess.text or 'ІМЗС-61' == mess.text or
                         'КСЗМ-61' == mess.text or 'СТЗМ-61' == mess.text or 'УБЗМ-61' == mess.text or
                         'ТСЗС-61' == mess.text or 'СЗЗМ-61' == mess.text or 'РТЗМ-61' == mess.text or
                         'РТЗМ-62' == mess.text or 'ІМЗМ-2015-1' == mess.text or 'БСЗМ-2015-1' == mess.text or
                         'КСЗМ-2015-1' == mess.text or 'МНЗМ-2015-1' == mess.text or 'РТЗМ-2015-1' == mess.text or
                         'УБЗМ-2015-1' == mess.text or 'УІД -2015-1 -З' == mess.text or 'ТСЗМ-2015-1' == mess.text or
                         'СЗЗМ-2015-1' == mess.text or 'РТЗМ-2015-2' == mess.text or 'ТСЗ-32' == mess.text or
                         'ІМД-32' == mess.text or 'ТСД-32' == mess.text or 'ТСД-43' == mess.text or
                         'БСД-41' == mess.text or 'СЗД-41' == mess.text or 'УБД-41' == mess.text or
                         'ІМД-41' == mess.text or 'КСД-41' == mess.text or 'ТСД-41' == mess.text or
                         'МНД-21' == mess.text or 'РТД-41' == mess.text or 'ТСДМ-61' == mess.text or
                         'АКБД-11' == mess.text or 'АКБЗ-11' == mess.text or 'МНД-41' == mess.text or
                         'ТСД-42' == mess.text or 'СТД-41' == mess.text or 'ІМД-42' == mess.text or
                         'КСД-42' == mess.text or 'ІМД-43' == mess.text or 'КСД-32' == mess.text or
                         'БСД-42' == mess.text or 'ПУД-11' == mess.text or 'АКСД-11' == mess.text or
                         'БСД-31' == mess.text or 'КСДМ-61' == mess.text or 'СЗД-31' == mess.text or
                         'УБД-31' == mess.text or 'КСД-31' == mess.text or 'ІМД-31' == mess.text or
                         'ТСД-31' == mess.text or 'РТД-31' == mess.text or 'АКСЗ-11' == mess.text or
                         'СТД-31' == mess.text or 'ІМД-21' == mess.text or 'МНД-31' == mess.text or
                         'РТД-42' == mess.text or 'МНД-11' == mess.text or 'ІМД-22' == mess.text or
                         'АМНД-11' == mess.text or 'АМНЗ-11' == mess.text or 'АІКД-11' == mess.text or
                         'АІКЗ-11' == mess.text or 'АСТД-11' == mess.text or 'БСД-21' == mess.text or
                         'СЗД-21' == mess.text or 'УБД-21' == mess.text or 'БСДМ-61' == mess.text or
                         'СЗДМП-61' == mess.text or 'УБДМП-61' == mess.text or 'КСД-21' == mess.text or
                         'КСД-22' == mess.text or 'ІМДМ-61' == mess.text or 'ТСД-21' == mess.text or
                         'ТСД-22' == mess.text or 'РТД-21' == mess.text or 'РТДМ-61' == mess.text or
                         'СТД-21' == mess.text or 'МНДМ-61' == mess.text or 'РТДМ-62' == mess.text or
                         'СТД-11' == mess.text or 'УІДМ-61' == mess.text or 'ДЗД-11' == mess.text or
                         'АСП-15-2' == mess.text or 'ДЗД-21' == mess.text or 'РАД-21' == mess.text or
                         'БСД-22' == mess.text or 'ПД-12' == mess.text or 'ПД-21' == mess.text or
                         'ПД-31' == mess.text or 'ТСД-33' == mess.text or 'БСД-32' == mess.text or
                         'ПД-22' == mess.text or 'РАД-31' == mess.text or 'ДЗД-31' == mess.text or
                         'ТСДМ-62' == mess.text or 'БСД-11' == mess.text or 'БСД-12' == mess.text or
                         'СЗД-11' == mess.text or 'УБД-11' == mess.text or 'ТСД-13' == mess.text or
                         'ТСД-15' == mess.text or 'ТСД-11' == mess.text or 'ТСД-14' == mess.text or
                         'ТСД-16' == mess.text or 'ТСД-17' == mess.text or 'АЗД-11' == mess.text or
                         'УБДМ-51' == mess.text or 'МНДМ-51' == mess.text or 'СЗДМ-51' == mess.text or
                         'ПД-11' == mess.text or 'КНД-11' == mess.text or 'ІCД-11' == mess.text or
                         'КІД-11' == mess.text or 'САД-11' == mess.text or 'БСДМ-51' == mess.text or
                         'СТДМ-51' == mess.text or 'РТДМ-52' == mess.text or 'ІМДМ-51' == mess.text or
                         'ТСД-12' == mess.text or 'КІД-12' == mess.text or 'ІМДМ-52' == mess.text or
                         'КСДМ-51' == mess.text or 'КСДМ-52' == mess.text or 'РТДМ-51' == mess.text or
                         'ТСДМ-51' == mess.text or 'ТСДМ-52' == mess.text or 'МРД-11' == mess.text or
                         'МРД-21' == mess.text or 'ПТБ-11' == mess.text or 'САД-21' == mess.text or
                         'КНД-21' == mess.text or 'ІCД-21' == mess.text or 'ПУД-21' == mess.text or
                         'ПТБ-21' == mess.text or 'ТБМ-11' == mess.text or 'БСД-13' == mess.text or
                         'БСД-14' == mess.text, content_types=['text'])
    def getSelectedGroup(message):
        position.set_group_position(str(message.chat.id), message.text)
        return keyboard.get_schedule(message)