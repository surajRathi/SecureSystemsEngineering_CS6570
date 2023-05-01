#include<math.h>


struct two_nums {
    int success;
    int a, b;
};


int average(struct two_nums nums) {
    double a = nums.a, b = nums.b;
    double x = ((double) (a + b)) / 2;
    if (x == (double) ((int) x))
        return (int) x;
    return ((int) x) + 1;
}

int sum(struct two_nums nums) {
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

int modulus(struct two_nums nums) {
    return nums.a % nums.b;
}

int xor(struct two_nums nums) {
    return nums.a ^ nums.b;
}

int or(struct two_nums nums) {
    return nums.a | nums.b;
}

int and(struct two_nums nums) {
    return nums.a & nums.b;
}

int exp_hidden(struct two_nums nums) {
    int ret = 1;
    int a = nums.a, b = nums.b;
    while (a-- > 0)
        ret *= b;
    return ret;
}

int gcd(struct two_nums nums) {
    int a = nums.a, b = nums.b;

    // Calculate gcd using Euclidean algorithm
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }

    return a;
}

int lcm(struct two_nums nums) {
    int a = nums.a, b = nums.b;

    // Calculate lcm using the formula lcm(a,b) = (a*b)/gcd(a,b)
    int gcd_val = gcd(nums);
    int lcm_val = (a * b) / gcd_val;

    return lcm_val;
}

int ncr(struct two_nums nums) {
    int a = nums.a, b = nums.b;

    // Calculate nCr using the formula nCr = n! / (r! * (n-r)!)
    int n = a, r = b;
    int numerator = 1, denominator = 1;

    for (int i = 1; i <= r; i++) {
        numerator *= (n - i + 1);
        denominator *= i;
    }

    return numerator / denominator;
}

int npr(struct two_nums nums) {
    int a = nums.a, b = nums.b;

    // Calculate nPr using the formula nPr = n! / (n-r)!
    int n = a, r = b;
    int numerator = 1;

    for (int i = 1; i <= r; i++) {
        numerator *= (n - i + 1);
    }

    return numerator;
}

int max(struct two_nums nums) {
    return (nums.a > nums.b ? nums.a : nums.b);
}

int min(struct two_nums nums) {
    return (nums.a < nums.b ? nums.a : nums.b);
}


typedef int (*func_type)(struct two_nums);

func_type func_table[16] = {
        average,
        sum,
        subtract,
        multiply,
        divide,
        modulus,
        xor,
        or,
        and,
        exp_hidden,
        gcd,
        lcm,
        ncr,
        npr,
        max,
        min
};