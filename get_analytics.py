#%%
import matplotlib.pyplot as plt
import pandas as pd
#from scraper.py import DojNewsScraper
#%%

df = pd.read_json('combined_csa.json')
def get_all_data(df=df):

    df['year'] = df['date'].str.slice(-4)
   #PLOT YEARLY REPORTS FOR CSA
    year_report_counts = df['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.set_title('reports from DOJ with tags "child" "sexual" "abuse"')
    ax.set_xlabel('year')
    ax.set_ylabel('report count')
    ax.plot(year_report_counts)
    fig.savefig('yearly_trends')
    plt.show()
    def get_stats(word):
        df_new = df.loc[df['contents'].str.contains(word, na=False)]
        return {
            'num_articles': df_new.shape[0],
            'year_splits': df_new['year'].value_counts().sort_index().to_json()
        }
    df_word_dict = {
        'threat': get_stats('threat'),
        'suicide': get_stats('suicide'),
        'TikTok': get_stats('TikTok'),
        'Facebook': get_stats('Facebook'),
        'CashApp' : get_stats('CashApp'),
        'Telegram': get_stats('Telegram'),
        'Discord': get_stats('Discord'),
        'video': get_stats('video'),
        'online': get_stats('online'),
        'valorant': get_stats('Valorant'),
        'gaming': get_stats('gaming'),
        'game': get_stats('game'),
        'coerce': get_stats('coerce'),
        'sextortion': get_stats('sextortion'),
        'picture': get_stats('picture'),
        'kill': get_stats('kill'),
        'video gam': get_stats('video gam')

    }
    
    import json
    with open("sample.json", "w") as outfile: 
        json.dump(df_word_dict, outfile)
    
    words_df = pd.read_json('sample.json', orient='index')
    fig2, ax2 = plt.subplots()
    
    ax2.barh(words_df.index,words_df['num_articles'])
    fig.savefig('bar')
    plt.show()
get_all_data(df=df)
# %%
if __name__ == '__main__':
    get_all_data(df=df)