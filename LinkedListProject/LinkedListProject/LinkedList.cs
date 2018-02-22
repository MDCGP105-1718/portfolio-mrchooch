using System;

namespace LinkedList {
	class LinkedList {

		public class Node {
			public object Content;
			public Node Next;
		}

		private Node head = null;
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
			return new Node();
		}

		public int Length() {
			return length;
		}
	}
}