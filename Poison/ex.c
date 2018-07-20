#include <stdio.h>
#include <unistd.h>

int main()
{
	setuid(0);
	setgid(0);
	printf("Congratulations you are root!");
}
