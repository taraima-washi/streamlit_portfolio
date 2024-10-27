import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

st.header('レッスン11: スライダーとセレクトボックス')

columns_to_plot = st.multiselect('プロットする列を選択', ['A', 'B', 'C', 'D'],
default=['A', 'B'], key='column_multiselect')
num_points = st.slider('データポイント数', min_value=50, max_value=1000,
value=200, step=50, key='points_slider')
data_sample4 = pd.DataFrame(np.random.randn(num_points, 4), columns=['A',
'B', 'C', 'D'])
fig4 = go.Figure()
for col in columns_to_plot:
    fig4.add_trace(go.Scatter(x=data_sample4.index, y=data_sample4[col],
    mode='lines+markers', name=col))
st.plotly_chart(fig4)


data_sample3 = pd.DataFrame(np.random.randn(200, 2), columns=['M', 'N'])
color_option = st.selectbox('マーカーの⾊を選択', ['blue', 'red', 'green','purple'], key='color_select')
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=data_sample3['M'], y=data_sample3['N'],
mode='markers', marker=dict(color=color_option)))
st.plotly_chart(fig3)


data_sample2 = pd.DataFrame(np.random.uniform(0, 100, size=(1000, 2)), columns=['P', 'Q'])
range_values = st.slider('値の範囲を選択', min_value=0.0, max_value=100.0,
                                value=(25.0, 75.0), key='range_slider')
filtered_data = data_sample2[(data_sample2['P'] >= range_values[0]) &
                                (data_sample2['P'] <= range_values[1])]
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=filtered_data['P'], y=filtered_data['Q'], mode='markers'))
st.plotly_chart(fig2)


sample_size = st.slider('サンプルサイズを選択', min_value=10, max_value=1000, value=100, step=10, key='sample_slider')
data_sample1 = pd.DataFrame(np.random.randn(sample_size, 2), columns=['X', 'Y'])
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data_sample1['X'], y=data_sample1['Y'], mode='markers'))
st.plotly_chart(fig1)


column_options = st.multiselect(
    '表⽰する列を選択してください',
    ['X', 'Y', 'Z'],
    ['X', 'Y'],
    key='column_selection')

sample_data = pd.DataFrame(np.random.randn(10, 3), columns=['X', 'Y', 'Z'])
st.write(sample_data[column_options])


if 'counter' not in st.session_state:
    st.session_state.counter = 0
col1, col2, col3 = st.columns(3)
if col1.button('カウントアップ', key='count_up'):
    st.session_state.counter += 1
if col2.button('カウントダウン', key='count_down'):
    st.session_state.counter -= 1
if col3.button('リセット', key='reset_count'):
    st.session_state.counter = 0
st.write(f"現在のカウント: {st.session_state.counter}")

show_chart = st.checkbox('チャートを表⽰', key='show_chart')
if show_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y',
'Z'])
    fig = go.Figure()
    for column in chart_data.columns:
        fig.add_trace(go.Scatter(x=chart_data.index, y=chart_data[column],
mode='lines', name=column))
    st.plotly_chart(fig)

st.header('レッスン10: ボタンとチェックボックス')
if st.button('データを⽣成', key='generate_data'):
    random_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y',
'Z'])
    st.write(random_data)










st.header('レッスン9: セッション状態の管理')

if 'count' not in st.session_state:
    st.session_state.count = 0

st.write(f"現在のカウント: {st.session_state.count}")

if st.button('カウントアップ'):
    st.session_state.count += 1
    st.rerun()

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""
user_name = st.text_input("ユーザー名", value=st.session_state.user_name)
user_email = st.text_input("メールアドレス",
value=st.session_state.user_email)
if st.button("ユーザー情報を保存"):
    st.session_state.user_name = user_name
    st.session_state.user_email = user_email
    st.success("ユーザー情報が保存されました！")
st.write(f"セッションに保存されたユーザー名: {st.session_state.user_name}")
st.write(f"セッションに保存されたメールアドレス: {st.session_state.user_email}")

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['商品', '価格'])

