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
        
        


send_email('проверка связи', 'mmgg@gmail.com')
send_email('привет', 'fan@mail.ru', sender='info@gmail.com')
send_email('hellp', 'student@mail.ru', sender='aaff@mail.uk')
send_email('hi', 'bbb@mail.ru', sender='bbb@mail.ru')


