"""
The vertices of polygon P have coordinates (x1, y1), (x2, y2), · · · , (xn, yn), numbered
either in a clockwise or counter clockwise way. The area P of the polygon can be
computed by just knowing the boundary coordinates:

Assume that x and y are either lists or arrays. Implement the function to compute the
area of a polygon and test your function on a triangular, a quadrilateral, and a
pentagon where you can calculate the area by alternative methods for computation.
"""

n = int(input('input the number of vertex : '))
arr = []
for i in range(n):
    x, y = map(int, input('input x, y : ').split())
    arr.append([x, y])

area = 0
for i in range(n):
    if i == n-1:
        area += arr[i][0]*arr[0][1] - arr[i][1]*arr[0][0]
    else:
        area += arr[i][0]*arr[i+1][1] - arr[i][1]*arr[i+1][0]

print('area of polygon', abs(area)*0.5)