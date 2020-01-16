#    Задание № 1 урока № 9:
#    Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
#
#    Примечание: в сумму не включаем пустую строку и строку целиком.
#
#    Пример работы функции:
#    >>> func("papa")
#    6
#    >>> func("sova")
#    9

import hashlib

def hashFunc(string):
    hashSet = set() # При итоговом подсчете длины множества хешей
    hashSet.update(recHashFunc(string[:-1])) # Берем подстроку равную строке без посл. символа
    for i in range(1, len(string)):
        hashSet.update(recHashFunc(string[i:])) # Перебираем все подстроки начиная с подстроки равной строке без первого
                                                # символа и продолжаем откидывать первый символ
    return hashSet

def recHashFunc(string): # рекурсивная функция возвращающая множество хешей подстрок строки, получаемых отбрасыванием
                         # последнего символа
    hashSet = set()
    print(f'Хеш подстроки {string} = ' + hashlib.sha1(string.encode('utf-8')).hexdigest())
    hashSet.add(hashlib.sha1(string.encode('utf-8')).hexdigest())
    if len(string) > 1:
        hashSet.update(recHashFunc(string[:-1]))
    return hashSet

s1 = 'papa'
print(f'В строке "{s1}" всего {len(hashFunc(s1))} подстрок.\n')
s2 = 'hello'
print(f'В строке "{s2}" всего {len(hashFunc(s2))} подстрок.\n')
s3 = 'hello world!'
print(f'В строке "{s2}" всего {len(hashFunc(s2))} подстрок.')

