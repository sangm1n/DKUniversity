// programming homework by sangmin

/*
동적 메모리 할당을 사용하여 정수형 배열을 생성하고, 그 배열의 크기만큼 정수를 입력받는다.
이때 같은 정수가 1번 이상 입력될 수 있으며, 중복되지 않은 정수들만을 출력하는 프로그램을 작성하시오.
 3가지 다른 데이터에 대해 프로그램을 실행하시오.
*/

#include <stdio.h>

int main() {
    int size;
    int* arr = NULL;                            // 동적 메모리 주소
    printf("배열의 크기 입력: ");
    scanf_s("%d", &size);

    arr = malloc(sizeof(int) * size);           // 동적 메모리 할당
    printf("%d개의 정수 입력: ", size);
    for (int i = 0; i < size; i++)
        scanf_s("%d", &arr[i]);

    printf("중복되지 않은 정수들: ");
    for (int i = 0; i < size; i++) {
        int count = 0;
        for (int j = 0; j < size; j++) {
            if (arr[i] == arr[j])               // 같은 값 있으면
                count++;                        // count 1 증가
        }
        if (count == 1)
            printf("%d ", arr[i]);
    }

    free(arr);                                  // 동적 메모리 해제

    return 0;
}