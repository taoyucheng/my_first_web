from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_weather():
    response = urlopen(url='http://www.weather.com.cn/weather/101270101.shtml')
    response_text = BeautifulSoup(response,"html.parser")
    today = response_text.find('p',class_ = 'tem')
    try:
        tempratureHigh = today.span.string
    except AttributeError as e:
        tempratureHigh = today.find_next('p', class_='tem').span.string
    tempratureLow = today.i.string
    weather = response_text.find('p',class_ = 'wea').string
    weather_attr = weather.find_previous('big').attrs['class'][1]
    # print(tempratureHigh,tempratureLow,weather,weather_attr)
    return {
        'weather':weather,
        'tempratureHigh':tempratureHigh,
        'tempratureLow':tempratureLow,
        'weather_attr':weather_attr
    }



