struct constdef {
    char *name;
    int value;
};

struct constdefs {
    char *name;
    struct constdef *members;
};
