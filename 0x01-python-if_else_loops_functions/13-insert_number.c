#include "lists.h"
/**
 * insert_node - inserts a new node with a given number
 * to a stored singly linked list
 * @head: a pointer to a pointer to the header of a singly
 * linked list
 * @number: the value to be inserted to the stored
 * linked list
 * Return: NULL if it fails, or the newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *curr, *prv;

	if (!node)
		return (NULL);

	node->n = number;
	node->next = NULL;
	curr = *head;
	prv = NULL;

	if (!curr)
	{
		node->next = curr;
		*head = node;
	}
	else if (curr->n >= number)
	{
		node->next = curr;
		*head = node;
	}
	else
	{
		while (curr && curr->next &&
			curr->next->n < number)
		{
			prv = curr;
			curr = curr->next;
		}
		node->next = curr;
		prv->next = node;
	}

	return (node);
}
