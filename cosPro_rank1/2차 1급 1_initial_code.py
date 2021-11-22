from abc import *
 
    
class Book(metaclass=ABCMeta):
    @abstractmethod
    def get_rental_price(self, day):
        pass
    
    
class ComicBook(Book):
    def get_rental_price(self, day):
        cost = 500
        day -= 2
        if day > 0:
            cost += day*200
        return cost
    
    
class Novel(Book):
    def get_rental_price(self, day):
        cost = 1000
        day -= 3
        if day > 0:
            cost += day*300
        return cost
    
    
def solution(book_types, day):
    books = []
    for x in book_types:
        if x == "comic":
            books.append(ComicBook())
        else:
            books.append(Novel())
    total_price = 0
    print(books)
    for x in books:
        total_price += x.get_rental_price(day)
    return total_price


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
book_types = ["comic", "comic", "novel"]
day = 4
ret = solution(book_types, day)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")