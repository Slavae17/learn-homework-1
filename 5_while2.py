"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
  'Как дела?': 'Хорошо!', 
  'Чем занят?': 'Убиваю время!',
  'Какой твой любимый цвет?': 'Синий', 
  'Кто ты по знаку зодиака?': 'Я не верю в знаки зодиака', 
  'Откуда дрова?': 'Из леса'
}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    user_ask = input('Введите ваш вопрос ')
    while questions_and_answers.get(user_ask) != None:
        print (questions_and_answers[user_ask])
        user_ask = input('Введите ваш вопрос ')

        

if __name__ == "__main__":
    ask_user(questions_and_answers)
