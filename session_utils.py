from requests.models import Response
from requests.sessions import Session
from credentials import email, password

"""
Data and Headers generated with
https://curl.trillworks.com/
"""

headers = {
    'authority': 'www.looperman.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://www.looperman.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.looperman.com/account/login',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'loop_csrfc=; loop_session=',
}

data = {
  'csrftoken': '',
  'user_email': '',
  'upass': '',
  'user_remember_code': '1',
  'user_disclaimer': '1',
  'submit': 'submit'
}

LOGIN_URL = 'https://www.looperman.com/account/login'

def login(session:Session):
  email.replace("@", "^%^40")
  data["user_email"] = email
  data["upass"] = password

  __set_headers__(session)

  session.post(LOGIN_URL, headers=headers, data=data)

"""
Sets cookie in header csfrtoken in data 
(tokens are generated by looperman therefore we need a get request)
"""
def __set_headers__(session : Session):
  loop_session = ""
  loop_csrfc = ""

  r :Response = session.get(LOGIN_URL)
  set_cookies = r.headers['Set-Cookie'].split(";")

  for cookie in set_cookies:
    if "loop_csrfc" in cookie:
      loop_csrfc = cookie.split("=")[-1]
    elif "loop_session" in cookie:
      loop_session = cookie.split(",")[-1].split("=")[-1]

  data['csrftoken'] = loop_csrfc
  headers['cookie'] = f"loop_csrfc={loop_csrfc}; loop_session={loop_session}"