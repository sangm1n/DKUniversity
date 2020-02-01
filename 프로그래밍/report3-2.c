// programming homework by sangmin

/*
아래의 구조체를 사용하여 5개 좌표값을 갖는 배열을 선언하고, 5개의 좌표값을 읽어 들여라. 
그리고 5개의 좌표값에 대해 서로 서로의 거리를 계산하여 가장 가까운 두 좌표값과 그 거리를 출력하라.
	struct point {
	   int x, y;
	};
*/

#include <stdio.h>
#include <math.h>

struct point {
	int x, y;
};

int main() {
	struct point arr[5];
	double dist, min;
	int index1, index2;

	for (int i = 0; i < 5; i++) {
		printf("%d번째 좌표 (x, y) 입력: ", i + 1);
		scanf_s("%d %d", &arr[i].x, &arr[i].y);
	}

	min = sqrt(pow((arr[0].x - arr[1].x), 2) + pow((arr[0].y - arr[1].y), 2));
	for (int i = 1; i < 5; i++) {
		for (int j = i + 1; j < 5; j++) {
			dist = sqrt(pow((arr[i].x - arr[j].x), 2) + pow((arr[i].y - arr[j].y), 2));

			if (dist < min) {
				min = dist;
				index1 = i;
				index2 = j;
			}
		}
	}

	printf("\n========== 가장 가까운 좌표 ==========\n");
	printf("첫번째 좌표: (%d, %d)\n", arr[index1].x, arr[index1].y);
	printf("두번째 좌표: (%d, %d)\n", arr[index2].x, arr[index2].y);
	printf("두 좌표 사이 거리: %lf\n", min);

	return 0;
}