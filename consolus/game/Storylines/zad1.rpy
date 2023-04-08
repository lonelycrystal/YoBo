label home2:
    gg "Слушай, ну это всё, конечно, хорошо"
    gg "Но я до сих пор не понимаю, зачем мне проверять соединение"
    L "Всё просто. Перед тем, как взаимодействовать с удаленным сервером, надо проверить соединение"
    L "Не будет соединения - не сможем ничего сделать"
    gg "А, ну понятно. Давай тогда дальше пойдем. Раньше начнем - раньше я получу деньги"
    L "Не торопись, малой. Отдохни маленько, обдумай всё перед сном. Отоспишься, заходи снова"
    gg "Ну ладно, ладно. Отосплюсь немного."
    scene home light
    with dissolve
    hide screen dkda
    with dissolve
    hide screen blocknote
    with dissolve
    pause 2
    play homefx2 "audio/Sounds/disappear.mp3" noloop
    scene home door
    with dissolve
    pause 2
    scene black fon
    with irisin
    pause 4
    scene home door
    with dissolve
    pause 2
    play homefx2 "audio/Sounds/lightswitch.mp3" noloop
    scene flashbang
    pause 1
    play homefx2 "audio/Sounds/laydivan.mp3" noloop
    scene page1
    with dissolve
    gg "Галья, музыку"
    play galina "audio/Voice/losOS/sdelano.mp3" noloop
    queue music ['audio/Music/consolus1.mp3', 'audio/Music/consolus2.mp3', 'audio/Music/consolus3.mp3'] loop
    gala "Сделано, сэр"
    L "Ну здравствуй, [name]. Выспался, надеюсь"
    menu:
        "Выберите ответ"
        "Да, вполне":
            gg "Вполне выспался, кофейка уже заварил"
            L "Это хорошо, так как сейчас начнется самая жесть"
        "Неособо":
            gg "Соседи всю ночь сверлили, спать не давали"
            L "Это печально, так как сейчас начнется самая жесть"
    L "Постепенно продвигаемся по пути изучения уязвимостей сетей wifi"
    gg "Так, погоди, это незаконно или я что-то не понял?"
    L "По сути, да. Но по факту, мы будем работать, чтобы показать компаниям уязвимости их сетей"
    gg2 "А я хотел спокойной жизни, без заморочек"
    gg "Ну ладно, ладно, давай приступать уже"
    L "Итак, перед тобой сейчас находится командная строка операционной системы Kali Linux"
    gg "Хорошо, пока всё понятно"
    L "Не радуйся сильно. Тебе нужно будет запомнить кучу команд, для дальнейшей работы"
    L "Рекомендую взять блокнотик, ручку, всё постепенно записывать"
    gg "Хорошо, погоди секунду"
    play homefx2 "audio/Sounds/collectitem.mp3" noloop
    "..."
    gg "Так, я готов"
    L "Итак, продолжим"
    L "На чём мы остановились? Ах да..."
    L "Перед тобой находится командная строка Kali Linux"
    L "Kali Linux - по сути операционка для хакеров"
    L "Многие вещи, необходимые в нашем деле уже предустановлены"
    L "Хотя, некоторые утилиты надо будет устанавливать ручками"
    L "Итак, приступим к работе"
    L "Я думаю, ты уже устал каждый раз прописывать sudo перед каждой командой. Давай исправим это"
    L "Надо перевести командную строку в режим администратора"
    L "Для этого просто нужно ввести sudo su"

label sudosu:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "sudo su":
        "Команда введена неверно"
        jump sudosu
    scene page2
    with dissolve
    "..."
    L "Итак, мы стали администратором. Поздравляю."
    gg "Что делать дальше?"
    L "Дальше давай займемся переводом роутера в режим анализа сетей"
    L "Для этого для начала надо установить утилиту aircrack"
    L "Всё довольно просто. Нужно ввести команду apt-get install aircrack-ng"

label aircrack:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "apt-get install aircrack-ng":
        "Команда введена неверно"
        jump aircrack
    scene page3
    with dissolve
    pause 1
    scene page4
    with dissolve

    L "Отлично, утилита установлена"
    gg "Я надеюсь, осталось немного работы"
    L "Надейся, надейся..."
    L "Дальше давай проверим устройства сети, которые у тебя есть, чтобы понять, с чем мы будем работать"
    L "Для этого пропиши команду iwconfig"

