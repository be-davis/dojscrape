#%%
import pandas as pd
import numpy as np
app_danger = pd.read_csv('app_danger_updated.csv')

def get_app_rankings(source, app_name):
    source_df = app_danger.loc[app_danger['Source'] == source].reset_index()
    source_df['percentile'] = source_df['Num_Negative_Reviews'].rank(pct=True)

    final_df = source_df.loc[source_df['Title']==app_name]
    if final_df.shape[0] > 1:
        raise Exception("There are multiple apps with that name")
    app_stats = {
        'ranking':final_df.loc[final_df['Title']==app_name].iloc[0,0] + 1,
        'percentile': np.round(final_df.iloc[0,4]*100, decimals=2),
        'num_negative_reviews': final_df.iloc[0,3]
    }
    print(app_stats)  
    return app_stats
# %%
"""
From app danger df
-get percentile score off app in question --DONE
-plot the number or negative reviews for all apps
-query number of negative reviews for app in question
-rank on apple and google maerketplaces
-tell person if the source store is more dangerous than the other (apple vs google)

Press releases page
https://www.justice.gov/usao-edva/pr?search_api_fulltext=child+sexual+abuse&start_date=&end_date=&sort_by=field_date
"""

