// /usr/bin/gcc

// File Name       : struct.c
// Author          : Yuankun.Wang
// Created Time    : 2025-01-06 23:05:51
// Last Modified   : 2025-01-08 23:36:57
#include <stdio.h>
#include <string.h>

struct Books
{
    char title[50];
    char author[50];
    char subject[100];
    int book_id;
};

void printBook(struct Books *book);

int main()
{
    struct Books Book1;
    struct Books Book2;
    
    strcpy(Book1.title, "C Programming");
    strcpy(Book1.author, "wangyuankun");
    strcpy(Book1.subject, "C Porgramming Tutorial");
    Book1.book_id = 6495407;

    strcpy(Book2.title, "Ellecom Billing");
    strcpy(Book2.author, "liuchunyu");
    strcpy(Book2.subject, "Telecom Billing Tutorial");
    Book2.book_id = 6495700;

    printBook(&Book1);
    printBook(&Book2);

    return 0;
}

void printBook(struct Books *book)
{
    printf("Book title: %s\n", book->title);
    printf("Book author: %s\n", book->author);
    printf("Book subject: %s\n", book->subject);
    printf("Book book_id: %d\n", book->book_id);
}
