from docx import Document
import re


def count_phrases(text, phrases):
    phrase_counts = {phrase: 0 for phrase in phrases}
    for phrase in phrases:
        phrase_counts[phrase] = text.count(phrase)
    return phrase_counts


def find_phrases(text, phrases):
    phrase_counts = {}
    for phrase in phrases:
        pattern = r'\\b' + phrase + r'\\b' if phrase.startswith(r'\b') and phrase.endswith(r'\b') else phrase
        matches = re.findall(pattern, text)
        phrase_counts[phrase] = len(matches)

    return phrase_counts



phrases = [
    "в общем,",
    "вот",
    "вроде",
    "да? ",
    "знаете,",
    "значит,",
    "итак",
    'как бы',
    "короче,",
    "на самом деле",
    "некий",
    "некая",
    "ну",
    "ну вот",
    "ну там",
    "получается,",
    "собственно",
    "так скажем",
    "так сказать,",
    "типа",
    "угу",
    "это самое,"
]
for i in range(len(phrases)):
    phrases[i] = fr'(?<!\w){phrases[i]}(?!\w)'

doc_path = 'call_64 (3).docx'
doc = Document(doc_path)
text = ''
for i, para in enumerate(doc.paragraphs):
    text += (para.text).lower() + " "

# Подсчет фраз в тексте
phrase_counts = find_phrases(text, phrases)

# Вывод результатов
for phrase, count in phrase_counts.items():
    print(f"Фраза '{phrase[7:-6:]}' встречается {count} раз.")
