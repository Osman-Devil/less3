
res = []
a = 0
with open('nginx_logs.txt', "r", encoding='utf-8') as f:
    for line in f:
        content = line.split()
        res.append((content[0], content[5].strip('"'), content[6]))
        d = dict()
        el = content[0]
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1








    #print(res)