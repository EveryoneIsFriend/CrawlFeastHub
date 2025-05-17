import requests

url = 'https://fanyi.baidu.com/sug'

str_input = input("请输入关键词：")

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Referer': 'https://fanyi.baidu.com/mtpe-individual/multimodal?query=%0A%E4%BD%A0%E5%A5%BD%0A&lang=zh2en&ext_channel=Aldtype'
    }

data = {'kw':str_input}

cookies = {'Cookie': 'BAIDUID=AA4C6CED47C490C971161BD5BAA309A1:FG=1; BIDUPSID=AA4C6CED47C490C971161BD5BAA309A1; PSTM=1555987183; H_PS_PSSID=61027_62325_62868_62890_62927_62967_63040_63048_63036_63148_63112_63178; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_YWM2MjU2ZTNkNjBhNDUyNzZkNzdiYmVjNDc4MjZkZjcxYTIyZWFiNjU0MGJhMzcxYTMzMWRjYTg4YWZjZTNhNmRhOWEyMjBjNGFmZDMzMTczZWQxZjBhYzRlZTdjN2Q0YjFlMjZlODI4Yjg3ZGMzNTVhOTU4ODJmMWQwY2E1MDNhZjAwNjBlNjk0MWJjNDQwMzE3MDFiZGY4ZWY4ZmUzMA==; BAIDUID_BFESS=AA4C6CED47C490C971161BD5BAA309A1:FG=1; BCLID=8406142754637781363; BCLID_BFESS=8406142754637781363; BDSFRCVID=dYKOJexroGWN3M5syseabZsvOeKK0gOTDYrEqkhrnY7IiU4Vvfe5EG0PtOi2xEPM4ch-ogKKymOTHr4F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=dYKOJexroGWN3M5syseabZsvOeKK0gOTDYrEqkhrnY7IiU4Vvfe5EG0PtOi2xEPM4ch-ogKKymOTHr4F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JR4H_CIhfCK3fP36q4Oo5tD_hgT22-us5N5i2hcHMPoosU38DUFhKnFybfQaXJJqBKTiaKJjBMbUotoHKtRsK4C4jPr0L63pbDc-_l5TtUJM8nI42MomXj0SM2cyKMniMCj9-pn-JpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjQ3DN083f; H_BDCLCKID_SF_BFESS=JR4H_CIhfCK3fP36q4Oo5tD_hgT22-us5N5i2hcHMPoosU38DUFhKnFybfQaXJJqBKTiaKJjBMbUotoHKtRsK4C4jPr0L63pbDc-_l5TtUJM8nI42MomXj0SM2cyKMniMCj9-pn-JpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjQ3DN083f; RT="z=1&dm=baidu.com&si=4b1a32e2-bad8-4739-89d4-40c0de9e52d9&ss=mac50p0n&sl=g&tt=dyi&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1frky"'}

response = requests.post(url=url, data=data, cookies=cookies, headers=headers)

content = response.json()

for i in content['data']:
    print(i['k'],i['v'])