import requests

# توكن
token =input(" Token :")
#ايدي
id = input(" id  :")
# رسالة لتوصل لبوت
masg = input(" masg  :")


req = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={masg}')

