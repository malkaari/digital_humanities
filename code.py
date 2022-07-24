import pandas as pd
 

df = pd.read_csv('data.csv', sep=',')

#fix the date column
df['date'] = pd.to_datetime(df['date'])

#mapping abbreviation to state
df2 = pd.read_csv('usa_states_to_postal.csv', sep=',')
abbreviation_to_state= dict(zip(df2.Code, df2.State ))

#converting abbreviation to state name
df['state']= df['state'].apply(lambda x : abbreviation_to_state[x])


# for the heat map
incidents_per_state = df['state'].value_counts().to_csv('incidents_per_state.csv') 

df['month_year'] = df['date'].dt.to_period('M')

# for the time line
incidents_per_month = df['month_year'].value_counts().to_csv('incidents_per_month.csv')

number_of_incidents_per_type =  df['type'].value_counts().to_csv('number_of_incidents_per_type.csv')

number_of_cities_per_state = df.groupby(['state'])['city'].unique().apply(lambda x: len(x)).to_csv('number_of_cities_per_state.csv')



df3 = pd.read_csv('jew_population.csv', sep=',')

data={'jewishPopulationPerc':[],'Number':[]}
for k,v in df['state'].value_counts().to_dict().items():
    percent = df3.loc[df3['State'] == k].jewishPopulationPerc.values
    data['jewishPopulationPerc'].extend(percent)
    if(len(percent) == 0):
        continue
    data['Number'].append(v)

#number of incidents as a function of jewish population percent
df4=pd.DataFrame(data)

incidents_per_percent = df4.to_csv('incidents_per_percent.csv',index=False)






