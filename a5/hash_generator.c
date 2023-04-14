#include <stdio.h>

#include <openssl/sha.h>
#include <string.h>


const size_t max_password_length = 2048 - 1;

#define SHA SHA512
#define SHA_L SHA512_DIGEST_LENGTH

int main() {
    unsigned char str[max_password_length + 1];
    memset(str, 0, max_password_length + 1);

    fgets(str, max_password_length + 1, stdin);

    unsigned char hash1[SHA_L];
    unsigned char hash2[SHA_L];

    // TODO: Use a cryptographically secure hash with a longer size
    SHA(str, sizeof(str) - 1, hash1);
    SHA(hash1, SHA_L, hash2);

    size_t offset = 0;
    unsigned int map_size = 16;
    for (int i = 0; i < SHA_L; i++) {
        offset += hash1[i];
        offset %= map_size;
    }
    printf("// Generated offset: %zu\n", offset);

    printf("unsigned char true_hash[] = {");
    for (int i = 0; i < SHA_L; i++) {
        printf("%u, ", hash2[i]);
    }

    printf("};\n");

    unsigned char true_hash[] = {38, 46, 191, 101, 65, 96, 142, 216, 211, 90, 26, 75, 150, 217, 240, 114, 95, 180, 34,
                                 92, 248, 66, 234, 167, 87, 61, 79, 154, 159, 45, 200, 229, 87, 156, 120, 151, 162, 246,
                                 227, 252, 39, 92, 164, 73, 251, 158, 125, 23, 19, 57, 64, 193, 129, 229, 230, 106, 239,
                                 45, 150, 160, 26, 34, 135, 141,};
    int correct = 1;
    for (int i = 0; i < SHA_L; i++) {
        correct &= hash2[i] == true_hash[i];
    }
    if (correct == 1) {
        printf("The Password is Correct!\n");
    } else {
        printf("The Password is wrong.\n");
    }
    return 0;
}
