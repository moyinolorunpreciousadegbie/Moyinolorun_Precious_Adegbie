#include <iostream>
using namespace std;
struct Node {
	int data;
	Node *next, *prev;
};
// function to add Node at the end of a Doubly LinkedList
Node* insertAtEnd(Node* head, int data)
{

	Node* new_node = new Node();
	new_node->data = data;
	new_node->next = NULL;
	Node* temp = head;
	if (head == NULL) {
		new_node->prev = NULL;
		head = new_node;
		return head;
	}

	while (temp->next != NULL) {
		temp = temp->next;
	}
	temp->next = new_node;
	new_node->prev = temp;
	return head;
}
// function to print Doubly LinkedList
void printDLL(Node* head)
{
	while (head != NULL) {
		cout << head->data << " ";
		head = head->next;
	}
	cout << endl;
}
// function to Reverse a doubly linked list
// in groups of given size
Node* reverseByN(Node* head, int k)
{
	if (!head)
		return NULL;
	head->prev = NULL;
	Node *temp, *curr = head, *newHead;
	int count = 0;
	while (curr != NULL && count < k) {
		/*
        // umadevi9616 version
        newHead = curr;
		temp = curr->prev;
		curr->prev = curr->next;
		curr->next = temp;
		curr = curr->prev;
		count++;
      */
      
      // my version
      newHead = curr;
		temp = curr->next;
		curr->next = curr->prev;
		curr->prev = temp;
		curr = temp; //      curr = curr->prev  will also work. 
		count++ ;

	}
	// checking if the reversed LinkedList size is
	// equal to K or not
	// if it is not equal to k that means we have reversed
	// the last set of size K and we don't need to call the
	// recursive function
	if (count >= k) {
		Node* rest = reverseByN(curr, k);
		head->next = rest;
		if (rest != NULL)
			// it is required for prev link otherwise u wont
			// be backtrack list due to broken links
			rest->prev = head;
	}
	return newHead;
}
int main()
{
	Node* head;
	for (int i = 1; i <= 10; i++) {
		head = insertAtEnd(head, i);
	}
	printDLL(head);
	int n = 4;
	head = reverseByN(head, n);
	printDLL(head);
}
