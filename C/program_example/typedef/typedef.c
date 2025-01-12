// /usr/bin/gcc

// File Name       : typedef.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-12 22:33:03
// Last Modified   : 2025-01-12 22:44:12
#include <stdio.h>
#include <string.h>

typedef struct Books
{
    char title[50];
    char author[50];
    char subject[100];
    int book_id;
} Book;

int main()
{
    Book book;
    strcpy(book.title, "C program");
    strcpy(book.author, "wangyuankun");
    strcpy(book.subject, "programming");
    book.book_id = 12345;

    printf("book title: %s\n", book.title);
    printf("book author: %s\n", book.author);
    printf("book subject: %s\n", book.subject);
    printf("book id: %d\n", book.book_id);
    return 0;
}
