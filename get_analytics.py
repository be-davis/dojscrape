#%%
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_json('combined_csa.json')
df['year'] = df['date'].str.slice(-4)
year_report_counts = df['year'].value_counts().sort_index()
plt.title('reports from DOJ with tags "child" "sexual" "abuse"')
plt.xlabel('year')
plt.ylabel('report count')
plt.plot(year_report_counts)
#%%
def get_num_articles(word):
    df_new = df.loc[df['contents'].str.contains(word, na=False)]
    return {
        'num_articles': df_new.shape[0],
        'year_splits': df_new['year'].value_counts().sort_index().to_json()
    }
df_word_dict = {
    'threat': get_num_articles('threat'),
    'suicide': get_num_articles('suicide'),
    'TikTok': get_num_articles('TikTok'),
    'Facebook': get_num_articles('Facebook'),
    'CashApp' : get_num_articles('CashApp'),
    'Telegram': get_num_articles('Telegram'),
    'Discord': get_num_articles('Discord'),
    'video': get_num_articles('video')
}
#%%
import json
with open("sample.json", "w") as outfile: 
    json.dump(df_word_dict, outfile)
#%%