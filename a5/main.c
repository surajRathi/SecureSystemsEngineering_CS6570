#include <gnu/libc-version.h>
#include <stdio.h>


int main() {
    /* Basic library version check. */
    printf("gnu_get_libc_version() = %s\n", gnu_get_libc_version());

}