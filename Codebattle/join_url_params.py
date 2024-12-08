"""Вернуть строку запроса (URL), созданную на основе адреса и словаря
параметров. Параметры в результирующей строке должны быть упорядочены по
алфавиту."""


def solution(url: str, params: dict[str, str]):
    result = f'{url}?'
    for key, value in sorted(params.items()):
        result += key + '=' + value + '&'
    result = result.rstrip('&')
    return result


print("http://www.foobar.com?first_param=test&second_param=some&third_param=clj"
      == solution("http://www.foobar.com",
                  {"first_param": "test", "second_param":
                      "some", "third_param": "clj"}))

print("http://www.example.com/search?q=findme&useragent=chrome" == solution(
    "http://www.example.com/search",
    {"q": "findme", "useragent": "chrome"}))

print("http://authority.com?smile=weight&steam=metal&surprise=connection" ==
      solution("http://authority.com", {"smile": "weight",
                                        "surprise": "connection", "steam":
                                            "metal"}))
