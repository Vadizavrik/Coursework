# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o3_djQ6hM1ZCuApwAWBTjyE4OpN3xIhu
"""

# Курсовая
# Программа должна определить часть речи татарского слова,
# для этого нужно перебрать грамматические показатели,
# составить последовательность грамматических аффиксов и сравнить со словом.
import re

def noun_check(word): # Проверка слова на существительное.
  plurality_list = ["", "лар", "ләр", "нар", "нәр"]
  possesiveness_list = ["", "ым", "ем", "м", "ың", "ең", "ң",
                        "ы", "е", "сы", "се", "ыбыз", "ебез", "быз", "без",
                        "ыгыз", "егез", "гыз", "гез", "лары", "ләре"]
  cases_list = ["ның", "нең", "ны", "не", "га",
                "гә", "ка", "кә", "да", "дә", "та", "тә",
                "дан", "дән", "тан", "тән", "нан", "нән"]
  # Собираем все возможные аффиксы одного грамм. показателя в один список,
  # кроме нулевого аффикса основного падежа, его наличие начинает относить
  # личные глаголы в существительные, так как аффиксы принадлежности
  # совпадают с аффиксами лица. Таким образом,
  # существительные основоного падежа не определяются этой функцией.
  for plurality in plurality_list:
    for possesiveness in possesiveness_list:
      for thecase in cases_list:
        if (word.endswith("маска") or
            word.endswith("мәскә")):
          return "неопределено"
          # Эти глагольные аффиксы оканчиваются так же, как некоторые аффиксы
          # сущ., глаголы с ними могут посчитаться за сущ.,
          # поэтому мы отдельно проверяем их наличие в слове.
        full_end = plurality + possesiveness + thecase
        if word.endswith(full_end) and word != full_end:
          if word.endswith("y" + full_end) or word.endswith("ү" + full_end):
            return "неопределено"
    # Проверяем слово на имя действия, оно изменяется так же как и сущ.,
    # но является формой глагола.
          return "существительное"
  return "неопределено"
  # Если слово кончается на один из возможных наборов грамм. аффиксов сущ.,
  # то оно - существительное, иначе - оно не существительное.

def verb_check(word, words, word_number): # Проверка слова на глагол.
  negation_list = ["", "ма", "мә", "м"]
  voice_list = ["", "н", "ын", "ен", "ел", "ыл", "л", "ыш",
                "еш", "ш", "дыр", "дер", "тыр", "тер", "т", "ыр", "ер", "ар",
                "әр", "гыр", "гер", "кыр", "кер", "гыз", "гез", "кыз", "кез"]
  repeatability_list = ["", "гала", "гәлә", "кала", "кәлә", "штыр", "штер",
                        "ыштыр","ештер", "ынкыра", "енкерә", "нкыра",
                        "нкерә", "ымсыра", "емсерә", "мсыра", "мсерә"]
  impersonal_list = ["", "рга", "ргә", "ырга", "ергә" "арга",
                     "әргә", "маска", "мәскә", "у", "ү", "ган", "гән",
                     "кан", "кән", "учы", "үче", "а", "ә", "ый",
                     "ыр", "ер", "ар", "әр", "р", "ачак", "әчәк",
                     "ячак", "ячәк", "асы", "әсе", "ыйсы", "исе",
                     "ып", "еп", "п", "и", "гач", "гәч", "кач", "кәч",
                     "ганчы", "гәнче", "канчы", "кәнче"]
  times_list = ["ыгыз", "гыз", "егез", "гез", "а", "ә", "ый", "и",
                "сын", "сен", "ды", "де", "ты", "те","ган", "гән" "кан",
                "кән", "ыр", "ер", "ар" ,"әр", "р",
                "ачак", "әчәк", "ячак" ,"ячәк", "са", "сә"]
     # В списке времён собраны все аффиксы наклонения
     # (кроме нулевого аффикса повелительного наклонения)
     # и все аффиксы времени,
     # поскольку они никогда вместе не существуют в одном слове
     # (нулевой аффикс изъявительного наклонения присутствует
     # в каждом аффиксе времени).
  person_list = ["", "мын", "мен", "сың", "сең", "быз", "без", "сыз", "сез",
                 "лар", "ләр", "нар", "нәр", "м", "ң", "к", "ыгыз", "гыз",
                 "егез", "гез"]
  auxiliary_list = ["и", "иде", "итү", "килү", "булу", "тую", "язу", "карау",
                    "күрү", "бару", "тору", "яту","бетү", "бетерү", "чыгу",
                    "чыгару","җитү", "җибәрү" ,"башлау", "китү", "керү",
                    "менү", "төшү", "тотыну", "алу", "кую", "җиткерү",
                    "торган"]
  if word in auxiliary_list:
    return "глагол"
  for negation in negation_list:
    for voice in voice_list:
      for repeatability in repeatability_list:
        for impersonal in impersonal_list:
          if impersonal != "": # Проверка на неличные формы глагола.
            if impersonal in ["у", "ү"]:
              action_name = action_name_check(word, voice, negation,
                                              repeatability, impersonal)
              if action_name == "имя действия":
                 return "имя действия"
                 # Имя действия изменяется и как глагол,
                 # и как существительное,
                 # поэтому ему нужна отдельная функция.
            else:
              full_end = negation + voice + repeatability + impersonal
              if word.endswith(full_end) and word != full_end:
                if impersonal in ["учы", "үче", "асы", "әсе", "ыйсы", "исе"]:
                  return "причастие"
                if impersonal in ["ып", "еп", "п", "гач", "гәч", "кач", "кәч",
                                  "ганчы", "гәнче", "канчы", "кәнче"]:
                  return "деепричастие"
                return "глагол"
                # Проверяем на причастие/деепричастие через их аффиксы.
        for time in times_list:
          for person in person_list:
            full_end = negation + voice + repeatability + time + person
            if word.endswith(full_end) and word != full_end:
              if (word_number + 1 < len(words) and
                  words[word_number + 1] == "торган"):
                 if (word_number + 2 < len(words) and
                     words[word_number + 2] == "иде"):
                   return "глагол"
                 return "причастие"
              return "глагол"
              # Проверка на аналитическую форму причастия и прошедшего времени.
  return "неопределено"

def action_name_check(word, voice, negation, repeatability, impersonal):
  # Отдельная функция для проверки имени действия.
  plurality_list = ["", "лар", "ләр", "нар", "нәр"]
  possesiveness_list = ["", "ым", "ем", "м", "ың", "ең", "ң",
                        "ы", "е", "сы", "се", "ыбыз", "ебез", "быз", "без",
                        "ысы", "ыгыз", "егез", "гыз", "гез", "лары", "ләре"]
  cases_list = ["", "ның", "нең", "ны", "не", "га",
                "гә", "ка", "кә", "да", "дә", "та", "тә",
                "дан", "дән", "тан", "тән", "нан", "нән"]
  for plurality in plurality_list:
    for possesiveness in possesiveness_list:
      for thecase in cases_list:
        full_end = (
            voice +
            repeatability +
            negation +
            impersonal +
            plurality +
            possesiveness +
            thecase
        )
        if word.endswith(full_end) and word != full_end:
          return "имя действия"
  return "неопределено"

def adjective_check(word): # Проверка на прилагательное/наречие.
  comparison_list = ["рак", "рәк", "гылт", "гелт", "кылт", "келт",
                     "сыл", "сел", "шыл", "шел", "су"]
    # Помимо степеней сравнения, эти части речи не имеют грамм. аффиксов,
    # поэтому часто не определяются.
  for comparison in comparison_list:
    if word.endswith(comparison) and word != comparison:
        return "прилагательное/наречие"
  return "неопределено"

def numeral_check(word): # Проверка на числительное.
  base_list = ["бер", "ике", "ик", "өч", "дүрт", "биш", "алты", "алт", "җиде",
               "җид", "сигез", "тугыз", "ун", "егерме", "егерм", "утыз",
               "кырык", "илле", "илл", "алтмыш", "җитмеш", "сиксән", "туксан",
               "йөз", "мең"]
  teens_list = ["", "ун"]
  category_list = ["", "нчы", "нче", "ынчы", "енче", "ар", "әр",
                   "шар", "шәр", "ау", "әү", "лап", "ләп", "лаган", "ләгән",
                   "ларча", "ләрчә", "дан", "дән", "тан", "тән", "нан", "нән"]
  for base in base_list:
    for teen in teens_list:
      for category in category_list:
        full_base = teen + base + category
        if full_base == word:
            # У числительных есть ограниченное количество корней,
            # поэтому можно перебрать их основы, с другой стороны,
            # приложение не проверяет числительные порядком выше миллиона.
          return "числительное"
  return "неопределено"

def pronoun_check(word): # Проверка на местоимения.
  base_list = ["мин", "миң", "син", "сиң", "ул", "ан", "аң", "без", "сез",
               "алар", "бу", "шушы", "шушың", "шушын", "мон", "моң", "бо",
               "шул", "шу", "шуң", "шун","агу", "теге", "теген",
               "кем", "нәрсә", "кай", "кая", "кайчан", "ничә", "нинди",
               "ничек", "нишли", "ни", "ник", "нишләде", "нәрсәгә", "кемнеке",
               "күпме", "никадәр", "бар", "барлык", "барлыгы", "бөтен",
               "hәммә", "hәр", "hop", "hәрбер", "hәркем", "үз", "кайбер"]
  plurality_list = ["", "лар", "ләр", "нар", "нәр"]
  category_list = ["", "нчы", "нче", "ынчы", "енче", "ар", "әр",
                   "шар", "шәр", "аү", "әү", "лап", "ләп", "лаган", "ләгән"]
  possesiveness_list = ["", "ым", "ем", "м", "ың", "ең", "ң", "а",
                        "ы", "е", "сы", "се", "ыбыз", "ебез", "быз", "без",
                        "ысы", "ыгыз", "егез", "гыз", "гез", "лары", "ләре"]
  cases_list = ["", "ем", "а", "е", "ең", "ы", "ә", "ың", "арда", "ардан",
                "ның", "ың" "нең", "ны", "не", "га",
                "гә", "ка", "кә", "да", "дә", "та", "тә",
                "дан", "дән", "тан", "тән", "нан", "нән"]
  uncertainty_list = ["", "дыр", "дер", "тыр", "тер"]
  negation_list = ["", "hич", "бер"]
  possesive_list = ["", "ыкы", "еке"]
  for base in base_list:
    if base in ["мин", "миң", "син", "сиң", "ул", "ан", "аң", "без", "сез",
               "алар", "бу", "шушы", "шушың", "шушын", "мон", "моң", "бо",
               "шул", "шу", "шуң", "шун","агу", "теге", "теген"]:
    # Только эти основы могут принимать аффиксы существительного.
      for plurality in plurality_list:
        for thecase in cases_list:
          for possesive in possesive_list:
            full_base = base + plurality + thecase
            if full_base == word:
              return "местоимение"
      for negation in negation_list:
        for uncertainty in uncertainty_list:
          for category in category_list:
            full_base = (
                negation +
                base +
                category +
                plurality +
                thecase +
                uncertainty
            )
            if full_base == word:
              return "местоимение"
  return "неопределено"

def function_word_check(word): # Проверка на служебное слово.
  postpositions_list = ["белән", "өчен", "кебек", "шикелле", "сымак", "чаклы",
                        "тиклем", "кадәр", "аркылы", "аша", "таба", "табан",
                        "тикле", "хәтле", "хәтлем", "бирле", "башка",
                        "турында", "каршы", "күк", "төсле", "буенча", "буйлап",
                        "буена", "буеннан", "буенда", "саен", "арасында",
                        "арада", "арасыннан", "арасына", "өстеннән", "өстендә",
                        "өстено", "алдыннан", "алдында", "артыннан", "артында",
                        "әченнән", "әчендо", "әченә", "астына", "астыннан",
                        "уртасына", "уртасында", "тирәсендә", "карамастан",
                        "караганда", "бутон", "тыш", "әлек", "башлап", "алып"]
  conjunctions_list = ["hәм", "тагы", "ә", "ләкин", "тик", "шулай",
                       "әмма", "фәкать", "юкса", "йә", "яки", "яисә",
                       "бер", "чөнки", "шуңа", "күрә", "әгәр", "лә", "во", "я",
                       "димәк", "ягъни", "тагын", "янә", "бары",  "ки", "гүя",
                       "гүяки", "гәрчә", "диярсең", "аеруча", "бигрәк"]
  particles_list = ["мы", "ме", "ни", "икән", "гына", "генә", "кына", "кенә",
                    "ук", "үк", "та", "тә", "да", "дә", "дыр", "дер", "тыр",
                    "тер", "бит", "чы", "че", "ка", "соң", "әле", "инде",
                    "менә", "әнә", "мыни", "мени", "сана", "сәно", "әле", "ич",
                    "әллә"]
  modal_words_list = ["әйе", "юк", "әлбәттә", "кирәк", "мөмкин", "ярый",
                      "зинhар", "ахыры", "бәлки", "ихтимал", "күрәсең",
                      "билгеле", "шиксез", "бәхәссез", "чыннан", "чынлап",
                      "әйтерсең", "бар", "тиеш", "түгел", "ярамый", "шул-шул",
                      "ярар"]
      # Не уверен, стоит ли оставлять модальные слова,
      # они во многом являются дополнительным значением
      # значимых слов различных частей речи...
  interjections_list = ["ура", "ah", "их", "ай-hай", "тфү", "уф", "абау", "hм",
                        "әhә", "чү", "әйдә", "каравыл",
                        "ә-ә-ә", "и-и-и", "у-у-у"]
  sound_words_list = ["кыйгак-кыйгак", "бак-бак", "карр", "мияу", "hау-hау",
                      "ләң-ләң", "кикрикүк", "мыр-мыр", "иhи-иhи", "гыр-гыр",
                      "чут-чут", "мелт-мелт", "җәлт-җәлт", "челтер-челтер",
                      "лачтор-лочтыр", "тук-тук"]
  if word in postpositions_list:
    return "послелог"
  elif word in conjunctions_list:
    return "союз"
  elif word in particles_list:
    return "частица"
  elif word in modal_words_list:
    return "вспомогательное слово"
  elif word in interjections_list:
    return "междометие"
  elif word in sound_words_list:
    return "звукоподражательное слово"
  else:
    return "неопределено"
      # Из-за природы служебных слов, чтобы их правильно определить,
      # остаётся просто перебирать по списку,
      # искать соответствие со словом...

text = input("Введите текст на татарском языке: ")
text = text.lower()
text = re.sub(r'[,":-]', "", text)
sentences = re.split(r"[.!?]", text)
sentences = [s.strip() for s in sentences if s.strip()]
# Можно ли как-то вернуть удалённые знаки препинания
# и восстановить правильную капитализацию текста?
for sentence in sentences:
  words = [word.strip() for word in sentence.split(" ") if word.strip()]
  for word_number in range(len(words)):
    theword = words[word_number]
    # Здесь выполняются функции определения частей речи и,
    # на основе их результатов, словам приписываются пометы.
    # Помета "неопределено" служит для предотвращения ошибок
    # и показывает слова, с которыми приложение не справилось.
    # Словарь для сопоставления результатов проверок с тегами:
    tags_dict = {"послелог": "[послелог]", "союз": "[союз]",
                   "частица": "[частица]",
                   "вспомогательное слово": "[вспом.слово]",
                   "междометие": "[междомет]",
                   "звукоподражательное слово": "[звукоподраж.слово]",
                   "местоимение": "[местим]", "числительное": "[числ]",
                   "существительное": "[сущ]", "глагол": "[глагол]",
                   "имя действия": "[глагол (имя действ.)]",
                   "причастие": "[глагол (прич)]",
                   "деепричастие": "[глагол (дееприч)]",
                   "прилагательное/наречие": "[прил/нар]"}
    # Список проверочных функций в порядке приоритета:
    check_functions = [function_word_check, pronoun_check, numeral_check,
                       noun_check, lambda w: verb_check(w, words, word_number),
                       adjective_check]
    # Основная логика обработки слова:
    for check_func in check_functions:
        result = check_func(theword)
        if result in tags_dict:
            words[word_number] = f"{theword}{tags_dict[result]}"
            break
    else:
        words[word_number] = f"{theword}[неопред]"
  if len(words) == 1:
    if words[0].endswith("[неопред]"):
      words[0] = re.sub(r"\[[а-я.() ]+\]", "[сущ]", words[0])
      print(words[0])
      continue
      # Если предложение состоит из одного неопределённого слова,
      # то оно, скорее всего, номинативное.
    else:
      print(words[0])
      continue
      # Границы предложений приходится прорабатывать отдельно,
      # чтобы избежать ошибки с обращением к несуществующему элементу списка.
  if words[0].endswith("[неопред]") or words[0].endswith("[прил/нар]"):
    if words[1].endswith("[послелог]"):
      words[0] = re.sub(r"\[[а-я.() ]+\]", "[сущ]", words[0])
    # Перед послелогом всегда стоит существительное (или местоимение).
    elif words[1].endswith("[неопред]"):
      words[0] = re.sub(r"\[[а-я.() ]+\]", "[прил]", words[0])
      words[1] = re.sub(r"\[[а-я.() ]+\]", "[сущ]", words[1])
        # Если предложение начинается с двух неопределённых слов, то,
        # скорее всего, одно из них - прилагательное,
        # второе - существительное в основном падеже.
    elif (words[1].endswith("[сущ]") or
          words[1].endswith("[местим]") or
          words[1].endswith("имя действ.)]")):
      words[0] = re.sub(r"\[[а-я.() ]+\]", "[прил]", words[0])
        # Неопределённое слово перед существительным, местоимением
        # или именем действия, скорее всего, будет прилагательным.
    elif words[1].endswith("[глагол]"):
      if words[0].endswith("[неопред]"):
        words[0] = re.sub(r"\[[а-я.() ]+\]", "[сущ]", words[0])
      else:
        words[0] = re.sub(r"\[[а-я.() ]+\]", "[нар]", words[0])
          # Предложение, в котором глагол - второе слово,
          # скорее имеет первое слово - подлежащее,
          # а значит - существительное.
    elif words[1].endswith("дееприч)]"):
      words[0] = re.sub(r"\[[а-я.() ]+\]", "[нар]", words[0])
  for word_number in range(1, len(words) - 1):
    if (words[word_number].endswith("[неопред]") or
        words[word_number].endswith("[прил/нар]")):
      if words[word_number + 1].endswith("[послелог]"):
        words[word_number] = re.sub(
            r"\[[а-я.() ]+\]",
            "[сущ]",
            words[word_number]
        )
      elif (words[word_number + 1].endswith("[сущ]") or
            words[word_number + 1].endswith("[местим]") or
            words[word_number + 1].endswith("имя действ.)]")):
        words[word_number] = re.sub(
            r"\[[а-я.() ]+\]",
            "[прил]",
            words[word_number]
        )
      elif (words[word_number + 1].endswith("[глагол]") or
            words[word_number + 1].endswith("дееприч)]")):
        words[word_number] = re.sub(
            r"\[[а-я.() ]+\]",
            "[нар]",
            words[word_number]
        )
            # Неопределённое слово перед глаголом или деепричастием,
            # скорее всего, будет наречием.
  if words[len(words) - 1].endswith("[неопред]"):
      words[len(words) - 1] = re.sub(
          r"\[[а-я.() ]+\]",
          "[глагол]",
          words[len(words) - 1]
      )
          # Неопределённое слово в конце предложения,
          # скорее всего, будет глаголом.
  new_sentence = " ".join(words)
  print(new_sentence)
  # Печатаем получившийся список слов с пометами, идём к следующему.