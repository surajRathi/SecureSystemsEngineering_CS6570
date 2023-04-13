#include <stdio.h>

#include <openssl/sha.h>

unsigned char true_hash[] = {124, 58, 177, 180, 135, 194, 12, 70, 113,
                             73, 31, 63, 147, 188, 139, 184, 14,
                             44, 22, 23,};

const size_t max_password_length = 40;

int main() {
    char input[max_password_length + 1];
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
    if (correct == 1) {
        printf("The Password is Correct!");
    } else {
        printf("The Password is wrong.");
    }
    unsigned int offset = hash1[SHA_DIGEST_LENGTH - 1] % 8;

    return 0;
}
