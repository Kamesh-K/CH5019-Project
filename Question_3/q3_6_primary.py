# Question 6 - Calssification into Primary, Secondry and Tertiary cases

# Primary Cases
primary_details = IndividualDetails.copy()
primary_details = primary_details[primary_details['diagnosed_date'] <= '10/04/2020'][['id', 'notes', 'detected_state']]
primary_details = primary_details.dropna()

travelled_flag = (primary_details['notes'].str.contains("Travelled from")) & 
travelled_in_flag = (primary_details['notes'].str.contains("Tralled (from|to) (Delhi)|(Bangalore)|(Rajasthan)|(Kolkata)|(Mumbai)", regex=True))
travelled_id = primary_details[travelled_flag]['id']
travelled_in_flag = primary_details[travelled_in_flag]['id']

primary_details = primary_details[travelled_flag & ~travelled_in_flag][['id', 'detected_state']].groupby('detected_state').count().reset_index()
primary_details = primary_details.rename(columns={'id':'Primary count', 'detected_state':'State name'})
primary_details_plot = primary_details.plot.bar(x='State name', y='Primary count', title='Primary count distribution across states')

primary_details = primary_details.sort_values(by='State name')
