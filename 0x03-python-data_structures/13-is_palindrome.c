#include "lists.h"

/**
<<<<<<< HEAD
 * is_palindrome - tests if linked lists is palindrome
 * @head: address of pointer to list
 * Return: 1 is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *node, *prev;
	int failed = 0;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	node = slow;
	prev = NULL;
	while (node)
	{
		fast = node->next;
		node->next = prev;
		prev = node;
		node = fast;
	}
	fast = *head;
	node = prev;
	while (prev)
	{
		if (fast->n != prev->n)
		{
			failed = 1;
			break;
		}
		fast = fast->next;
		prev = prev->next;
	}
	prev = NULL;
	while (node)
	{
		fast = node->next;
		node->next = prev;
		prev = node;
		node = fast;
	}
	return (!failed);
=======
 * pal - recursive helper function to determine if llst is palindrom
 * @start: start position of list
 * @end: end position of list
 *
 * Return: 1 if list is a palindrome, 0 otherwise
 */

int pal(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (pal(start, end->next) == 1 && (*start)->n == end->n)
	{
		*start = (*start)->next;
		return (1);
	}

	return (0);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: list to check
 *
 * Return: 1 if list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	return (pal(head, *head));
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
}
