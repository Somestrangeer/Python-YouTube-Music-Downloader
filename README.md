# About the project

This project is multi-thredaded and provides users with listening to music that is limited in their own contry, without constantly turning on VPN.
The project is based on pytube and pyTelegramBotAPI

# Advantages
- Bot can download any music video from YouTube
- It's the fastest bot to get audio from YouTube
- It's multi-thredaded

# Test the project

At any time you can test the bot by the link: [click](t.me/Musik_Youtube_Bot)

# Pytube problem

If you try to use pytube now (12.0.0 version) then you'll get an error: 
>pytube: 'NoneType' object has no attribute 'span'

To solve this problem, you have to go to thhis way: 
>C:\Users\yoyr user\PycharmProjects\your project\venv\Lib\site-packages\pytube\cipher.py

In **cipher.py** you have to find the function **get_throttling_function_name()** and replace that code on this:

```
def get_throttling_function_name(js: str) -> str:
"""Extract the name of the function that computes the throttling parameter.

:param str js:
    The contents of the base.js asset file.
:rtype: str
:returns:
    The name of the function used to compute the throttling parameter.
"""
function_patterns = [
    # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
    # a.C&&(b=a.get("n"))&&(b=Dea(b),a.set("n",b))}};
    # In above case, `Dea` is the relevant function name
    r'a\.[A-Z]&&\(b=a\.get\("n"\)\)&&\(b=([^(]+)\(b\)',
]
logger.debug('Finding throttling function name')
for pattern in function_patterns:
    regex = re.compile(pattern)
    function_match = regex.search(js)
    if function_match:
        logger.debug("finished regex search, matched: %s", pattern)
        function_name = function_match.group(1)
        is_Array = True if '[' or ']' in function_name else False
        if is_Array:
            index = int(re.findall(r'\d+', function_name)[0])
            name = function_name.split('[')[0]
            pattern = r"var %s=\[(.*?)\];" % name
            regex = re.compile(pattern)
            return regex.search(js).group(1).split(',')[index]
        else:
            return function_name

raise RegexMatchError(
    caller="get_throttling_function_name", pattern="multiple"
)
```
