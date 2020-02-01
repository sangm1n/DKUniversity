// programming homework by sangmin

/*
문자 배열을 입력받아 문자열의 길이를 구해서 출력하는 프로그램을 작성하시오. 
단, 문자열의 길이를 구할 때 문자 배열의 원소를 가리키는 포인터를 이용하시오. 
(주의사항: 라이브러리 함수인 strlen 함수를 이용하지 말고 구현하시오.)
*/

#include <stdio.h>

int main() {
	char str[100];
	char* p = NULL;					// 널 포인터
	int count = 0;

	printf("===== 문자열 길이 출력 프로그램 =====\n");
	printf("문자열 입력: ");
	gets(str);						

	for (p = str; *p; p++)			// *p != '\0' 동안 반복
		count++;
	printf("입력한 문자열의 길이: %d\n", count);

	return 0;
}