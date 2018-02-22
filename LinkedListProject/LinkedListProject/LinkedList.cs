using System;

namespace LinkedList {
	class LinkedList {

		public class Node {
			public object Content;
			public Node Next;
		}

		//Creates entirely empty node
		private Node head = null;

		private int length;

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

		public void RemoveBeginning() {
		}

		public void RemoveAfter(int index) {
		}

		public int Length() {
			return length;
		}
	}
}