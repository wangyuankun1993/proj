// /usr/bin/gcc

// File Name       : struct.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-06 23:05:51
// Last Modified   : 2025-01-06 23:17:22
#include <stdio.h>

struct Books
{
    char title[50];
    char author[50];
    char subject[100];
    int book_id;
} book = {"C", "wangyuankun", "program", 123456};

int main()
{
    printf("title: %s\nauthor: %s\nsubject: %s\nbook_id: %d\n", book.title, book.author, book.subject, book.book_id);
}
