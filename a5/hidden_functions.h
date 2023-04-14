struct two_nums {
    int success;
    int a, b;
};

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

typedef int (*func_type)(struct two_nums);

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