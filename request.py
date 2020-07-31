#!/usr/bin/python

import json
import requests
import time

def main():
  # sleep
    time.sleep(1200)
    res=requests.get('https://raw.githubusercontent.com/SWADESNA/custom_inv/master/custom.ini')
    data=res.json()
    print json.dumps(data, sort_keys=True, indent=2)
if __name__ == '__main__':
  main()
