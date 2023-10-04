import requests
def getexp(file_path,key='K87420617888957'):
    url = 'https://api.ocr.space/parse/image'
    file_path = file_path
    file = open(file_path, 'rb')
    files = {'file': file}
    data = {
        "apikey": key,
        "language": "eng",
    }
    response = requests.post(url, files=files, data=data)
    if response.status_code != 200:
        print('error')
        return 'error'
    result = response.json()['ParsedResults'][0]['ParsedText'].replace(',', '').replace('+', '')
    file.close()  # 关闭文件
    if result == '':
        print('获得经验：' + result)
        return 'error'
    else:
        print('获得经验：' + result)
        return result
if __name__=="__main__":
    expocr('./imgs/exp.png')