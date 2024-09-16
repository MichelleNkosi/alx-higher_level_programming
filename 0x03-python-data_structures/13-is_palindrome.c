#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list to be reversed.
 * Return: Pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL, *next = NULL;

while (head != NULL)
{
next = head->next;
head->next = prev;
prev = head;
head = next;
}
return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
return (1);

listint_t *slow = *head, *fast = *head, *second_half, *prev_of_slow = *head;
listint_t *mid_node = NULL;  /* To handle odd-sized lists */
int result = 1;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_of_slow = slow;
slow = slow->next;
}

if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}
second_half = reverse_list(slow);
prev_of_slow->next = NULL;

result = compare_lists(*head, second_half);

second_half = reverse_list(second_half);

if (mid_node != NULL)
{
prev_of_slow->next = mid_node;
mid_node->next = second_half;
}
else
prev_of_slow->next = second_half;

return (result);
}

/**
 * compare_lists - Compares two linked lists for equality.
 * @head1: Pointer to the head of the first list.
 * @head2: Pointer to the head of the second list.
 * Return: 1 if the lists are identical, 0 otherwise.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
while (head1 != NULL && head2 != NULL)
{
if (head1->n != head2->n)
return (0);
head1 = head1->next;
head2 = head2->next;
}

if (head1 == NULL && head2 == NULL)
return (1);

return (0);
}
