import imp
from platform import python_branch
from tkinter import Button
from xml.dom.pulldom import SAX2DOM
from matplotlib.animation import TimedAnimation
import streamlit as st
import numpy as np
import pandas as pd
import time
import json
#写真用
from PIL import Image
# #お天気APIを取得
import requests
# #GUIアプリの作成
# import tkinter as tk
from time import sleep
from datetime import datetime

# def confirm_aqc(data:list) -> str:
#   """
#   品質情報を確認し、データを文字列で返す
#   input : list
#   return : str
#   """
#   if data[1] == 0:
#     return str(data[0])
#   else:
#     return "品質情報を確認して下さい"

# def find_index(data:list, code:str) -> int:
#   """
#   対象のエリアのデータが格納されているインデックス番号を返す
#   input : list
#   return : int
#   """
#   index = [num for num, i in enumerate(data) if i["area"]["code"] == code][0]
#   return index

# latest_time_url = "https://www.jma.go.jp/bosai/amedas/data/latest_time.txt"
# latest_time_req = requests.get(latest_time_url)
# latest_datetime = datetime.strptime(latest_time_req.text, "%Y-%m-%dT%H:%M:%S%z") # タイムゾーン込みで日時文字列をdatetime型へ
# yyyymmdd = latest_datetime.strftime('%Y%m%d') # 年月日　- アメダスデータ取得時に必要
# h3 = ("0" + str((latest_datetime.hour//3)*3))[-2:] # 3時間ごとの時間 - アメダスデータ取得時に必要
# area = "130000" # エリア番号 - 今回は東京都
# detail_area = "130010" # 詳細の予報エリア番号 - 今回は東京地方
# stnid = "44132" # 観測所番号 - 今回は千代田区 北の丸公園

# # 天気概況
# overview_forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area}.json"
# overview_forecast_req = requests.get(overview_forecast_url)
# overview_forecast_data = overview_forecast_req.json() # 天気概況
# overview_forecast_text = "\n".join(overview_forecast_data["text"].split())

# # 天気予報
# forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area}.json"
# forecast_req = requests.get(forecast_url)
# forecast_data = forecast_req.json()
# forecast_data = forecast_data[0]["timeSeries"][0]["areas"] #エリア毎の予報データ（天気, 風速, 風向...etc）が格納
# forecast_data_target_index = find_index(forecast_data, detail_area)
# weathers = forecast_data[forecast_data_target_index]["weathers"] # 天気
# tommorow_weather = " ".join(weathers[1].split())

# # アメダス (地点)
# amedas_url = f"https://www.jma.go.jp/bosai/amedas/data/point/{stnid}/{yyyymmdd}_{h3}.json"
# amedas_req = requests.get(amedas_url)
# amedas_data = amedas_req.json()
# latest_key = max(amedas_data) # 最新のアメダスデータが入っているkey
# latest_temp = confirm_aqc(amedas_data[latest_key]["temp"]) # 最新の気温データを取得, 品質情報を確認
# latest_precipitation10m = confirm_aqc(amedas_data[latest_key]["precipitation10m"]) # 最新の降水量データを取得, 品質情報を確認

# st.write(f"現在の気温 : {latest_temp} 度")
# st.write(f"現在の降水量(10分あたり) : {latest_precipitation10m} mm")
# st.write(f"翌日の天気: {tommorow_weather}")
# st.write(f"天気概況 : {overview_forecast_text}")

# def __init__(self):
    


a = ("Arial black", 20, "bold")

st.title('Brain training m2')

text = st.text_input('あなたの名前を教えて下さい')
condition = st.slider('難易度を選んでください', 1, 5, 1)


# def difselect(cond):
    # if cond == 1:
    #     st.write('rule1')
    # elif cond == 2:
    #     st.write('rule2')
    # elif cond == 3:
    #     st.write('rule3')
    # elif cond == 4:
    #     st.write('rule4')
    # else:
    #     st.write('rule5')

button1 = st.button('ルールについて')

