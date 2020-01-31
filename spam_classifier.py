import numpy as np
import re

pA, pNotA = 0, 0
spam, ham = {}, {}
len_spam, len_ham = 0, 0
words_pattern = re.compile("[А-Яа-яЁё]+")

def calculate_word_frequencies(body, label):
    global len_spam
    global len_ham
    word_list = list(set(words_pattern.findall(body.lower())))
    if label == 'SPAM':
        for word in word_list:
            if word in spam:
                spam[word] += 1
                len_spam += 1
            else:
                spam[word] = 2
                len_spam += 2
    else:
        for word in word_list:
            if word in ham:
                ham[word] += 1
                len_ham += 1
            else:
                ham[word] = 2
                len_ham += 2
    return

def train():
    global pA
    global pNotA
    spam_count = 0
    ham_count = 0
    total = 0
    for item in train_data:
        calculate_word_frequencies(item[0],item[1])
        spam_count, ham_count = spam_count + int(item[1] == SPAM), ham_count + int(item[1] == NOT_SPAM)
        total += 1
    pA, pNotA = spam_count / total, ham_count / total
    return  

def calculate_P_Bi_A(word, label):
    global len_spam
    global len_ham
    if label == 'SPAM':
        if word in spam:
            return spam[word]/len_spam
        else:
            return 1/len_spam
    else:
        if word in ham:
            return ham[word]/len_ham
        else:
            return 1/len_ham

def calculate_P_B_A(text, label):
    pBA = 0
    word_list = list(set(words_pattern.findall(text.lower())))
#     if label == 'SPAM': print(word_list)
    for word in word_list:
        if pBA == 0:
            pBA = calculate_P_Bi_A(word, label)
        else:
            pBA = pBA * calculate_P_Bi_A(word, label)
    if label == 'SPAM': return pA * pBA
    else: return pNotA * pBA

def classify(email):
    prob_spam = calculate_P_B_A(email,SPAM)
    prob_ham = calculate_P_B_A(email,NOT_SPAM)
    print('prob_spam',prob_spam, '/ prob_ham',prob_ham)
    if calculate_P_B_A(email,SPAM) > calculate_P_B_A(email,NOT_SPAM):
        return SPAM
    else: return NOT_SPAM

SPAM, NOT_SPAM = 'SPAM', 'NOT_SPAM'

train_data = [  
    ['Купите новое чистящее средство', SPAM],   
    ['Купи мою новую книгу', SPAM],  
    ['Подари себе новый телефон', SPAM],
    ['Добро пожаловать и купите новый телевизор', SPAM],
    ['Привет давно не виделись', NOT_SPAM], 
    ['Довезем до аэропорта из пригорода всего за 399 рублей', SPAM], 
    ['Добро пожаловать в Мой Круг', NOT_SPAM],  
    ['Я все еще жду документы', NOT_SPAM],  
    ['Приглашаем на конференцию Data Science', NOT_SPAM],
    ['Потерял твой телефон напомни', NOT_SPAM],
    ['Порадуй своего питомца новым костюмом', SPAM]
]
