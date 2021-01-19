#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head
 * @number: number to add in node
 * Return: the address for success, or NULL for error
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *temp = NULL, *addresstemp = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	temp = *head;
	addresstemp = *head;

	while (temp)
	{
		if (temp->n >= new_node->n)
		{
			if (addresstemp == *head)
			{
				new_node->next = *head;
				*head = new_node;
				return (new_node);
			}
			new_node->next = addresstemp->next;
			addresstemp->next = new_node;
			return (new_node);
		}
		addresstemp = temp;
		temp = temp->next;
	}
	addresstemp->next = new_node;
	return (new_node);
}