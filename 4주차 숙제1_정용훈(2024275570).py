# 4주차 숙제
print("1번 문제 : Write an if statement to determine if an album had a rating greater than. "
      "8 Test it using the rating for the album 'Back in Black' that had a rating of 8.5."
      "If the statement is true print 'This album is Amazing!'")
rating_1 = 8.5
print("rating_1 입력 값 : ", rating_1)
if rating_1 > 8:
    print("1번 문제 정답 : This album is Amazing!")
#else: #그냥 'This album is Amazing!'만 하드코딩되어 출력될 것 같아 else문을 설정해보았습니다.
  #  print("I'm sorry to hear that.")
print("========================================")
print("2번 문제 : Write an if-else statement that performs the following."
      "If the rating is larger then eight print 'this album is amazing'."
      "If the rating is less than or equal to 8 print 'this album is ok.' ")
rating_2 = 8.5
print("rating_2 입력 값 : ", rating_2)
if rating_2 > 8:
    print("2번 문제 정답 : this album is amazing")
else:
    print("2번 문제 정답 : this album is ok")
print("========================================")
print("3번 문제 : Write an if statement to determine if an album came out before 1980 or in the years : 1991 or 1993."
      "If the condition is true print out the year the album came out. ")
album_release_year = 1979
print("앨범 발매 연도 입력 : ", album_release_year)
if album_release_year < 1980 or album_release_year == 1991 or  album_release_year == 1993:
    print("3번 문제 정답 : this album came out already")
print("========================================")