label iwconfig:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "iwconfig":
        "Команда введена неверно"
        jump iwconfig
    scene page411
    with dissolve
    pause 1
    scene page5
    with dissolve

    L "Итак, ты можешь видеть свой wifi-адаптер и ещё парочку неактивных сетевых"
    L "Запомни название активного и введи команду airmon-ng start *Название адаптера*"
    L "Название адаптеров находятся слева"
    gg2 "Ну тут точно надо записать, так просто не запомнить"

label airmon1:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "airmon-ng start wlp1s0":
        "Команда введена неверно"
        jump airmon1
    scene page6
    with dissolve
    pause 1
    scene page7
    with dissolve

    L "Как ты можешь видеть, теперь наш адаптер был переведен в режим мониторинга сети"
    L "Собственно, сейчас мы и займемся мониторингом"
    L "Пропиши ещё раз команду iwconfig, чтобы узнать текущее название wifi-устройства"

label iwconfig2:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "iwconfig":
        "Команда введена неверно"
        jump iwconfig2
    scene page8
    with dissolve
    pause 1
    scene page9
    with dissolve

    L "Итак, название адаптера немного изменилось, это надо будет учитывать в дальнейшем"
    L "Следующей командой будет запуск самого мониторинга"
    L "Записывается она так: airodump-ng *Название адаптера*"

label dumbp:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "airodump-ng wlp1s0mon":
        "Команда введена неверно"
        jump dumbp
    scene page10
    with dissolve
    pause 1
    scene page12
    with dissolve

    L "Отлично. Твой адаптер просканировал сеть на WIFI - сети"
    L "Специально для тебя я создал точку, чтобы ты практиковался. Называется LonelyDragon (Увидеть это можно в столбике ESSID)"
    L "Следующая команда будет ОЧЕНЬ сложная"
    L "Советую тебе записать её, или сделать скриншот/фотографию"
    L "Как только ты введешь команду, твой адаптер начнет перехватывать \"Фреймы\" или запросы"
    L "Я отправлю около 17 тысяч фреймов, чтобы создать видимость использования сети"
    L "Команда звучит так: airodump-ng --bssid *Данные из столбика BSSID* --essid *Данные из столбика ESSID* -c *Номер канала(столбик CH)* -w /tempo/lonel *Название адаптера*"

label airobomzh:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "airodump-ng --bssid F2:B7:FE:1C:DF:C4 --essid LonelyDragon -c 1 -w /tempo/lonel wlp1s0mon":
        "Команда введена неверно"
        jump airobomzh
    scene page13
    with dissolve
    pause 1
    scene page14
    with dissolve

    L "Вот мы и закончили с мониторингом"
    L "Дальше остается только расшифровать данные"
    L "В этом нам поможет утилита wireshark"
    L "Тут всё просто. Пропиши в консоль apt-get install wireshark"

label wireshark:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "apt-get install wireshark":
        "Команда введена неверно"
        jump wireshark
    scene page16
    with dissolve
    pause 1
    scene page17
    with dissolve

    L "Дальше просто пропиши wireshark в консоль, чтобы запустить её"

label wireshark2:
    $ commline = renpy.input("Введите команду")
    $ commline = commline.strip() or "chumba"
    if not commline == "wireshark":
        "Команда введена неверно"
        jump wireshark2
    scene page18
    with dissolve
    pause 1
    scene page19
    with dissolve

    L "Итак, добро пожаловать в WireShark"
    L "Не пугайся интерфейса, всё не так сложно"
    gg "Ага, не сложно... Знаю я твоё не сложно"
    L "Нет, ну правда. Пару кнопок нажать и всё"
    gg "Ладно, ладно, верю"
    L "Итак, для начала зайдем в параметры, поменяем настройки расшифровки"
    "..."
    pause 0.5
    scene page20

    L "Дальше жми редактировать и пиши в правой колонке пароль, логин от сети(должно будет получиться 12345678:LonelyDragon)"
    "..."
    pause 0.5
    scene page21

    L "Отлично, можешь закрывать это безобразие"
    pause 0.5
    scene page22

    L "Уже практически закончили. Сейчас перед тобой находится список пакетов, которые были переданы внутри сети"
    L "Просто ради интереса можно прописать в фильтр DNS, чтобы увидеть только фреймы от сайтов по протоколу DNS"
    pause 0.5
    scene page23

    L "Вот мы и закончили краткий курс по анализу простых уязвимостей"
    L "Давай вернемся назад и продолжим изучение разнообразных вещей"
    play sound "audio/Sounds/questup.mp3" noloop
    dkzadan "Ветка 1 закончена. Проверьте доску заданий"
    $ zad1done = True
    jump posled
    jump beta
