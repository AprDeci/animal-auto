from ocr.PPOCR_api import GetOcrApi
import os.path as path
ocr = GetOcrApi('./PaddleOCR-json_v.1.3.0/PaddleOCR-json.exe')
def getexp(img_path):
    img = path.abspath(img_path)
    result = ocr.run(img)
    if type(result) == str:
        print('error')
        return 'error'
    else:
        exp = result['data'][-1]['text'].replace('.', '').replace('+', '').replace(',', '')
        print(f'paddleOcr:{exp}')
        return exp
