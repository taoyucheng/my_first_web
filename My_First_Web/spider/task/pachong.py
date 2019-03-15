import requests
import re

def get_data(keyword,pages):
      params = []
      urls = []
      results = []
      for i in range(30*pages,30*pages+30,30):
            params.append(
                  {
                        'tn': 'resultjson_com',
                        'ipn': 'rj',
                        'ct': 201326592,
                        'is': '',
                        'fp': 'result',
                        'queryWord': keyword,
                        'cl': 2,
                        'lm': -1,
                        'ie': 'utf-8',
                        'oe': 'utf-8',
                        'adpicid': '',
                        'st': -1,
                        'z': '',
                        'ic': 0,
                        'word': keyword,
                        's': '',
                        'se': '',
                        'tab': '',
                        'width': '',
                        'height': '',
                        'face': 0,
                        'istype': 2,
                        'qc': '',
                        'nc': 1,
                        'fr': '',
                        'pn': i,
                        'rn': 30,
                        'gsm': '1e',
                        '1526377465547': ''
                  }
            )
      url = "https://image.baidu.com/search/acjson"
      # url_pattern = re.compile(r'''objURL":"(.*?)"''')
      for i in params:
            urls.append(requests.get(url,params=i).json().get('data'))
      for dict in urls:
            for obj in dict:
                  if obj.get('thumbURL'):
                        results.append(obj.get('thumbURL'))
      return results
