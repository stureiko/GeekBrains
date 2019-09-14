with open('bytes.txt', 'wb') as f:
    f.write('Hello world Привет'.encode('utf-8'))

with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

with open('bytes.txt', 'rb') as f:
    s = f.read()
    print(s)
    print(s.decode('utf-8'))

