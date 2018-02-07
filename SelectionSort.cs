using System;
using System.Collections.Generic;

namespace SortingAlgorithms {
	class Program {
		static void Main(string[] args) {
			int[] randomList = new int[10];
			//Make random list of 10 numbers between 1 and 50
			Random randNum = new Random();
			for (int i = 0; i < randomList.Length; i++) {
				randomList[i] = randNum.Next(1, 50);
			}
			//Print them all out
			Console.WriteLine("Original:");
			foreach (int i in randomList) {
				Console.WriteLine(i);
			}

			//For each number
			for (int i = 0; i < randomList.Length-1; i++){
				int minimum = i;

				//Find the first number smaller than it
				for (int j = i+1; j < randomList.Length; j++){
					if (randomList[j] < randomList[minimum]){
						minimum = j;
					}
				}

				//Swap numbers
				if (minimum != i){
					int holderI = randomList[i];
					int holderMin = randomList[minimum];
					randomList[i] = holderMin;
					randomList[minimum] = holderI;
				}
			}

			//Print the sorted list
			Console.WriteLine("Sorted:");
			foreach (int i in randomList) {
				Console.WriteLine(i);
			}
			Console.ReadLine();
		}
	}
}
