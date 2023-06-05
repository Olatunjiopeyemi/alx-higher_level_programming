#include "lists.h"

/**
 * check_cycle - A function that checks if a singly linked list has a cycle inC
 * @list: The linked list to check
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	fast = list->next;
	slow = list;

	while (fast && slow && fast->next)
	{
		if (fast == slow)
		{
			return (1);
		}

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}


