# loveAPI
Оболочка для API которое позволяет получить доступ к милым сообщениям для парня/девушки
Для получения сообщений используется [smsta.ru](https://smsta.ru/)
Данные обрабатываются BeautifulSoup4

# Quick start
* `git clone https://github.com/freQuensy23-coder/loveAPI`
* Use in your python file
```Python
from API import API
from config import endpoint

love_api = API()
love_msg = api.get_random_msg(endpoints=[ENDPOINTS["her"]["quit"]])
print(msg)
```
Result:
```
Говорю тебе — прощай, отношения прекращаю.
В мыслях последний поцелуй отправляю.
Прими это смс, а меня из жизни удали,
Ведь наши мосты мы давно развели. 
```

### More examples in examples folder