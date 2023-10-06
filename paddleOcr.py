from ocr.PPOCR_api import GetOcrApi
import os.path as path
ocr = GetOcrApi('./PaddleOCR-json_v.1.3.0/PaddleOCR-json.exe')
def getexp(img_path):
    img = path.abspath(img_path)
    try:
        result_pending = ocr.run(img)
    except:
        return  'error'
    result = result_pending['data']
    if type(result) == str:
        print('error')
        return 'error'
    else:
        exp = result[-1]['text'].replace('.', '').replace('+', '').replace(',', '')
        print(f'paddleOcr:{exp}')
        return exp

if __name__ == '__main__':
    getexp('./imgs/exp.png')