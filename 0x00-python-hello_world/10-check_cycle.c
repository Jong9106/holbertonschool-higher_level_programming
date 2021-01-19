#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function that checks if a list has a cycle in it
 * @list: List to check
 * Return: 1 for success or 0 if it fails
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
