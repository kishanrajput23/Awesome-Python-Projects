a.out:function.o main.o 
	  gcc function.c main.c
functions.o: function.c
			 gcc -c function.c
main.o: main.c header.h
		gcc -c main.c




    