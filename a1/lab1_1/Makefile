FLAGS = -m32 -g -fno-stack-protector -O0 -no-pie -static

EXES = lab1_1 

all: $(EXES) 


$(EXES):
	gcc $(FLAGS) $@.c -o $@

clean:
	rm -f $(EXES)
