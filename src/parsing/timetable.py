import requests
from bs4 import BeautifulSoup

from src.controller.async_mess import sendmess



def get_timetable() -> str:
  timetable = requests.get("https://timetable.tusur.ru/faculties/fvs/groups/544-m")


  # Парсинг HTML с помощью BeautifulSoup
  soup = BeautifulSoup(timetable.text, 'html.parser')

  # Извлечение данных
  title = soup.title.string  # Заголовок страницы
  h1 = soup.h1.string  # Заголовок h1

  lessons = []

  # Поиск тега <td> с классом "current_day"
  current_classes = soup.findAll('td', class_='current_day')

  for i in current_classes:
    lesson_name = i.find('h4', class_='modal-title')
    if lesson_name:
      lesson_name = lesson_name.next

    teacher = i.find('span', class_='group')
    if teacher:
      teacher = teacher.text
      teacher = teacher.replace('\n', '')

    p_tags = i.findAll('p')
    if len(p_tags) > 0:
      for p in p_tags:
        if 'Время проведения:' in p.text:
          time = p.text
          time = time.replace('Время проведения:', '')
          time = time.replace('\n', '')
          time = time.replace(' ', '')


    p_tags = i.findAll('p')
    if len(p_tags) > 0:
      for p in p_tags:
        if 'Место проведения:' in p.text:
          place = p.text
          place = place.replace('Место проведения:', '')
          place = place.replace('\n', '')



      lesson ={
      'name': lesson_name,
      'time': time,
      'teacher': teacher,
      'place': place,
      }

      lessons.append(lesson)


  times = []
  lessons_to_keep = []  # Список для хранения уникальных занятий

  for lesson in lessons:
      if lesson['time'] not in times:  # Проверяем, что 'time' уникально
          times.append(lesson['time'])  # Добавляем уникальное время в список
          lessons_to_keep.append(lesson)  # Добавляем урок в новый список

  # После цикла обновляем исходный список уроков
  lessons = lessons_to_keep

  # Выводим оставшиеся уникальные занятия

  output = ''
  for i in lessons:
      output += f'''

Занятие: {i['name']}
Преподаватель: {i['teacher']}
Время: {i['time']}
Место: {i['place']}

  '''

  print(output)
  return output


def send_timetable():
  sendmess(get_timetable())
