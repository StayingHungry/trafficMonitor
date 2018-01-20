from flask import Flask
import requests
import re
import json


app = Flask(__name__)








@app.route('/')
def hello_world():
    url_baidu = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%8C%97%E4%BA%AC%E5%91%A8%E4%B8%80%E9%99%90%E8%A1%8C&oq=%25E5%258C%2597%25E4%25BA%25AC%25E4%25BB%258A%25E5%25A4%25A9%25E9%2599%2590%25E8%25A1%258C&rsv_pq=ab82e4170000bac5&rsv_t=07d9ZFxoNF%2Fb%2F3UU9ny%2FdkK%2Fwrkp7ynAWRryGuPRpiaWeXCX0WksYY9%2Fw6I&rqlang=cn&rsv_enter=1&rsv_sug3=13&rsv_sug1=11&rsv_sug7=100&rsv_sug2=0&inputT=4385&rsv_sug4=4961"


    headers = {
        'cache-control': "no-cache",
        'postman-token': "97c916e2-33c6-13db-8696-2612827fee83",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        }

    response_baidu = requests.request("GET", url_baidu, headers=headers).content
    # print type(response_baidu)

    number_baidu = re.findall('op_traffic_off">\d</div>',response_baidu)
    if len(number_baidu)==0:
        traffic_baidu = "Null"
    else:
        traffic_baidu = ",".join(number_baidu)
    # print(response.text)


    url_sogou = "https://wap.sogou.com/web/searchList.jsp?uID=PqrJOEMiHW-0_peB&v=5&from=index&w=1274&t=1516436174557&s_t=1516436180465&s_from=index&keyword=%E5%8C%97%E4%BA%AC%E9%99%90%E8%A1%8C&pg=webSearchList&suguuid=6594816b-eaf7-4816-bdd6-2585e65ecb4d&sugsuv=AAHdpkHJHQAAAAqZCjNscgAAkwA%3D&sugtime=1516436180467"

    headers = {
        'cache-control': "no-cache",
        'postman-token': "97c916e2-33c6-13db-8696-2612827fer83",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        }
    response_sogou = requests.request("GET", url_sogou, headers=headers).content
    number_sogou = re.findall('op_traffic_off">\d</div>',response_sogou)
    if len(number_sogou) == 0:
        traffic_sogou = "Null"
    else:
        traffic_sogou = ",".join(number_sogou)

    if traffic_sogou != traffic_baidu:
        isEqual = False
    else:
        isEqual = True

    diffResult = json.dumps({"baiduNumber":traffic_baidu,"sogouNumber":traffic_sogou,"diffResult":str(isEqual)})
    return diffResult


if __name__ == '__main__':
    app.run(host="",port="8787")
