# 5주차 숙제
print("1번 문제 : Write a for loop the prints out all the element between '-5' and '5' using the range fucntion.")
for i in range(-5, 6):
    print("1번 문제 정답 : ", i)
print("=============================")
print("2번 문제 : Print the elements of the following list : 'Genres=['rock', 'R&B', 'Soundtrack', R&B', 'soul', 'pop']'"
      "Make sure your follow Python conventions.")
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print("2번 문제 정답 : ", Genre)
print("=============================")
print("3번 문제 : Write a for loop that prints out the following list : "
      "'squares = ['red', 'yellow', 'green', 'purple', 'blue']")
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print("3번 문제 정답 : ", square)
print("=============================")
print("4번 문제 : Write a while loop to display the values of the Rating of an album playlist stored in the list"
      "'PlayListRatings', If the score is less than 6, exit the loop."
      "The list 'PlayListRatings' is given by : 'PlayListRatings = [10, 9.5, 10, 8, 7,5, 5, 10, 10]")
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >= 6):
    print("4번 문제 정답 : ", Rating)
    Rating = PlayListRatings[i]
    i = i + 1
print("=============================")
print("5번 문제 : Write a while loop to copy the strings 'orange' of the list 'squares' to the list 'new_squares'."
      "Stop and exit the loop if the value on the list is not 'orange' :")
squares = ['orange', 'orange', 'purple', 'blue', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
    print(new_squares)
print("=============================")
#감사합니다.
