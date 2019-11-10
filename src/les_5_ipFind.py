import argparse
from collections import ChainMap


defaults = {'ip': 'localhost', 'port': 7777}

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip')
parser.add_argument('-p', '--port')

args = parser.parse_args()
new_dict = {key: value for key, value in vars(args).items() if value}

settings = ChainMap(new_dict, defaults)
print(settings['ip'])
print(settings['port'])
