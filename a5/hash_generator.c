#include <stdio.h>

#include <openssl/sha.h>
#include <string.h>

const size_t max_password_length = 40;

int main() {
    // const unsigned char str[] = "This is the super duper secret password!";
    // const unsigned char str[max_password_length + 1] = "suraj";
    unsigned char str[max_password_length + 1];
    memset(str, 0, max_password_length + 1);

    fgets(str, max_password_length + 1, stdin);

    unsigned char hash1[SHA_DIGEST_LENGTH]; // == 20
    unsigned char hash2[SHA_DIGEST_LENGTH]; // == 20

    // TODO: Use a cryptographically secure hash with a longer size
    SHA1(str, sizeof(str) - 1, hash1);
    SHA1(hash1, SHA_DIGEST_LENGTH, hash2);

    // do some stuff with the hash

    printf("%d\n", SHA_DIGEST_LENGTH);
    printf("%lu\n", sizeof(str) - 1);


    unsigned int offset = hash1[SHA_DIGEST_LENGTH - 1] % 8;
    printf("// Generated offset: %u\n", offset);

    printf("unsigned char true_hash[] = {");
    for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        printf("%u, ", hash2[i]);
    }
    printf("};\n");


    unsigned char second_hash[] = {124, 58, 177, 180, 135, 194, 12, 70, 113,
                                   73, 31, 63, 147, 188, 139, 184, 14,
                                   44, 22, 23,};


    int correct = 1;
    for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        correct &= hash2[i] == second_hash[i];
    }
    if (correct == 1) {
        printf("The Password is Correct!");
    } else {
        printf("The Password is wrong.");
    }
    return 0;
}
