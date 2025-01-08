import pandas as pd
csvRead = pd.read_csv(r"D:\pythonCode01\data\crawlingFile\realData\okky\okkyLifeStoryFirstPageUp500Es5.csv")
# csvRead = pd.read_csv(r"D:\pythonCode01\data\crawlingFile\realData\okky\okkyLifeStoryLastPage.csv")

# DataFrame에서 row추출
newDf = csvRead.iloc[3:6] # 샘플 데이터 추출
aa01 = newDf['content'].str.replace('\r\n', '<br>')
aa02 = aa01.str.replace('\n', '<br>')
aa03 = aa02.str.replace('\r', '<br>')
print(aa03)


# csvRead['createAt'] = csvRead['createAt'].apply(dm.timeConvert)