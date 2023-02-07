#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char large_string[128];

void exploit(){
	printf("Exploit succesfull...\n");
}

void welcome(char *name)
{
	long canary= 1431721816;
	char words[12];
	
	strcpy(words, name);

	printf("Welcome group %s, %s.\n", words, name);

	if (canary!=1431721816)
		exit(1);

}


int main(int argc, char** argv)
{
	if(argc != 2)
	{
		printf("usage:\n%s\n", argv[0]);
		return EXIT_FAILURE;
	}
	welcome(argv[1]);
	return EXIT_SUCCESS;
}



