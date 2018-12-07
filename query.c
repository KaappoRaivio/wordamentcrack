#include <stdio.h>
#include <string.h>
#include <Python.h>

#define bufSize 1024
#define true 1
#define false 0


int is_word(const char* word);

int main(int argc, char* argv[]) {
    printf("%d\n", is_word("Zulus"));
}

int is_word(const char* word) {
    char buf[bufSize];
    FILE* fp;


    if ((fp = fopen("newwords.txt", "r")) == NULL) {
        perror("fopen source-file");
        return -1;
    }

    int toReturn = false;
    while (fgets(buf, sizeof(buf), fp) != NULL) {
        buf[strlen(buf) - 1] = '\0';

        if (!strcmp(buf, word)) {
            toReturn = true;
            break;
        }
    }
    fclose(fp);
    return toReturn;
}

static PyObject* py_myFunction (PyObject* self, PyObject* args) {
    char* s = "Testing!";
    return Py_BuildValue("s", s);
}