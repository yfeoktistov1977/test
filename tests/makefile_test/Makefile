.PHONY: all

all: test1.out test2.out

#such dependencies means that file is always rebuild
test1.out: bbb
	gcc aaa.c -o test1.out

test2.out:
	gcc aaa2.c -o test2.out


bbb: