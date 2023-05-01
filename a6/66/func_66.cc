#include <cmath>

using uint = unsigned int;

int main() {
    int num1 = 60;
    int num2 = 40;

    uint uVar1;
    double dVar2;
    int k;
    int j;
    int m;
    int l;
    int result;
    uint auStack_158[16];
    uint auStack_118[16];
    uint auStack_d8[16];

    m = 0;
    for (j = num1; 0 < j; j = j / 2) {
        auStack_158[m] = j % 2;
        m += 1;
    }
    l = 0;
    for (k = num2; k > 0; k = k / 2) {
        auStack_118[l] = k % 2;
        l += 1;
    }
    for (; l < 16; l += 1) {
        auStack_118[l] = 0;
    }
    for (; m < 16; m += 1) {
        auStack_158[m] = 0;
    }
    for (m = 15; m >= 0; m--) {
        auStack_d8[m] = auStack_158[m] ^ auStack_118[m];
    }
    result = 0;
    for (l = 15; l >= 0; l--) {
        uVar1 = auStack_d8[l];
        dVar2 = pow(2.0, (double) l);
        result = (int) (dVar2 * (double) uVar1 + (double) result);
    }
    return result;
}