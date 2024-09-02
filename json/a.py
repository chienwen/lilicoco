import json
import re

# 定義全域變數 haha，用於存放擷取到的 IBAN
haha = []

# 假設 foo 函式
def foo(input_string):
    # 正則表達式，用來匹配 IBAN
    iban_pattern = r'\b[A-Z]{2}[0-9]{2}\s?([A-Z0-9]{1,4}\s?){1,7}\b'
    
    # 搜尋是否有符合的 IBAN
    match = re.search(iban_pattern, input_string)
    
    if match:
        # 如果有匹配到，將其擷取出來並放入 haha 陣列中
        iban = match.group(0)
        haha.append(iban)
        print(f"Found IBAN: {iban}")
    #else:
    #    print(f"No IBAN found in: {input_string}")

def process_strings(data):
    if isinstance(data, dict): # {}
        for value in data.values():
            process_strings(value)
    elif isinstance(data, list): # []
        for item in data:
            process_strings(item)
    elif isinstance(data, str): # 字串
        foo(data)
    # 如果資料不是字串、列表或字典，則忽略

# 定義 yoyo 函式，用於去除字串的前後空白
def yoyo(input_string):
    a = input_string.replace(" ", "")
    # regular expression 判斷
    return a

def main():
    # 讀取 input.json 檔案
    with open('input.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 處理 JSON 裡面的所有字串
    process_strings(data)

    # 使用 yoyo 函式處理每個 IBAN
    cleaned_haha = list(map(yoyo, haha))

    # 將結果寫入 output.json 檔案
    with open('output.json', 'w', encoding='utf-8') as outfile:
        json.dump(cleaned_haha, outfile, ensure_ascii=False, indent=4)

main()

