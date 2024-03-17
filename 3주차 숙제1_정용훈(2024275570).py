# 교수님 안녕하세요. 3주차 tuple 숙제 입니다.

print("1번 문제 : Consider the following tuple :")
# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
print(genres_tuple)
# 교수님 Tuples(학생용).ipynb 에서 genres_tuple이 한줄로 출력되는 것 처럼 보여서
# 해당 Quiz도 한줄로 출력하게 하겠습니다.
print("(예외) 배포해주신 Tuples(학생용).ipynb 처럼 한줄로 보이기")
genres_tuple_imsi = ("('pop'", "'rock'", "'soul'", "'hard rock'", "'soft rock'", "'R&B'", "'progressive rock'", "'disco')")
for line in genres_tuple_imsi :
    print(line)
print("========================================")
print ("2번 문제 : Find the length of the tuple, genres_tuple")
length_of_tuple = len (genres_tuple)
print("length of tuple : ", length_of_tuple)
print("========================================")
print("3번 문제 : Access the element, with respect to index 3:")
genres_tuple[3]
NestedT = genres_tuple[3]
print("[3]번 인덱스는? ",NestedT)
print("========================================")
print("4번 문제 : Use slicing to obtain indexes 3, 4 and 5 :")
genres_tuple_slicing = genres_tuple[3:6]
print("슬라이싱 3번~6번 범위는? ", genres_tuple_slicing)
print("========================================")
print("5번 문제 : Find the first two elements of the the tuple genres_tuple :")
genres_tuple_elements = genres_tuple[0:2]
print("1, 2의 요소는 : ", genres_tuple_elements)
print("========================================")
print("6번 문제 : Find the first index of 'disco' :")
genres_tuple_find = genres_tuple.index("disco")
print("찾는 것에 대한 인덱스 번호 : ", genres_tuple_find)
print("========================================")
print("7번 문제 : Generate a sorted List from the Tuple 'C_tuple = (-5, 1, -3)'")
C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
print("C_tuple을 정렬하면 ? :", C_list)
print("========================================")
# 감사합니다
