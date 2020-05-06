# Question 6 - Calssification into Primary, Secondry and Tertiary cases

# Primary Cases
primary_details = IndividualDetails.copy()
primary_details = primary_details[primary_details['diagnosed_date'] <= '10/04/2020'][['id', 'notes', 'detected_state']]
primary_details = primary_details.dropna()

travelled_flag = (primary_details['notes'].str.contains("Travelled from"))
travelled_in_flag = (primary_details['notes'].str.contains("Travlled ((from|to) Delhi)|((from|to) Bangalore)|((from|to) Rajasthan)|((from|to) Kolkata)|((from|to) Mumbai)|((from|to) WB)", regex=True))
travelled_id = primary_details[travelled_flag]['id']
travelled_in_id = primary_details[travelled_in_flag]['id']

travelled_out = primary_details[travelled_flag & (!travelled_in_flag)][['id', 'detected_state', 'notes']]#.groupby('detected_state').count().reset_index()

primary_id = travelled_out['id']
primary_details = primary_details.rename(columns={'id':'Primary count', 'detected_state':'State name'})

#primary_details_plot = primary_details.plot.bar(x='State name', y='Primary count', title='Primary count distribution across states')

#primary_details = primary_details.sort_values(by='State name')

pd.set_option("display.max_rows", None, "display.max_columns", None)
travelled_out