#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


URL = './'  # URL of ecfit in relative path

if True:  # True for showing detailed traceback
    import cgitb
    cgitb.enable()


def main():
    """Passme CGI interface"""
    import cgi
    from io import TextIOWrapper
    from os import getenv
    from ecfit import printhtml

    # Run test if invoked from shell
    if getenv('SCRIPT_NAME') is None:
        print('This program should be run from cgi.')
        # return

    # Change encoding of stdout to utf-8
    # It is required becaue CGI script runs as another user and may not
    # print utf-8 encoded text
    sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Respond HTTP header
    print('Content-Type: text/html')
    print('Cache-Control: public\n')

    # Get input strings
    f = cgi.FieldStorage()
    getlang = f.getfirst('lang', 'none')
    inputtext = f.getfirst('input', '')

    print('''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Passme cgi</title>
  <link rel="stylesheet" type="text/css" media="screen and (min-width:641px)" href="../seki.css">
</head>

<body>
<h1>Passme cgi</h1>''')


    print('</body></html>')

    return


if __name__ == '__main__':
    main()
