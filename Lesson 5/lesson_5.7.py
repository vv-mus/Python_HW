import json


with open('Data\\5.7.txt', 'r', encoding='UTF-8') as file:
    res = []
    firms = {}
    av_profit = 0
    amount = 0
    for line in file:
        name, org, profit, cost = line.split()
        firms[name] = float(profit) - float(cost)
        if firms[name] > 0:
            av_profit += firms[name]
            amount += 1
    av_profit /= amount
    res.append(firms)
    res.append({'average_profit': av_profit})
    print(res)

with open('Data\\5.7(exp).json', 'w') as exp_file:
    json.dump(res, exp_file)
