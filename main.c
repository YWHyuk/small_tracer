#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void __attribute__((no_instrument_function)) dummy_ftrace_func(unsigned long ip, unsigned long parent_ip)
{
		char buffer[1024];	
		sprintf(buffer, "python3 symbol.py --pid %d --addr1 %p --addr2 %p", getpid(), (void*)ip, (void*)parent_ip);
		system(buffer);
}

int foo()
{
	return 1;
}

int bar()
{
	return foo();
}

int recursive(int a)
{
	if(!a)
		return 0;
	recursive(a-1);
}

int main()
{
	bar();
	recursive(4);
}
