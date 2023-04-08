label p:
    $ ipad = renpy.input("Введите ip адрес")
    $ ipad = ipad.strip() or "none"
    if ipad == "192.168.102.9":
        "Обмен пакетами с [ipad] по с 32 байтами данных:"
        $ temp1 = renpy.random.randint(100,500)
        $ temp11 = int(temp1)
        "Ответ от [ipad]: число байт=32 время=[temp1] TTL=50"
        $ temp2 = renpy.random.randint(100,500)
        $ temp22 = int(temp2)
        "Ответ от [ipad]: число байт=32 время=[temp2] TTL=50"
        $ temp3 = renpy.random.randint(100,500)
        $ temp33 = int(temp3)
        "Ответ от [ipad]: число байт=32 время=[temp3] TTL=50"
        $ temp4 = renpy.random.randint(100,500)
        $ temp44 = int(temp4)
        "Ответ от [ipad]: число байт=32 время=[temp4] TTL=50"
        "Статистика Ping для [ipad]: Пакетов: отправлено = 4, получено = 4, потеряно = 0 (0\% потерь)"
        $ pingmin = min(temp11, temp22, temp33, temp44)
        $ pingmax = max(temp11, temp22, temp33, temp44)
        $ temp5 = (temp11 + temp22)
        $ temp5 = (temp5 + temp33)
        $ temp5 = (temp5 + temp44)
        $ pingmid = temp5/4
        "Приблизительное время приема-передачи в мс: Минимальное = [pingmin]мсек, Максимальное = [pingmax]мсек, Среднее = [pingmid]мсек"
    elif ipad == "231.235.55.1":
        if q11done:
            $ q12done = True
            $ q1done = True
        "Обмен пакетами с [ipad] по с 32 байтами данных:"
        $ temp1 = renpy.random.randint(100,500)
        $ temp11 = int(temp1)
        "Ответ от [ipad]: число байт=32 время=[temp1] TTL=50"
        $ temp2 = renpy.random.randint(100,500)
        $ temp22 = int(temp2)
        "Ответ от [ipad]: число байт=32 время=[temp2] TTL=50"
        $ temp3 = renpy.random.randint(100,500)
        $ temp33 = int(temp3)
        "Ответ от [ipad]: число байт=32 время=[temp3] TTL=50"
        $ temp4 = renpy.random.randint(100,500)
        $ temp44 = int(temp4)
        "Ответ от [ipad]: число байт=32 время=[temp4] TTL=50"
        "Статистика Ping для [ipad]: Пакетов: отправлено = 4, получено = 4, потеряно = 0 (0\% потерь)"
        $ pingmin = min(temp11, temp22, temp33, temp44)
        $ pingmax = max(temp11, temp22, temp33, temp44)
        $ temp5 = (temp11 + temp22)
        $ temp5 = (temp5 + temp33)
        $ temp5 = (temp5 + temp44)
        $ pingmid = temp5/4
        "Приблизительное время приема-передачи в мс: Минимальное = [pingmin]мсек, Максимальное = [pingmax]мсек, Среднее = [pingmid]мсек"
    else:
        "Обмен пакетами с [ipad] по с 32 байтами данных:"
        "Превышен лимит ожидания для запроса."
        "Превышен лимит ожидания для запроса."
        "Превышен лимит ожидания для запроса."
        "Превышен лимит ожидания для запроса."
        "..."
        "Статистика Ping для [ipad]: Пакетов: отправлено = 4, получено = 0, потеряно = 4 (100\% потерь)"
        jump p
    return 0

label netdis:
    if not q11done:
        $ q11done = True
    "sudo netdiscover"
    "192.168.100.1 08:00:27:3b:8f:ed 1 60 PCS Systemtechnik GmbH
    192.168.102.9 08:00:27:fe:31:e6 1 60 PCS Systemtechnik GmbH
    231.235.55.1 24:11:64:5a:54:e2 1 60 PCS Systemtechnik GmbH"
    return 0

label placeholder:
    
