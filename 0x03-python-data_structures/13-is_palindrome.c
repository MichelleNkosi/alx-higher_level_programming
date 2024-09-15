#include "lists.h"
#include <stddef.h>

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL, *next = NULL;
while (head)
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
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;
listint_t *midnode = NULL;  // To handle odd size list
int result = 1;  // Assume it is a palindrome

if (*head == NULL || (*head)->next == NULL)
return (1);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}
if (fast != NULL)
{
midnode = slow;
slow = slow->next;
}
second_half = slow;
prev_slow->next = NULL;
second_half = reverse_list(second_half);
result = compare_lists(*head, second_half);
second_half = reverse_list(second_half);
if (midnode != NULL)
{
prev_slow->next = midnode;
midnode->next = second_half;
}
else
prev_slow->next = second_half;
return (result);
}

/**
 * compare_lists - Compares two singly linked lists.
 * @head1: Pointer to the head of the first list.
 * @head2: Pointer to the head of the second list.
 * Return: 1 if they are identical, 0 otherwise.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
while (head1 && head2)
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
