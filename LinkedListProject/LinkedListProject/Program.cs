using System;

namespace LinkedList {
	class Program {
		static void Main() {
			Stack newStack = new Stack();
			newStack.Push("A");
			newStack.Push("B");
			newStack.Push("C");

			Console.WriteLine(newStack.Peek(1));
			Console.WriteLine(newStack.Length());
			Console.WriteLine(newStack.Pop());
			Console.WriteLine(newStack.Length());
			Console.WriteLine(newStack.Pop());
			Console.WriteLine(newStack.Pop());
			Console.ReadLine();
		}
	}
}
