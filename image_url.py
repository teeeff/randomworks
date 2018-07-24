# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:25:52 2018

@author: tfarid
"""

import urllib.request
import datetime
import multiprocessing

def mp_worker(line):
    array=line.split(',')
    style_code=array[0].strip()
    seq_num=array[1].strip()
    url=array[2].strip()
    try:
        response=urllib.request.urlopen(url)
        response.getcode()
        return(style_code,seq_num,url,'Y')
    except:
        return(style_code,seq_num,url,'N')
    

def mp_handler():
    p = multiprocessing.Pool(32)
    with open('prod_urls.csv') as f:
        urls = [line for line in (l.strip() for l in f) if line]
    with open('validated_prod.csv', 'w') as f:
        for result in p.imap(mp_worker, urls):
            # (filename, count) tuples from worker
            f.write('%s,%s,%s,%s\n' % result)

if __name__=='__main__':
    print(datetime.datetime.utcnow())
    mp_handler()
    print(datetime.datetime.utcnow())