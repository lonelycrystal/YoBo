screen dkda():
    imagebutton:
        xalign 0.87 yalign 0
        idle "dk3"
        hover "dk3"
        action Function(renpy.call, label="dk")

screen blocknote():
    imagebutton:
        xalign 0.99 yalign 0
        idle "blocknote"
        hover "blocknote"
        action Function(renpy.call, label="helpnote")

label dk:
    "Добро пожаловать на доску заданий"
    "Тут вы можете следить за выполнением заданий"
    menu:
        "Доска заданий"
        "Задание 1":
            "1. Провести сканирование сети на доступные подключения"
            "2. Проверить доступ к третьему IP-адресу в команде netdiscover"
            if went1:
                "Состояние: Выполнено"
                if zad1done:
                    menu:
                        "Повторить историю?"
                        "Давай":
                            jump home2
                        "Нет, спасибо":
                            jump dk
                else:
                    menu:
                        "Продолжить историю?"
                        "Давай":
                            jump home2
                        "Погоди, ещё есть дела":
                            jump dk
            else:
                "Состояние: Не выполнено"
            jump dk
        "Вернуться":
            jump posled
    if not zad1done:
        "..."
    else:
        menu:
            "Задание 2":
                "Пока нет задания"
                jump dk
            "Задание 3":
                "Пока нет задания"
                jump dk
            "Задание 4":
                "Пока нет задания"
                jump dk
            "Задание 5":
                "Пока нет задания"
                jump dk



label helpnote:
    "Добро пожаловать в гайд по командам"
    menu:
        "Выберете интересующую вас команду"
        "netping":
            "Команда netping помогает проверить соединение с сервером"
            "Синтаксис: sudo netping"
            jump helpnote

        "netdiscover":
            "Команда netdiscover помогает выполнить сканирование локальной сети, показать все доступные устройства и их IP-Адреса"
            "Синтаксис: sudo netdiscover"
            jump helpnote

        "Вернуться":
            return
