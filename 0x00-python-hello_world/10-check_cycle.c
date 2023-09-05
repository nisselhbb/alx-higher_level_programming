#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has
 * a cycle
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *check;

	if (list == NULL || list->next == NULL)
		return (0);
	check = list->next;

	while (check != NULL && check->next != NULL)
	{
		if (list == check)
			return (1);
		list = list->next;
		check = check->next->next;
	}
	return (0);
}

