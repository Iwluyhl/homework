def send_email(messege, recipient, sender = "university.help@gmail.com"):
    variants = (".com", ".ru", ".net")
    if recipient.endswith(variants) and sender.endswith(variants) == 0:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient.count('@') and sender.count('@') == 0:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    elif sender != 'university.help@gmail.com':
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
        
        


send_email('проверка связи', 'vasyok1337@gmail.com')
send_email('привет', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('hellp', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('hi', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


