#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @list: a singly linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	if (head == NULL)
		return (0);
	while (head->next != NULL && head->next != list)
	{
		head = head->next;
	}

	if (head->next == NULL)
	{
		return (0);
	}
	else
	{
		return (1);
	}
}
