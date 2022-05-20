#!/usr/bin/env python

# -*- coding: utf_8 -*-

import socket
import threading
import os
import datetime
import sys
import win32net as win

def get_shares(server):
    return [x[0] for x in win.NetShareEnum(server)]

def print_shares_and_directories(server):
    shares = get_shares(server)
    for share in shares:
        print('SHARE: %s' % share)
        path = '\\\\%s\\%s' % (server, share)
        try:
            files = os.listdir(path)
        except OSError:
            print('    (Directory listing failed)')
        else:
            for file in files:
                if os.path.isdir(os.path.join(path, file)):
                    print('    %s' % file)

def delete_share(server, share):
    win.NetShareDel(server, share, 0)

if __name__ == '__main__':
    server = input("Enter host name: ")
    print_shares_and_directories(server)
    share = input("Enter share name for deletion: ")
    if share == 'test1' or 'test2' or 'test3' or 'test4':
        delete_share(server, share)

