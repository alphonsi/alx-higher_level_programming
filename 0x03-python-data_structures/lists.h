#ifndef LISTS_H
#define LISTS_H

<<<<<<< HEAD
#include <stdlib.h>
#include <stdio.h>
=======
#include <unistd.h>
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);
<<<<<<< HEAD
=======
int pal(listint_t **start, listint_t *end);
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc

#endif /* LISTS_H */
