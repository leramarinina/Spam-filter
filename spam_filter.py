import re
triggers_spam = [r'(М|м)ой дорогой друг', r'Только сегодня!', r'((П|п)ришли(те)?|(П|п)ереведи(те)?) (деньги|сумму|\d+)', r'!!', r'много зараб', r'([А-ЯЁ]+(\s|\.|\!|\?)){2,}', r'(Д|д)елаем деньги',
                 r'(Н|н)е упусти(те)?', r'Для завершения регистрации', r'Ссылка действительна']
triggers_normal = [r'(Здравствуй(те)?)|(Добрый (день|вечер))|(Привет)', r'С уважением']

name_file = input('Введите путь к файлу ')
with open(name_file, encoding = 'utf8') as file:
    email = file.read()

    spam_count = 0
    for trigger in triggers_spam:
        if len(re.findall(trigger, email)) != 0:
            print(re.findall(trigger, email))
            spam_count += 1
    for trigger in triggers_normal:
        if len(re.findall(trigger, email)) != 0:
            spam_count -= 1
    print(spam_count)
    if spam_count >= 0 and spam_count < 2:
        print('Это может быть спам, проверьте письмо')
    elif spam_count < 4:
        print('Скорее всего это спам')
    elif spam_count >= 4:
        print('Это точно спам')