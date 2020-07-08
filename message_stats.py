#!/usr/bin/env python3

# INSTAGRAM JSON VIEWER - Message Statistics
# 2020 (c) Micha Johannes Birklbauer
# https://github.com/t0xic-m/
# micha.birklbauer@gmail.com

import pandas as pd
import json

# only 1-1 conversations, no groupchats
def get_stats(username):
    stats = {}

    with open("messages.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    for conversation in data:
        participants = conversation["participants"]
        if len(participants) != 2:
            continue
        partner_1 = participants[0]
        partner_2 = participants[1]
        if partner_1 == username:
            if partner_2 in stats:
                stats[partner_2] = stats[partner_2] + len(conversation["conversation"])
            else:
                stats[partner_2] = len(conversation["conversation"])
        else:
            if partner_1 in stats:
                stats[partner_1] = stats[partner_1] + len(conversation["conversation"])
            else:
                stats[partner_1] = len(conversation["conversation"])

    df = pd.DataFrame({"conversation":list(stats.keys()), "messages":list(stats.values())})
    df.to_csv("message_stats.csv")

    return df

if __name__ == '__main__':
    username = input("Enter your Instagram username:\n")
    result = get_stats(username)
