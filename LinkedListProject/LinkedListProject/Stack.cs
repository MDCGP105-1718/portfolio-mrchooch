using System;

namespace LinkedList {
	class Stack: LinkedList {

		public void Push(object data){
			if (IsEmpty()) {
				InsertBeginning(data);
			} else {
				InsertAfter(Length(),data);
			}
		}

		public object Pop(){
			if (Length() > 1) {
				return RemoveAfter(Length() - 2).Content;
			} else {
				return RemoveBeginning().Content;
			}
		}

		public object Peek(int index){
			int count = 0;
			Node currentNode = head;
			while (count < index) {
				if (currentNode == null || currentNode.Next == null) {
					return null;
				}

				currentNode = currentNode.Next;

				count++;
			}
			return currentNode.Content;
		}

		public bool IsEmpty(){
			return Length()==0;
		}
	}
}