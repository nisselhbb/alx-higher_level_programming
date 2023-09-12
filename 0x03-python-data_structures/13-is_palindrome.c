#include "lists.h"
/**
 * is_palindrome - checks if a singly linkes list is a
 * palindrome
 * @head: pointer to a pointer to the head node
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *final = *head;
	int num = 0, a = 0, b = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (curr)
	{
		curr = curr->next;
		num++;
	}
	curr = *head;

	for (a = 1; a <= num; a++)
	{
		for (b = a; b <= num; b++)
		{
			final = final->next;
		}
		if (curr->n != final->n)
			return (0);
		curr = curr->next;
		final = *head;
	}
	return (1);
}