# Вывод вида -  Хеш подстроки pap = 627a19572de5279b23ee9767fc5cf4b270625ac6
#               Хеш подстроки pa = 379fc0d5299a71ac0f171fbb5afb262829b4e765
#               Хеш подстроки p = 516b9783fca517eecbd1d064da2d165310b19759
#               Хеш подстроки apa = 313212a1870215e863a9da1859fbaa6e53f50670
#               Хеш подстроки ap = ac78b022715c5b8357b4dca8045e8463b4de2124
#               Хеш подстроки a = 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8
#               Хеш подстроки pa = 379fc0d5299a71ac0f171fbb5afb262829b4e765
#               Хеш подстроки p = 516b9783fca517eecbd1d064da2d165310b19759
#               Хеш подстроки a = 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8
#               В строке "papa" всего 6 подстрок.
#
#               Хеш подстроки sov = 8b73d2cf55be45a40c9b3e8ef2db7b9b57a603d0
#               Хеш подстроки so = cd1b646ebd1f6844c60dd91951c6867e43857114
#               Хеш подстроки s = a0f1490a20d0211c997b44bc357e1972deab8ae3
#               Хеш подстроки ova = 4cec6994a371031000221302fe40e9f4a02aa69b
#               Хеш подстроки ov = 998e1e781c4979b5989b6c40d25e3f1e0448a19b
#               Хеш подстроки o = 7a81af3e591ac713f81ea1efe93dcf36157d8376
#               Хеш подстроки va = 665a4dc918ddfb85ea0f1e35c9aef6d1b697c23d
#               Хеш подстроки v = 7a38d8cbd20d9932ba948efaa364bb62651d5ad4
#               Хеш подстроки a = 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8
#               В строке "sova" всего 9 подстрок.
#
#               Хеш подстроки hello world = 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
#               Хеш подстроки hello worl = 5fc1c9e9c73ab18667335ee971cc3eafaf558f4a
#               Хеш подстроки hello wor = f9f687473e170cbfc027068033a3d11a87948c5c
#               Хеш подстроки hello wo = ef5d474beb59efc5968333aa24bbffb2640a1d2e
#               Хеш подстроки hello w = 974d929ed4b5aaab1d1fcf02fea21a48eafc6c48
#               Хеш подстроки hello  = c4d871ad13ad00fde9a7bb7ff7ed2543aec54241
#               Хеш подстроки hello = aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
#               Хеш подстроки hell = a5cec7af5f7aab769cf0d4aa440e01c7bfc371b2
#               Хеш подстроки hel = 3617b3d66d38049664288366ce2ef9f8b9747883
#               Хеш подстроки he = 30f088ea6673877c2e2c1edbe7513ff90eda9a6f
#               Хеш подстроки h = 27d5482eebd075de44389774fce28c69f45c8a75
#               Хеш подстроки ello world! = 4eda2159b0e09598232ce7e3015537d3baa7829e
#               Хеш подстроки ello world = 801ecd005251d6e726d1bb7f6b3dfd3b5bbd7dc0
#               Хеш подстроки ello worl = b2c09e5bb487086eeb600ce24311d62c993d8043
#               Хеш подстроки ello wor = b4f4687a510a4eaa2103149083d7734f0564e8e9
#               Хеш подстроки ello wo = f3e86660b6318abd74d23f3d843867bbd9c29b9b
#               Хеш подстроки ello w = 2f283c2348661e8599f8e59861c74763e2573a58
#               Хеш подстроки ello  = 0a5e3f137409ab7e84b57278e283e2df788ea839
#               Хеш подстроки ello = 179641107fd0dd2684242bc78c86da5fe5f642bf
#               Хеш подстроки ell = d027b4c247e6911ac060b71f7a4979b6e52e773b
#               Хеш подстроки el = 4f1ea4f09db2aaafb0a92c0b9e57751121ed6647
#               Хеш подстроки e = 58e6b3a414a1e090dfc6029add0f3555ccba127f
#               Хеш подстроки llo world! = 010bcd1b46405e046a325ec74c2cfa383b6158cf
#               Хеш подстроки llo world = eeb9a0c61afa87015e9958f70e2c0e5182a09be1
#               Хеш подстроки llo worl = c7b3ee0b011f7c4856d67f7525b9634e681e5f75
#               Хеш подстроки llo wor = 75853459ac4e1b3c61aa97f8dd36aa654627624a
#               Хеш подстроки llo wo = 151309814f49148f2e54d98d57dcf28af955059d
#               Хеш подстроки llo w = ad73698bf90b30e65447dac2df8399537f801ea1
#               Хеш подстроки llo  = 21850c25707dbbc9038ae2539fbb48c120c988ef
#               Хеш подстроки llo = 15eb5215aad6734861a5a5bb9972398fdea9b8d0
#               Хеш подстроки ll = 110c8a30c16070bf2813480d9492a1a170a7d80a
#               Хеш подстроки l = 07c342be6e560e7f43842e2e21b774e61d85f047
#               Хеш подстроки lo world! = c053dc13fb4b8020e703cdd97f744446bd77f8a1
#               Хеш подстроки lo world = 9bb3a6c2efee1f8474ed6ac0fb4cd11316f8bbbc
#               Хеш подстроки lo worl = 6317f621cbed8f3b3913e20330dc06c80e9e8b98
#               Хеш подстроки lo wor = 7504b2218deb426a08c0a6602061a82c56fd5307
#               Хеш подстроки lo wo = 4f664540ff30b8d34e037298a84e4736be39d731
#               Хеш подстроки lo w = c52df063b77c8fb5a01e52f4283ec0ab7883d907
#               Хеш подстроки lo  = 263b8ac41bd2ffb775af535c54d8b0a0e6b9e743
#               Хеш подстроки lo = 638e8f0171575864326f06d2a5f8e72287427b15
#               Хеш подстроки l = 07c342be6e560e7f43842e2e21b774e61d85f047
#               Хеш подстроки o world! = f95b6f5236b88b9179b9c79778ae61105dbedc98
#               Хеш подстроки o world = 7654ed0857479ad0c031a34b71fc8142091468e1
#               Хеш подстроки o worl = 216a5d16caf94de183321afb70847e4ab968038d
#               Хеш подстроки o wor = bb77e042a5d091993daeacb672bcc8e13d7c3252
#               Хеш подстроки o wo = 1085cd1a2f46b0902dac61890f31072561978deb
#               Хеш подстроки o w = 2846627a068ec1bb88cedec0d6a1fc53faf21a02
#               Хеш подстроки o  = 3844e4abcc6962fd091f1657e595a2fd1489be47
#               Хеш подстроки o = 7a81af3e591ac713f81ea1efe93dcf36157d8376
#               Хеш подстроки  world! = 41cdc76e8f597cfd5aa8a448fcd7cf4d5c46c49a
#               Хеш подстроки  world = 3f822726a0c9fb556618e9cb97fb642f7ef62d6f
#               Хеш подстроки  worl = 83c98a35bd56899544bf192db0ce1c59e6fa16f5
#               Хеш подстроки  wor = 24733c09aa28ef947596c92b38840f8f3033e961
#               Хеш подстроки  wo = 62bd868f56c2f537642385b7fd34150a6b08464c
#               Хеш подстроки  w = 39ea134291bdaa96741efedb1750697fbbece53a
#               Хеш подстроки   = b858cb282617fb0956d960215c8e84d1ccf909c6
#               Хеш подстроки world! = a6794c8314ad6aeb08ed149660ee3fefbcda5e6c
#               Хеш подстроки world = 7c211433f02071597741e6ff5a8ea34789abbf43
#               Хеш подстроки worl = 5bfcd144685d14d2d94374d2f71b64b4140a521a
#               Хеш подстроки wor = ff9e40da2345dc9ddb3b7d8f2a95cc335dfedaea
#               Хеш подстроки wo = d29f180f1bb04bcfeb93e4243d542d56e1b504cc
#               Хеш подстроки w = aff024fe4ab0fece4091de044c58c9ae4233383a
#               Хеш подстроки orld! = 2e7be9976b922a040d975ee7052ecd6089cb5af4
#               Хеш подстроки orld = c5161053358305d4523ea755a46229ede4dc845a
#               Хеш подстроки orl = 90255a902e3a09b87ea94d0074d32fa53f1e3df0
#               Хеш подстроки or = 1758356db21759f7c5a0da9b4dd1db8fd6feab3f
#               Хеш подстроки o = 7a81af3e591ac713f81ea1efe93dcf36157d8376
#               Хеш подстроки rld! = d25232b431e159bd56b9e08a1331a46035c891a5
#               Хеш подстроки rld = c466b3a33e6f6dc170438d34fcddf7860d3658fb
#               Хеш подстроки rl = 58e412cbe2ec7e4e08150df17744131fb4aabe84
#               Хеш подстроки r = 4dc7c9ec434ed06502767136789763ec11d2c4b7
#               Хеш подстроки ld! = c20d168802bbae1c84f90b9b0495e0d918da3aea
#               Хеш подстроки ld = 2934526b788a419c15c351c8462a7a7eef4633fb
#               Хеш подстроки l = 07c342be6e560e7f43842e2e21b774e61d85f047
#               Хеш подстроки d! = ef0295f34076cb5928183553e493ad8acc8d609e
#               Хеш подстроки d = 3c363836cf4e16666669a25da280a1865c2d2874
#               Хеш подстроки ! = 0ab8318acaf6e678dd02e2b5c343ed41111b393d
#               В строке "hello world!" всего 74 подстрок.
#
#               Process finished with exit code 0
