#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: pointer to the head of the linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* Check if the list is empty */
	if (!list)
		return (0);

	/* Use Floyd's Cycle Detection Algorithm */
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If there is a cycle, return 1 */
		if (slow == fast)
			return (1);
	}

	/* If no cycle is found, return 0 */
	return (0);
}
