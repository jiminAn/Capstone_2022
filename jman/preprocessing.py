import pandas as pd
import sys
import pprint as pp
from collections import defaultdict

input_file = sys.argv[1]

users = []
chatbots = defaultdict(list)
idx = 1
cnt = 0
same_flag = False

with open(input_file, 'r') as f:
    for line in f.readlines():
        category, user, chatbot = line.split('\t')
        users.append(user.strip())
        chatbot = chatbot.strip()

        if chatbot != "":
            if not same_flag:
                idx = cnt
                same_flag = True
            chatbots[idx].append(chatbot)
        elif same_flag:
            same_flag = False
        cnt += 1

for i in range(len(users)):
    if i in chatbots:
        chats = chatbots[i]

    for chat in chats:
        print(users[i], chat, sep = '\t')
