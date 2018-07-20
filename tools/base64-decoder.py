#!/usr/bin/python3.6


import base64
import logging


hash_list = []
hash_file = open('/root/Workspace/htb/Poison/passwd.txt', 'r')
read_hash = hash_file.read()
hash_list.append(read_hash)
hash_file.close()

#print(hash_list[0])
#input("ENTER")

def decoder(hash):
    return base64.b64decode(hash)
    # return decoder(decoded)


def base64_decode(s):
    """Add missing padding to string and return the decoded base64 string."""
    log = logging.getLogger()
    s = str(s).strip()
    try:
        # hash_list.append(base64.b64decode(s))
        return base64.b64decode(s)
    except TypeError:
        padding = len(s) % 4
        if padding == 1:
            log.error("Invalid base64 string: {}".format(s))
            return ''
        elif padding == 2:
            s += b'=='
        elif padding == 3:
            s += b'='
        # hash_list.append(base64.b64decode(s))
        return base64.b64decode(s)







for x in range(0, 14):
    # current_hash = decoder(hash_list[x])
    print('['+str(x)+'] Decoding')
    try:
        current_hash = decoder(hash_list[x])
        padding = len(current_hash) % 4
        print("Current padding: " + str(padding))
    except TypeError:
        current_hash = base64_decoder(hash_list[x])
    hash_list.append(current_hash)
    print(hash_list[x])

    if x == 8:
        padding = len(current_hash) % 4
        print("Current padding: "+str(padding))
        if padding == 2:
            current_hash += b'=='
        elif padding == 3:
            current_hash += b'='
        print(str(current_hash))

print(hash_list)
