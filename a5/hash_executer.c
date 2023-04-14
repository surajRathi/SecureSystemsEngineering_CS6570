#include <stdio.h>

#include <openssl/sha.h>
#include <string.h>


const size_t max_password_length = 2048 - 1;

#define SHA SHA512
#define SHA_L SHA512_DIGEST_LENGTH


// Generated offset: 3
unsigned char true_hash[] = {38, 46, 191, 101, 65, 96, 142, 216, 211, 90, 26, 75, 150, 217, 240, 114, 95, 180, 34,
                             92, 248, 66, 234, 167, 87, 61, 79, 154, 159, 45, 200, 229, 87, 156, 120, 151, 162, 246,
                             227, 252, 39, 92, 164, 73, 251, 158, 125, 23, 19, 57, 64, 193, 129, 229, 230, 106, 239,
                             45, 150, 160, 26, 34, 135, 141,};

#include "hidden_functions.h"

struct two_nums get_nums() {
    // a > b and a != 0, b != 0
    struct two_nums nums = {0, 0, 0};
    printf("Enter num1: ");
    scanf("%i", &nums.a);
    printf("Enter num2: ");
    scanf("%i", &nums.b);
    if (nums.a != 0 && nums.b != 0 && nums.a >= nums.b) {
        nums.success = 1;
    }
    return nums;
}

int check_password() {
    unsigned char str[max_password_length + 1];
    memset(str, 0, max_password_length + 1);

    fgets(str, max_password_length + 1, stdin);

    unsigned char hash1[SHA_L];
    unsigned char hash2[SHA_L];

    // TODO: Use a cryptographically secure hash with a longer size
    SHA(str, sizeof(str) - 1, hash1);
    SHA(hash1, SHA_L, hash2);

    size_t offset = 0;
    unsigned int map_size = 19;
    for (int i = 0; i < SHA_L; i++) {
        offset += hash1[i];
        offset %= map_size;
    }

    int correct = 1;
    for (int i = 0; i < SHA_L; i++) {
        correct &= hash2[i] == true_hash[i];
    }
    if (correct == 1) {
        return (int) offset;
    } else {
        return -1;
    }
}


void run_func(func_type func) {
    struct two_nums nums = get_nums();
    if (nums.success) {
        printf("Output: %i\n", func(nums));
    } else {
        printf("Invalid Numbers inputed. Num1 must be greater than num2 and neither of them can be zero.");
    }
}


int main() {
    printf("(S)ecure function or (A)dd function: ");
    char func[3];
    fgets(func, 3, stdin);
    int offset = -1;
    switch (func[0]) {
        case 'S':
            offset = check_password();
            if (offset != -1) {
                run_func(func_table[offset]);
                break;
            } else {
                printf("you do not have the required access\n");
            }
        case 'A':
            run_func(&add);
            break;
        default:
            printf("Invalid Input.\n");
    }

    return 0;
}