product = st.text_input("商品名を⼊⼒")
price = st.number_input("価格を⼊⼒", min_value=0)

if st.button("商品データを追加"):
    new_data = pd.DataFrame({'商品': [product], '価格': [price]})
    st.session_state.df = pd.concat([st.session_state.df, new_data],
                                    ignore_index=True)
st.write("現在の商品データ:")
st.write(st.session_state.df)

if st.button("データをリセット"):
    st.session_state.df = pd.DataFrame(columns=['商品', '価格'])
    st.rerun()


st.header("レッスン8: キャッシュを使⽤したパフォーマンス最適化")

@st.cache_data(ttl=10)
def get_current_time():
    return pd.Timestamp.now()


st.subheader("キャッシュの無効化")
st.write("現在時刻（10秒ごとに更新）:")
st.write(get_current_time())

@st.cache_resource
def load_large_dataset():
    return pd.DataFrame(
    np.random.randn(1000000, 5),
    columns=['A', 'B', 'C', 'D', 'E']
)
    
    
st.subheader("⼤規模データセットの処理")
start_time = time.time()
large_data = load_large_dataset()
end_time = time.time()
st.write(f"⼤規模データセット読み込み時間: {end_time - start_time:.2f} 秒")
st.write(f"データセットの形状: {large_data.shape}")
st.write(large_data.head())

def generate_large_dataset():
    # ⼤きなデータセットを⽣成（約10秒かかる）
    data = pd.DataFrame(np.random.randn(1000000, 5), columns=["A", "B", "C", "D", "E"])
    return data


@st.cache_data
def load_data_cached():
    return generate_large_dataset()


def load_data_uncached():
    return generate_large_dataset()


st.subheader("キャッシュなしの場合")
start_time = time.time()
data_uncached = load_data_uncached()
end_time = time.time()
st.write(f"データ読み込み時間: {end_time - start_time:.2f} 秒")
st.write(data_uncached.head())
st.subheader("キャッシュありの場合")
start_time = time.time()
data_cached = load_data_cached()
end_time = time.time()
st.write(f"データ読み込み時間: {end_time - start_time:.2f} 秒")
st.write(data_cached.head())
st.write("キャッシュありの場合、2回⽬以降の読み込みは⾮常に⾼速になります。"),


st.header("レッスン7: 円グラフ(plotly,go)の作成")
# サンプルデータの作成
data = {"商品": ["A", "B", "C", "D", "E"], "売上": [300, 200, 180, 150, 120]}
df = pd.DataFrame(data)
st.write("サンプルデータ:")
st.dataframe(df)

# 基本的な円グラフの作成
fig = go.Figure(data=[go.Pie(labels=df["商品"], values=df["売上"])])
fig.update_layout(title="商品別売上⽐率")
st.plotly_chart(fig)