readychk = False

if button1 == True:
    # def difselect(condition):
    #     return
    if condition == 1:
        st.write('rule1')
    elif condition == 2:
        st.write('rule2')
    elif condition == 3:
        st.write('rule3')
    elif condition == 4:
        st.write('rule4')
    else:
        st.write('rule5')
    
# if readychk == True:
#     break
# readychk == st.checkbox('Are you Ready?')
        
st.write('Are you ready to start Level', condition, 'training?')


if __name__ == "__main__":
    pushbtn = 0




# 'あなたの趣味:', text
# 'コンディション:', condition

# st.write('DataFrame')
# st.write('Display Image')
# st.write('Interactive Widgets')

# option1 = 0

# left_column,  center_column, right_column = st.columns(3)
# # left_column2,  right_column2 = st.columns(2)
# button1 = left_column.button('DataFrame1')
# button2 = left_column.button('DataFrame2')
# button3 = right_column.button('Game start')


# セレクトボックス
# option = st.selectbox(
#     'あなたの好きな数字を教えて下さい。',
#     list(range(1, 11))    
# )
# 'あなたの好きな数字は', option, 'です。'

# 入力値出力
# text = st.text_input('あなたの趣味を教えて下さい')
# 'あなたの趣味:', text

# 指定の値の間をスライド(最小値、最大値、初期値)
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition

# カードを通して

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')



# print(TimedAnimation)
# = timedatetime.strptime(latest_time_req.text, "%Y-%m-%dT%H:%M:%S%z") # タイムゾーン込みで日時文字列をdatetime型へ

#target_time = 10
 

# if button3:
#     def up_timer(secs):
#         for i in range(0,secs):
#             st.write(i)
#             sleep(1)
#         st.write("時間です！")


#     up_timer(target_time)


# if button1:
# #    セレクトボックス
#     option1 = st.selectbox(
#         'DataFrame1',
#         list(range(1, 11))    
#     )

# if button2:
# #    セレクトボックス
#     option2 = st.selectbox(
#         'DataFrame2',
#         list(range('a', 'e'))    
#     )

# if button3:
# #    セレクトボックス
#     option3 = st.selectbox(
#         'DataFrame3',
#         list(['A', 'B', 'C', 'D', 'E'])    
#     )

# if option1 == True:
#     list.append(option1)


# st.center_colum.button('DataFrame')
# button2 = left_column2.button('DataFrame')

# if button2:
#     right_column.write('ここは右カラム')

# button = left_column.button('右カラムに文字を表示')
# button = left_column.button('右カラムに文字を表示')

# if button:
#     right_column.write('ここは右カラム')


# text = st.sidebar.text_input('あなたの趣味を教えて下さい')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:', text
# 'コンディション:', condition



expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容3の回答')

# サイドバーに表示できる
# st.sidebar.write('Interactive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:', text
# 'コンディション:', condition

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

#チェックボックスの判定
# if st.checkbox('Show Image'):
#     #写真の設定
#     img = Image.open('yamazaki.jpg')
#     # 写真の表示
#     st.image(img, caption='yamazaki hiromasa', use_column_width=False)

# マップの表示
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], 
#     columns=['lat', 'lon']
# )
# st.map(df)

# グラフの表示
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# 折れ線グラフの表示
# st.line_chart(df)
# 折れ線グラフの下を塗ったものを表示
# st.area_chart(df)
# 棒グラフの表示
# st.bar_chart(df)

# 表の表示
# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40],
# })
# st.write(df)
# dataframeでは高さ幅を指定できる
# st.dataframe(df, width=1000, height=500)
#axisは列の時は0行の時は1を入れる

# st.dataframe(df.style.highlight_max(axis=0))
# staticな表を作成する場合はtableを使う
# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

#ソースコードの表示
```python
import streamlit as st
import numpy as np
import pandas as pd
```

#シンプルにの表示
...python
import streamlit as st
import numpy as np
import pandas as pd
...

"""



