# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
from random import randrange as rr

def get_jokes(n):
    jokes = []
    for _ in range(n):
        joke = ' '.join([nouns[rr(len(nouns))], adverbs[rr(len(adverbs))], adjectives[rr(len(adjectives))]])
        jokes.append(joke)
    print(jokes)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(5)
