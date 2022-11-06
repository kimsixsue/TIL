def solution(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book) - 1):
        if phone_book[idx + 1].startswith(phone_book[idx]):
            return False
    answer = True
    return answer
