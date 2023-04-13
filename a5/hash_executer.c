#include <stdio.h>

#include <openssl/sha.h>
#include <string.h>

// Generated offset: 6
unsigned char true_hash[] = {24, 45, 223, 87, 45, 155, 197, 153, 202, 94, 20, 184, 67, 39, 243, 113, 185, 111, 45,
                             202,};

const size_t max_password_length = 40;

struct two_nums {
    int success;
    int a, b;
};

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

    char input[max_password_length + 1];
    memset(input, 0, max_password_length + 1);
    printf("Enter the password: ");
    fgets(input, max_password_length, stdin);

    unsigned char hash1[SHA_DIGEST_LENGTH]; // == 20
    unsigned char hash2[SHA_DIGEST_LENGTH]; // == 20

    // TODO: Use a cryptographically secure hash with a longer size
    SHA1(input, max_password_length, hash1);
    SHA1(hash1, SHA_DIGEST_LENGTH, hash2);

    int correct = 1;
    for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        correct &= hash2[i] == true_hash[i];
    }
    unsigned int offset = hash1[SHA_DIGEST_LENGTH - 1] % 8;

    if (correct == 1) {
        return offset;
    } else {
        return -1;
    }
}

typedef int (*func_type)(struct two_nums);

void run_func(func_type func) {
    struct two_nums nums = get_nums();
    if (nums.success) {
        printf("Output: %i\n", func(nums));
    } else {
        printf("Invalid Numbers inputed. Num1 must be greater than num2 and neither of them can be zero.");
    }
}


int add(struct two_nums nums) {
    return nums.a + nums.b;
}

int subtract(struct two_nums nums) {
    return nums.a - nums.b;
}

int multiply(struct two_nums nums) {
    return nums.a * nums.b;
}

int divide(struct two_nums nums) {
    return nums.a / nums.b;
}

func_type func_table[8] = {
        add,
        add,
        subtract,
        subtract,
        multiply,
        multiply,
        divide,
        multiply,
};

int main() {
    printf("(S)ecure function or (A)dd function: ");
    char func[3];
    fgets(func, 3, stdin);
    int offset = -1;
    switch (func[0]) {
        case 'A':
            run_func(&add);
            break;
        case 'S':
            offset = check_password();
            if (offset == -1) {
                printf("User is not Authenticated\n");
            } else {
                run_func(func_table[offset]);
            }
            break;
        default:
            printf("Invalid Input.\n");
    }

    return 0;
}
