# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

electors_2009 = pd.read_csv(path)
candidate_2009 = pd.read_csv(path1)
candidate_2009.head(2)

# Plot a bar chart to compare the number of male and female candidates in the election
candidate_2009.Candidate_Sex.value_counts(normalize=True).plot(kind='bar')
# Plot a histogram of the age of all the candidates as well as of the winner amongst them. Compare them and note an observation
fig,ax=plt.subplots(1,2,figsize=(20,10))
ax[0].hist(candidate_2009.Candidate_Age)
ax[0].set_xlabel('age')
ax[0].set_ylabel('count')
ax[0].set_title('all candidate')
win=candidate_2009[candidate_2009.Position==1]
ax[1].hist(win.Candidate_Age)
ax[1].set_xlabel('age')
ax[1].set_ylabel('count')
ax[1].set_title('All Winners')
# Plot a bar graph to get the vote shares of different parties
votes=candidate_2009.groupby('Party_Abbreviation').Total_Votes_Polled.sum()
votes.plot(kind='bar',stacked=False)
# Plot a barplot to compare the mean poll percentage of all the states
#electors_2009.head(2)
state_poll_percentage=electors_2009.groupby('STATE')['POLL PERCENTAGE'].mean()
state_poll_percentage.plot(kind='bar',stacked=False)
# Plot a bar plot to compare the seats won by different parties in Uttar Pradesh
win_uttarpradesh_seat= win[win['State_name']=='Uttar Pradesh']
win_uttarpradesh_seat.Party_Abbreviation.value_counts().plot(kind='bar',stacked=False)
# Plot a stacked bar chart to compare the number of seats won by different `Alliances` in Gujarat,Madhya Pradesh and Maharashtra. 
al=win[(win['State_name']=='Gujarat') | (win['State_name']=='Madhya Pradesh') | (win['State_name']=='Maharashtra') ]
al.groupby(['State_name','Alliance']).count().unstack().plot(kind='bar',stacked=True)
# Plot a grouped bar chart to compare the number of winner candidates on the basis of their caste in the states of Andhra Pradesh, Kerala, Tamil Nadu and Karnataka
grpchart=win[(win['State_name']=='Kerala')  | (win['State_name']=='Andhra Pradesh') | (win['State_name']=='Tamil Nadu') | (win['State_name']=='Karnataka') ]
grpchart.groupby(['State_name','Candidate_Category']).size().unstack().plot(kind='barh')
# Plot a horizontal bar graph of the Parliamentary constituency with total voters less than 100000
tot_voters_lessthan=electors_2009[electors_2009['Total voters']<100000]
plt.barh(tot_voters_lessthan['PARLIAMENTARY CONSTITUENCY'],tot_voters_lessthan['Total voters'])

# Plot a pie chart with the top 10 parties with majority seats in the elections
top10=win['Party_Abbreviation'].value_counts()[:10]
plt.pie(top10.values,labels=top10.index)
# Plot a pie diagram for top 9 states with most number of seats
top9_states=win['State_name'].value_counts()[:9]
print(top9_states.head(2))
plt.pie(top9_states.values,labels=top9_states.index)




