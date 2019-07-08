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
    import io
    import os
    import subprocess

    # Run test if invoked from shell
    if os.getenv('SCRIPT_NAME') is None:
        print('This program should be run from cgi.')
        # return

    # Change encoding of stdout to utf-8
    # It is required becaue CGI script runs as another user and may not
    # print utf-8 encoded text
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Respond HTTP header
    print('Content-Type: text/html')
    print('Cache-Control: public\n')

    # Get input strings
    f = cgi.FieldStorage()
    site = f.getfirst('site', 'none')
    char = f.getfirst('char', 'an')
    plen = f.getfirst('len', '16')
    desc = f.getfirst('desc', '')
    
    # Print header
    print('''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Passme cgi</title>
  <link rel="stylesheet" type="text/css" media="screen and (min-width:641px)" href="../seki.css">
</head>

<body>
<h1>Passme cgi</h1>''', flush=True)
    print(site)

    site = site.replace(' ','').replace('<','').replace('>','').replace('&','').replace('"','').replace("'",'').replace('|','').replace('.','')
    print(site)

    if len(site) < 1:
    	site = 'none'
    if char not in ['a', 'n', 'an', 'ans']:
        char = 'an'
    plen = int(plen)
    if plen < 4:
        plen = 16
    desc = desc.replace('"','').replace("'",'')

    if site != 'none':
        with open("add.txt", "w") as f:
            f.write('{0}\n{1}\n{2}\n{3}\n\n'.format(site, char, plen, desc))
        
        
        print('<hr>')


    print('''<form action="index.py" method="post">
サイト: <input type="text" name="site" id="site" size="10" maxlength="10" value=""><br>
記号: <select name="char" id="char">
  <option value="an" selected>アルファベット + 数字
  <option value="ans">アルファベット + 数字 + 記号
  <option value="a">アルファベットのみ
  <option value="n">数字のみ
</select><br>
文字数: サイト: <input type="text" name="len" id="len" size="2" maxlength="2" value="16"><br>
説明<br><textarea name="desc" id="desc" rows="4" cols="20" wrap="off">
</textarea></p>
<p><input type="submit" value="追加する"></p>
</form>''', flush=True)

    print('<h2>サイト一覧</h2>', flush=True)

    subprocess.check_call(['sh', 'output.sh'])

    list = subprocess.check_output(['passme', 'list']).decode("utf-8").split()
    for i in range(len(list)):
    	list[i] = list[i].strip(",[]'")
    print('<ul>')
    for s in list:
    	print('<li>{0}'.format(s))
    print('</ul>')

    
    # print footer

    print('<hr>', flush=True)
    subprocess.check_call(['python3', '-V'])
    print('</body></html>')

    return


if __name__ == '__main__':
    main()
