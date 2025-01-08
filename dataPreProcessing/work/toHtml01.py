import pandas as pd
csvRead = pd.read_csv(r"D:\pythonCode01\data\crawlingFile\realData\okky\okkyLifeStoryFirstPageUp500Es5.csv")


csvRead['content'] = csvRead['content'].apply(dm.timeConvert)
csvRead['viewCount'] = csvRead['viewCount'].apply(dm.convert_k_to_numbers)
csvRead.to_csv(r"D:\pythonCode01\data\crawlingFile\processedData\okky01.csv",encoding ='utf8',index = False)
