from collections import OrderedDict, defaultdict, deque, Counter

N = 3000 # количество ip адресов для анализа

with open('big_log.txt', 'r', encoding='utf-8') as f:
    log = deque(f, N)

print(log)

data = OrderedDict()
spam = defaultdict(int)

for item in log:
    ip = str(item[:-1])

    if not ip.startswith('192.168'):
        spam[ip] += 1
        data[ip] = 1

data.update(spam)
print(Counter(data).most_common(10))
