#include "lists.h"

/**
 * is_it - checks if a string is a palindrome.
 *
 * @str: a pointer to a string
 * @len: is an arrey length.
 *
 * Return: 1 if the list is palindrome.
 *	0 if it is not.
 *	-1 on failure.
 */
int is_it(int str[], unsigned int len)
{
	unsigned int list_len = 0, i = 0;

	list_len = len;
	if ((list_len % 2) != 0)
		return (0);

	list_len -= list_len;
	for (; i < list_len; i++)
	{
		if (str[i] != str[i + (list_len - i)])
		{
			return (0);
		}
	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: a singliy linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int str[BUFFER_SIZE];
	unsigned int i = 0;
	size_t check = 0;
	listint_t *start = *head;

	if (start == NULL)
	{
		free(start);
		return (1);
	}
	while (start != NULL)
	{
		str[i] = start->n;
		start = start->next;
		i++;
	}
	check = is_it(str, i);

	return (check);
}