# カスタマイズされた円グラフの作成
colors = ["gold", "mediumturquoise", "darkorange", "lightgreen", "lightcoral"]
fig = go.Figure(
    data=[
        go.Pie(
            labels=df["商品"],
            values=df["売上"],
            hole=0.3,
            marker=dict(colors=colors, line=dict(color="#000000", width=2)),
        )
    ]
)
fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hoverinfo="label+value+percent",
    textfont_size=14,
)
fig.update_layout(
    title="商品別売上⽐率（詳細版）",
    font=dict(family="Meiryo", size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    annotations=[dict(text="総売上", x=0.5, y=0.5, font_size=20, showarrow=False)],
)
st.plotly_chart(fig)


st.title("私のStreamlitアプリです♡")
st.header("レッスン3: テキスト要素の追加")
# 通常のテキスト
st.text("これは通常のテキストです。")
# Markdown形式のテキスト
st.markdown("これは **太字** で、*イタリック* です。")
# LaTeX形式の数式
st.latex(r"\sqrt{x^2 + y^2} = z")
# 情報メッセージ（⻘⾊）
st.info("データの読み込みが完了しました。")
# 警告メッセージ（⻩⾊）
st.warning("ファイルのサイズが⼤きいため、処理に時間がかかる可能性があります。")
# エラーメッセージ（⾚⾊）
st.error("ファイルの形式が正しくありません。CSVファイルをアップロードしてください。")
# 成功メッセージ（緑⾊）
st.success("グラフの作成が完了しました。")

code = """def hello():
print("Hello, Streamlit!")"""
st.code(code, language="python")

st.header("レッスン4:データ入力と表示")
name = st.text_input("名前を入力")
if name:
    st.write(f"こんにちは{name}さん")

age = st.number_input(
    "あなたの年齢を⼊⼒してください", min_value=0, max_value=120, value=20
)
st.write(f"あなたは{age}歳です。")

date = st.date_input("⽇付を選択してください")
st.write(f"選択された⽇付: {date}")

data = {
    "名前": ["太郎", "花⼦", "⼀郎"],
    "年齢": [25, 30, 35],
    "都市": ["東京", "⼤阪", "福岡"],
}
df = pd.DataFrame(data)
# データフレームの表⽰
st.subheader("データフレームの表⽰")
st.dataframe(df)

st.header("レッスン5: 折れ線グラフ(plotly,go)の作成")
# サンプルデータの作成
data = {
    "⽉": ["1⽉", "2⽉", "3⽉", "4⽉", "5⽉", "6⽉"],
    "売上": [100, 120, 140, 180, 200, 210],
    "利益": [20, 25, 30, 40, 50, 55],
}
df = pd.DataFrame(data)
st.write("サンプルデータ:")
st.dataframe(df)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["⽉"], y=df["売上"], mode="lines+markers", name="売上"))
fig.add_trace(go.Scatter(x=df["⽉"], y=df["利益"], mode="lines+markers", name="利益"))
fig.update_layout(title="⽉別売上と利益", xaxis_title="⽉", yaxis_title="⾦額（万円）")
st.plotly_chart(fig)

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df["⽉"],
        y=df["売上"],
        mode="lines+markers",
        name="売上",
        line=dict(color="blue", width=2),
    )
)
fig.add_trace(
    go.Scatter(
        x=df["⽉"],
        y=df["利益"],
        mode="lines+markers",
        name="利益",
        line=dict(color="red", width=2),
    )
)
fig.update_layout(
    title="⽉別売上と利益の推移",
    xaxis_title="⽉",
    yaxis_title="⾦額（万円）",
    font=dict(family="Meiryo", size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    hovermode="x unified",
)
fig.update_xaxes(tickangle=-45)
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor="white")
st.plotly_chart(fig)

st.header("レッスン6: 棒グラフ(plotly,go)の作成")
# サンプルデータの作成
data = {
    "製品": ["A", "B", "C", "D", "E"],
    "売上": [300, 400, 200, 600, 500],
    "利益": [30, 60, 20, 100, 80],
}
df = pd.DataFrame(data)
st.write("サンプルデータ:")
st.dataframe(df)

# 基本的な棒グラフの作成
fig = go.Figure()
fig.add_trace(go.Bar(x=df["製品"], y=df["売上"], name="売上"))
fig.add_trace(go.Bar(x=df["製品"], y=df["利益"], name="利益"))
fig.update_layout(
    title="製品別の売上と利益",
    xaxis_title="製品",
    yaxis_title="⾦額（万円）",
    barmode="group",
)
st.plotly_chart(fig)

# カスタマイズされた棒グラフの作成
fig = go.Figure()
fig.add_trace(go.Bar(x=df["製品"], y=df["売上"], name="売上", marker_color="blue"))
fig.add_trace(go.Bar(x=df["製品"], y=df["利益"], name="利益", marker_color="red"))
fig.update_layout(
    title="製品別の売上と利益⽐較",
    xaxis_title="製品",
    yaxis_title="⾦額（万円）",
    barmode="group",
    font=dict(family="Meiryo", size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    hovermode="x unified",
)
fig.update_traces(texttemplate="%{y}", textposition="outside")
fig.update_yaxes(range=[0, max(df["売上"].max(), df["利益"].max()) * 1.1])
st.plotly_chart(fig)
