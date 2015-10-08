all: index.html all.html 199x.html 1995.html 1996.html 1997.html 1998.html 1999.html 200x.html 2000.html 2001.html 2002.html

index.html: head.txt top.txt foot.txt
	cat head.txt top.txt foot.txt > index.html

all.html: head.txt 199x.txt 200x.txt foot.txt
	cat head.txt 199x.txt 200x.txt foot.txt > all.html

1995.html: head.txt 1995.txt foot.txt
	cat head.txt 1995.txt foot.txt > 1995.html

1996.html: head.txt 1996.txt foot.txt
	cat head.txt 1996.txt foot.txt > 1996.html

1997.html: head.txt 1997.txt foot.txt
	cat head.txt 1997.txt foot.txt > 1997.html

1998.html: head.txt 1998.txt foot.txt
	cat head.txt 1998.txt foot.txt > 1998.html

1999.html: head.txt 1999.txt foot.txt
	cat head.txt 1999.txt foot.txt > 1999.html

199x.html: head.txt 199x.txt foot.txt
	cat head.txt 199x.txt foot.txt > 199x.html

199x.txt: 1995.txt 1996.txt 1997.txt 1998.txt 1999.txt
	cat 1995.txt 1996.txt 1997.txt 1998.txt 1999.txt > 199x.txt

2000.html: head.txt 2000.txt foot.txt
	cat head.txt 2000.txt foot.txt > 2000.html

2001.html: head.txt 2001.txt foot.txt
	cat head.txt 2001.txt foot.txt > 2001.html

2002.html: head.txt 2002.txt foot.txt
	cat head.txt 2002.txt foot.txt > 2002.html

200x.txt: 2000.txt 2001.txt 2002.txt
	cat 2000.txt 2001.txt 2002.txt > 200x.txt

200x.html: head.txt 200x.txt foot.txt
	cat head.txt 200x.txt foot.txt > 200x.html

clean:
	rm *.html
	rm *x.txt

