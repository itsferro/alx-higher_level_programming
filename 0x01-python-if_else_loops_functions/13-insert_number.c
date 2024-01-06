#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: a pointer to a pointer points to the head of the list.
 * @number: an integer to insert.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp, *current = *head;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	if (current != NULL)
	{
		while (number >= current->n)
		{
			tmp = current;
			current = current->next;
		}
		current = tmp;
		node->next = current->next;
		current->next = node;
	}
	else
	{
		node->next = NULL;
		current = node;
	}
	return (node);
}
