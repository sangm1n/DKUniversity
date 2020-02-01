// programming homework by sangmin

/*
입력된 수 만큼의 정수들을 예제 7-5의 선택정렬 프로그램을 이용하여 정렬하는 프로그램을 작성하시오.
이러한 정렬과정을 반복하며,
정수의 수를 입력할 때 -1 이 입력되면 프로그램을 종료하도록 작성하시오.
*/

#define MAX 999										// define 매크로 정의
#include <stdio.h>

int main() {
	int num, index, tmp = 0;
	int arr[MAX];									// 빈 배열 선언

	printf("============= 정렬 프로그램 =============\n");
	while (1) {
		printf("\n정렬할 정수의 수 입력 (종료 시 -1 입력)\n>> ");
		scanf_s("%d", &num);
		if (num == -1)								// -1 입력 시 종료
			break;

		printf("%d개의 정수 차례로 입력\n>> ", num);
		for (int i = 0; i < num; i++)
			scanf_s("%d", &arr[i]);

		for (int i = 0; i < num - 1; i++) {			// 선택정렬
			index = i;
			for (int j = i + 1; j < num; j++)		// 가장 작은 값 선택
				if (arr[index] > arr[j])
					index = j;

			tmp = arr[i];							// switch
			arr[i] = arr[index];
			arr[index] = tmp;
		}

		printf("정렬 결과\n>> ");
		for (int i = 0; i < num; i++)
			printf("%d ", arr[i]);
		printf("\n");
	}

	return 0;
}