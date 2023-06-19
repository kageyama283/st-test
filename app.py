import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader('ファイルをアップロード',type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)#CSV読み込み
    name = df['Ad name'].str[10::]#文字列の11文字目からを取得(A1T1など)
    df['name'] = name#CSVに[name]という項目を追加
    # st.write(df)

    options = df['name'].unique()#['name']項目の中から重複を削除して抽出
    # options = st.sidebar.multiselect('プログラム名',dupli)
    
    name_arr = []
    imp_arr = []
    click_arr = []
    cv_arr = []
    cost_arr = []

    ctr_arr = []
    cpc_arr = []
    cvr_arr = []
    cpa_arr = []

    # if options:
    for i,option in enumerate(options):
        selected = df.query(f'name == "{option}"')
        name_arr.append(option)
        imp = selected['Impressions'].sum()
        imp_arr.append(imp)
        click = selected['Clicks'].sum()
        click_arr.append(click)
        cv = selected['CV (conversions)'].sum()
        cv_arr.append(cv)
        cost = selected['Cost'].sum()
        cost_arr.append(cost)

        ctr = click / imp * 100
        ctr_arr.append(str(round(ctr,2)) + '%')
        cpc = cost / click
        cpc_arr.append(str('{:,.2f}'.format(cpc)) + '円')
        cvr = cv / click * 100
        cvr_arr.append(str(round(cvr,2)) + '%')
        cpa = cost / cv
        cpa_arr.append(str(round(cpa,0)) + '円')

        df1 = pd.DataFrame(
            data={
                '広告名':name_arr,
                'インプレッション':imp_arr,
                'クリック数':click_arr,
                'CV':cv_arr,
                'Cost':cost_arr,
                'CTR':ctr_arr,
                'CPC':cpc_arr,
                'CVR':cvr_arr,
                'CPA':cpa_arr,
            }
        )
    st.write(df1)

    # st.write(df[['Adname','Impressions','Clicks','CTR (click-through rate)','CPC (cost per click)','CV (conversions)','CVR (conversion rate)','CPA (cost per action)','Cost']])