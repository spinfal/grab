import requests as r
import time as t
import random
from termcolor import colored as cl
import os
# user-agents
from fake_useragent import UserAgent
ua = UserAgent()

f = open("proxies.txt", "r")

haha = [
  'stop being weird, loser',
  'grabbing ips? try going outside, smh',
  'oh no dont dos me!',
  'i hope your pillow is warm on both sides tonight',
  'get a life',
  'dont hack my fortnight account!',
  'this is why mom doesnt fucking love you!'
]

# the stuff
while True:
  a = ua.random
  line = f.readline()
  if not line:
    break
  getProx = line.strip()
  refe = haha[random.randint(0,6)]

  headers = {
    'User-Agent': a,
    'referer': refe
  }

  proxies = {
    'http': getProx
  }

  print('proxy: ' + cl(getProx, 'cyan') + '\nreferer: ' + cl(refe, 'cyan') + '\nuser-agent: ' + cl(a, 'cyan') + '\n')
  # grabify is here to test the ips and tool (dont visit, use common sense)
  res = r.get('https://grabify.link/3OUF0O', headers=headers, proxies=proxies)
  print(res)
  t.sleep(0)