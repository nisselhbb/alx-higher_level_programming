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
	listint_t *curr = *head;
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;

	if (curr == NULL || curr->n >= number)
	{
		node->next = curr;
		*head = node;
		return (node);
	}
	while (curr && curr->next &&
		curr->next->n < number)
		curr = curr->next;
	node->next = curr->next;
	curr->next = node;

	return (node);
}
