using System;

namespace LinkedList {
	class Program {
		static void Main(string[] args) {
			LinkedList list = new LinkedList();
			list.InsertBeginning(5);
			list.RemoveBeginning();

			Console.WriteLine(list.Length());
			Console.ReadLine();
		}
	}
}
