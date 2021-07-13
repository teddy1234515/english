import os

nowPath = "."   # . 代表目前路徑(程式存在的路徑)

pathList = os.listdir(nowPath)

# 讀取目前路徑有的檔案
for i in pathList:

    # 只讀取 txt 檔
    if i.endswith(".txt"):
        with open(i,'r+',encoding="utf-8") as f:
            # 將每一行讀區並加入 data_raw 列表
            data_raw = f.read().splitlines()
            # 得到列表中最長字的長度
            maxLen = len(max(data_raw,key = len))
            # 暫時儲存區, 等等用來存放『英文』與『翻譯』
            save_temporarily = []
            # 將『英文』與『翻譯』分開
            for j in range(len(data_raw)):
                wordSplit = data_raw[j].split()
                save_temporarily.append(wordSplit)
            f.truncate(0)    # 清空目前的檔案
            # 使用 truncate(0) 清空後,      (接下行)
            # 需要使用 seek(0)移到檔案的開頭 (接下行)
            # 不然字就不會從開頭開始寫了
            f.seek(0)
            for k in save_temporarily:
                f.write(k[0] +
                        " "*(maxLen-len(k[0])) + 
                        k[1] +
                        "\n")
            save_temporarily = []