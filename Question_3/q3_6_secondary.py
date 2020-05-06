# Secondry Cases
secondary_details = IndividualDetails.copy()
secondary_details = secondary_details[secondary_details['diagnosed_date'] <= '10/04/2020'][['id', 'notes', 'detected_state']]
secondary_details = secondary_details.dropna()


contact_flag = (secondary_details['notes'].str.contains("Contact", case=False))
patient_id_flag = (secondary_details['notes'].str.contains("(P\d+?)", regex=True))
hospitals_flag = (secondary_details['notes'].str.contains("(Doctor)|(Hospital)", regex=True, case=False))
nri_flag = (secondary_details['notes'].str.contains("NRI"))


secondary_contacts = secondary_details[(contact_flag | patient_id_flag | hospitals_flag | nri_flag) & (secondary_details['id']!=primary_id)][['id', 'detected_state', 'notes']]#.groupby('detected_state').count().reset_index()
secondary_id = secondary_contacts['id']

secondary_details = secondary_details.rename(columns={'id':'Secondary count', 'detected_state':'State name'})
secondary_details_plot = secondary_details.plot.bar(x='State name', y='Secondary count', title='Secondary count distribution across states')

secondary_details = secondary_details.sort_values(by='State name')
