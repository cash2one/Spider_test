import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def _parse_url(url):  # 解析url,return html_str
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    # proxies = {'http': 'http://125.45.87.12:9999'}
    response = requests.get(url, headers=headers, timeout=5,) # proxies=proxies)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except Exception as e:
        print(e)
        html_str = None
    return html_str
