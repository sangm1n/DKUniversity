# AI homework by sangmin
from simpleai.search import CspProblem, backtrack

def constraint_func(names, values):
    return values[0] != values[1]

if __name__ == '__main__':
    names = ('인천', '경기', '강원', '경북', '울산', '충북', '전북', '대구',
             '충남', '대전', '경남', '부산', '광주', '전남', '독도', '제주도')
    colors = dict((name, list(i for i in range(1, len(names) + 1))) for name in names)

constraints = [
(('인천', '경기'), constraint_func), (('경기', '강원'), constraint_func),
(('경기', '충북'), constraint_func), (('경기', '충남'), constraint_func),
(('강원', '충북'), constraint_func), (('강원', '경북'), constraint_func), 
(('경북', '충북'), constraint_func), (('경북', '전북'), constraint_func),
(('경북', '대구'), constraint_func), (('경북', '울산'), constraint_func),
(('경북', '경남'), constraint_func), (('울산', '경남'), constraint_func),
(('울산', '부산'), constraint_func), (('충북', '충남'), constraint_func),
(('충북', '대전'), constraint_func), (('충북', '전북'), constraint_func),
(('부산', '경남'), constraint_func), (('경남', '대구'), constraint_func),
(('경남', '전북'), constraint_func), (('경남', '전남'), constraint_func),
(('경남', '전남'), constraint_func), (('전남', '광주'), constraint_func),
(('전남', '전북'), constraint_func), (('전북', '충남'),constraint_func),
(('충남', '대전'), constraint_func)
]

problem = CspProblem(names, colors, constraints)

output = backtrack(problem)
print('<< Color mapping >>\n')
min_color = 0
for k, v in output.items():
    if v == 1:
        print(k, '==> red')
    elif v == 2:
        print(k, '==> green')
    elif v == 3:
        print(k, '==> blue')
    elif v == 4:
        print(k, '==> black')
        
    if min_color < v:
        min_color = v
print('\nNumber of Color:', min_color)