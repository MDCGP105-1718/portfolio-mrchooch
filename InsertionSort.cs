using System;
using System.Collections.Generic;

namespace InsertionSort {
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

			int j = 1;
			while (j < randomList.Length){
				int k = j;
				while (k > 0 && randomList[k-1] > randomList[k]) {
					int holderK = randomList[k];
					int holderKMin1 = randomList[k - 1];
					randomList[k - 1] = holderK;
					randomList[k] = holderKMin1;
					k--;
				}
				j++;
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
