using System;

namespace LinkedList {
	class LinkedList {

		public class Node {
			public object Content;
			public Node Next;
		}

		public Node head = null;
		private int length;

		//Adds new node at start of list
		public void InsertBeginning(object Data) {
			Node newNode = new Node();
			newNode.Content = Data;

			if (head == null){
				newNode.Next = null;
			} else {
				newNode.Next = head;
			}

			head = newNode;
			length ++;
		}

		public void InsertAfter(int index, object Data) {
			int count = 0;
			Node currentNode = head;

			while (count < index){
				if (currentNode == null) {
					InsertBeginning(Data);
					return;
				}

				if (currentNode.Next != null) {
					currentNode = currentNode.Next;
				} else {
					break;
				}

				count++;
			}

			Node newNode = new Node();
			newNode.Content = Data;

			if (currentNode.Next != null) {
				newNode.Next = currentNode.Next;
			}

			currentNode.Next = newNode;
			length++;
		}

		public Node RemoveBeginning() {

			if (head == null) {
				return head;
			}

			Node returnNode = head;
			head = head.Next;
			length--;
			return returnNode;
		}

		public Node RemoveAfter(int index) {
			int count = 0;
			Node currentNode = head;
			while (count < index) {
				if (currentNode == null || currentNode.Next == null) {
					return null;
				}

				currentNode = currentNode.Next;

				count++;
			}

			Node returnNode = currentNode.Next;
			if (returnNode != null) {
				currentNode.Next = currentNode.Next.Next;
			}
			length--;
			return returnNode;
		}

		public int Length() {
			return length;
		}
	}
}