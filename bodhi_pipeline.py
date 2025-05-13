#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:52:03 2024

@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/25-IOM-GLO-1 - Clean_dataset.xlsx')
indicators = []

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    country = bd.Indicator(df, "Country", 0, ['1'], i_cal=None, i_type='count', description='Which country is the survey conducted in?', period='endline', target = None)
    country.add_breakdown({'Age Group':'Age Group'})
    country.add_var_order(['Ethiopia', 'Philippines'])
    indicators.append(country)
    
    age = bd.Indicator(df, "Age group", 0, ['Age Group'], i_cal=None, i_type='count', description='Age distribution', period='endline', target = None)
    age.add_breakdown({'1':'Country'})
    indicators.append(age)
    
    region = bd.Indicator(df, "Region", 0, ['2'], i_cal=None, i_type='count', description='Participants Region', period='endline', target = None, visual = False)
    region.add_breakdown({'1':'Country', "Age Group":"Age Group"})
    region.add_var_order(["Pio Duran, Albay",
                          "Minalabac, Camarines Sur",
                          "Jimma Zone1",
                          "East Hararghe Zone 2"])
    indicators.append(region)
    
    gender = bd.Indicator(df, "Gender", 0, ['4'], i_cal=None, i_type='count', description='Gender distribution', period='endline', target = None)
    gender.add_breakdown({'1':'Country', "Age Group":"Age Group", "2":"Region"})
    gender.add_var_order(['Female', 'Male'])
    indicators.append(gender)
    
    disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability status', period='endline', target = None, visual = False)
    disability.add_breakdown({'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(disability)
    
    impact1 = bd.Indicator(df, "impact1", 0, ['impact1'], i_cal=None, i_type='count', description='impact1', period='endline', target = None)
    impact1.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    impact1.add_var_order(["Adequate","Inadequate"])
    indicators.append(impact1)
    
    impact2 = bd.Indicator(df, "impact2", 0, ['impact2'], i_cal=None, i_type='count', description='impact2', period='endline', target = None)
    impact2.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    impact2.add_var_order(["Adequate","Inadequate"])
    indicators.append(impact2)
  
    q21 = bd.Indicator(df, "Q21", 0, ['21'], i_cal=None, i_type='count', description='Since you participated in the CREATE Project, have you taken up any new livelihood activities?', period='endline', target = None)
    q21.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q21.add_var_order(["Yes",
                       "No",
                       "Unsure"])
    indicators.append(q21)
    
    q22 = bd.Indicator(df, "Q22_1", 0, ['22-a-1', '22-a-2', '22-a-3', '22-a-4', '22-a-5', '22-a-6', '22-a-7', '22-a-8','22-a-9'], i_cal=None, i_type='count', description='Livelihood activities you were engaged in before CREATE', period='endline', target = None)
    q22.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q22.add_var_change({1: "Yes", 0: "No"})
    q22.add_var_order([1, 0])
    q22.add_label(["Crop farming","Pastoralist/livestock keeper","Bee keeping",
                   "Fishing","Self-employed – non-agricultural value chain","Self-employed – agricultural value chain",
                   "Housewife/househusband","Unemployed","Other"])
    indicators.append(q22)
    
    q22_2 = bd.Indicator(df, "Q22_2", 0, ['22-b-1','22-b-2','22-b-3', '22-b-4', '22-b-5', '22-b-6', '22-b-7', '22-b-8', '22-b-9', '22-b-10'], i_cal=None, i_type='count', description='Livelihood activities you started through CREATE support', period='endline', target = None)
    q22_2.add_breakdown({'1':'Country', "Age Group":"Age Group","4":"Gender"})
    q22_2.add_var_change({1: "Yes", 0: "No"})
    q22_2.add_var_order([1, 0])
    q22_2.add_label(["Eco-tourism","Climate-smart agriculture","Livestock diversification",
                   "Beekeeping","Fishing/aquaculture","Small business/self-employment (non-agriculture)",
                   "Agricultural value chain","Vocational skills training","Other",
                   "None"])
    indicators.append(q22_2)
    
    q23 = bd.Indicator(df, "Q23", 0, ['23'], i_cal=None, i_type='count', description='To what extent did the CREATE project influence your decision to pursue the livelihood activities mentioned above? ', period='endline', target = None)
    q23.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    q23.add_var_order(["Not at all",
                       "Low",
                       "Moderate",
                       "High",
                       "Very high"])
    indicators.append(q23)
    
    q27 = bd.Indicator(df, "Q27", 0, ['27-1', '27-2', '27-3', '27-4', '27-5', '27-6', '27-7'], i_cal=None, i_type='count', description='Compared to before the project how would you describe any change in  food security?', period='endline', target = None)
    q27.add_breakdown({'1':'Country', "Age Group":"Age Group","4":"Gender"})
    q27.add_var_change({1: "Yes", 0: "No"})
    q27.add_var_order([1, 0])
    q27.add_label(["I am able to eat more meals in a day than before",
                   "I am able to eat more food per serving than before",
                   "I am able to eat expensive food  types more regularly than before",
                   "I can afford to eat more food types in a single meal than before",
                   "I have more flexibility to decide what I want to eat without worrying about the cost of food",
                   "I am to feed more people than I could in the past",
                   "Other"])
    indicators.append(q27)

 
    q28 = bd.Indicator(df, "Q28", 0, ['28-1', '28-2', '28-3', '28-4', '28-5', '28-6', '28-7', '28-8', '28-9'], i_cal=None, i_type='count', description='What skills or training have you received through the CREATE project?', period='endline', target = None, visual = False)
    q28.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q28.add_var_change({1: "Yes", 0: "No"})
    q28.add_var_order([1, 0])
    q28.add_label(["Agricultural",
                       "Livestock (e.g. Bee Keeping)",
                       "Business/ Entrepreneurial",
                       "Vocational",
                       "Security/Safety",
                       "Food Processing",
                       "Tourism Skills",
                       "Accounting",
                       "Other (Please specify…..)"])
    indicators.append(q28)
  
    q29 = bd.Indicator(df, "Q29", 0, ['29'], i_cal=None, i_type='count', description='', period='endline', target = None, visual = False)
    q29.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    q29.add_var_order(["Yes, significantly reduced migration",
                       "Yes, somewhat reduced migration",
                       "No, migration levels have stayed the same",
                       "No, migration has increased",
                       "Unsure"])
    indicators.append(q29)
    
    q31 = bd.Indicator(df, "Q31", 0, ['31'], i_cal=None, i_type='count', description='If your household lost its main source of income today, how long could you sustain your basic needs?', period='endline', target = None)
    q31.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    q31.add_var_order(["1 week or less",
                       "2 - 3 weeks",
                       "Less than a month",
                       "1-3 months",
                       "More than 3 months",
                       "Unsure"])
    indicators.append(q31)
    
    q32 = bd.Indicator(df, "Q32", 0, ['32'], i_cal=None, i_type='count', description='Before joining the CREATE project, how long would it have taken you to sustain your basic needs if you lost your main source of income?', period='endline', target = None)
    q32.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q32.add_var_order(["1 week or less",
                       "2 - 3 weeks",
                       "Less than a month",
                       "1-3 months",
                       "More than 3 months",
                       "Unsure"])
    indicators.append(q32)
    
    q34 = bd.Indicator(df, "Q34", 0, ['34'], i_cal=None, i_type='count', description='Since the CREATE project how able is your primary livelihood to cope with the effects of climate change?', period='endline', target = None)
    q34.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q34.add_var_order(["Not at all prepared",
                       "A little prepared",
                       "Moderately prepared",
                       "Highly prepared",
                       "Very highly prepared"])
    indicators.append(q34)
    
    q36 = bd.Indicator(df, "Q36", 0, ['36'], i_cal=None, i_type='count', description='Before the CREATE project, how much did you know about the risks of unsafe migration and human trafficking?', period='endline', target = None)
    q36.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    q36.add_var_order(["Nothing at all",
                       "A little",
                       "A moderate amount",
                       "A lot"])
    indicators.append(q36)
    
    q37 = bd.Indicator(df, "Q37", 0, ['37'], i_cal=None, i_type='count', description='How much do you know about these risks now?', period='endline', target = None)
    q37.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q37.add_var_order(["Nothing at all",
                       "A little",
                       "A moderate amount",
                       "A lot"])
    indicators.append(q37)

    q38 = bd.Indicator(df, "Q38", 0, ['38-1', '38-2', '38-3', '38-4', '38-5', '38-6', '38-7'], i_cal=None, i_type='count', description='Please mention the risks of unsafe migration and human trafficking that you can recall', period='endline', target = None)
    q38.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q38.add_var_change({1: "Yes", 0: "No"})
    q38.add_var_order([1, 0])
    q38.add_label(["Loss of property",
                   "Physical injury",
                   "Detention and deportation",
                   "Forced labour",
                   "Violence",
                   "Abuse and exploitation",
                   "Other"])
    indicators.append(q38)
    
    q40 = bd.Indicator(df, "Q40", 0, ['40'], i_cal=None, i_type='count', description='Before the CREATE project, how much did you know about climate change and how it affects livelihoods?', period='endline', target = None)
    q40.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q40.add_var_order(["Nothing at all",
                       "A little",
                       "A moderate amount",
                       "A lot"])
    indicators.append(q40)
    
    q41 = bd.Indicator(df, "Q41", 0, ['41'], i_cal=None, i_type='count', description='How much do you know about these risks now?', period='endline', target = None)
    q41.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    q41.add_var_order(["Nothing at all",
                       "A little",
                       "A moderate amount",
                       "A lot"])
    indicators.append(q41)
    
    q44 = bd.Indicator(df, "Q44", 0, ['44'], i_cal=None, i_type='count', description='Did you receive information on how to protect yourself from/against human trafficking?', period='endline', target = None, visual = False)
    q44.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q44.add_var_order(["Yes (Please specify_____)",
                       "No"])
    indicators.append(q44)
    
    q46 = bd.Indicator(df, "Q46", 0, ['46'], i_cal=None, i_type='count', description='How would you rate your ability to recover from climate disasters now?', period='endline', target = None)
    q46.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    q46.add_var_order(["Completely unable",
                       "Not very well",
                       "Somewhat well",
                       "Very well",
                       "Completely able"])
    indicators.append(q46)
    
    q48 = bd.Indicator(df, "Q48", 0, ['48'], i_cal=None, i_type='count', description='How would you rate your ability to prepare for climate related challenges now?', period='endline', target = None)
    q48.add_breakdown({'1':'Country', "Age Group":"Age Group",  "4":"Gender"})
    q48.add_var_order(["Completely unable",
                       "Not very well",
                       "Somewhat well",
                       "Very well",
                       "Completely able"])
    indicators.append(q48)
    
    q49 = bd.Indicator(df, "Q49", 0, ['49'], i_cal=None, i_type='count', description='Do you feel more informed about safe migration pathways than before?', period='endline', target = None)
    q49.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q49.add_var_order(["Yes",
                       "No"])
    indicators.append(q49)
    
    q50 = bd.Indicator(df, "Q50", 0, ['50'], i_cal=None, i_type='count', description='In the past three years, have you encountered a job offer that seemed suspicious or fraudulent?', period='endline', target = None)
    q50.add_breakdown({'1':'Country', "Age Group":"Age Group", "4":"Gender"})
    q50.add_var_order(["Yes",
                       "No"])
    indicators.append(q50)
    
    q51 = bd.Indicator(df, "Q51", 0, ['51-1', '51-2', '51-3', '51-4', '51-5', '51-6'], i_cal=None, i_type='count', description='If yes, how did you determine that the job offer was suspicious?', period='endline', target = None)
    q51.add_breakdown({ "Age Group":"Age Group", "4":"Gender"})
    q51.add_var_change({1: "Yes", 0: "No"})
    q51.add_var_order([1, 0])
    q51.add_label(["The offer seemed too good to be true",
                   "There was no clear contract or legal documentation",
                   "The recruiter asked for upfront payment or personal documents",
                   "I was warned by family, friends, or community members",
                   "I recognized the risks based on information received from the CREATE project",
                   "Other"])
    indicators.append(q51)
    
    q52 = bd.Indicator(df, "Q52", 0, ['52'], i_cal=None, i_type='count', description='Do you know where to report suspected cases of human trafficking or exploitation?', period='endline', target = None)
    q52.add_breakdown({ '1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q52.add_var_order(["Yes",
                       "No"])
    indicators.append(q52)
    
    q55 = bd.Indicator(df, "Q55", 0, ['55'], i_cal=None, i_type='count', description='Since the CREATE project activities how likely are you to have to migrate because of limited livelihoods?', period='endline', target = None)
    q55.add_breakdown({'1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q55.add_var_order(["Very likely",
                       "Somewhat likely",
                       "Neutral",
                       "Somewhat unlikely",
                       "Very unlikely"])
    indicators.append(q55)
    
    q58 = bd.Indicator(df, "Q58", 0, ['58'], i_cal=None, i_type='count', description='Do you expect the project’s benefits to last?', period='endline', target = None)
    q58.add_breakdown({ '1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q58.add_var_order(["Not at all",
                       "To a small extent",
                       "To a moderate extent",
                       "To a great extent",
                       "Completely"])
    indicators.append(q58)
    
    q59 = bd.Indicator(df, "Q59", 0, ['59'], i_cal=None, i_type='count', description='Were you aware of any other interventions active in your community during the CREATE project lifecycle?', period='endline', target = None, visual = False)
    q59.add_breakdown({ '1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q59.add_var_order(["Yes (Please specify……..)",
                       "No"])
    indicators.append(q59)

    q60 = bd.Indicator(df, "Q60", 0, ['60-1', '60-2', '60-3', '60-4', '60-5', '60-6'], i_cal=None, i_type='count', description='What factors do you think will affect whether the benefits of the CREATE project last?', period='endline', target = None)
    q60.add_breakdown({'1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q60.add_var_change({1: "Yes", 0: "No"})
    q60.add_var_order([1, 0])
    q60.add_label(["Continued support from local government",
                   "Community engagement and willingness to continue activities",
                   "Availability of financial resources",
                   "Access to markets and business opportunities",
                   "Climate-related risks and disasters",
                   "Other"])
    indicators.append(q60)
    
    q61 = bd.Indicator(df, "Q61", 0, ['61'], i_cal=None, i_type='count', description='Have you or your household made any long-term changes based on what you learned from the CREATE project?', period='endline', target = None, visual = False)
    q61.add_breakdown({ '1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q61.add_var_order(["Yes (Please specify……..)",
                       "No (Please specify why……)"])
    indicators.append(q61)
    
    q62 = bd.Indicator(df, "Q62", 0, ['62'], i_cal=None, i_type='count', description='Are you still using the skills or knowledge you gained from the CREATE project?', period='endline', target = None)
    q62.add_breakdown({ '1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q62.add_var_order(["Yes, regularly",
                       "Yes, occasionally",
                       "No, not anymore"])
    indicators.append(q62)
    
    q63 = bd.Indicator(df, "Q63", 0, ['63-1', '63-2', '63-3','63-4', '63-5', '63-6'], i_cal=None, i_type='count', description='Are there any challenges preventing you from continuing the activities or benefits from the CREATE project?', period='endline', target = None)
    q63.add_breakdown({'1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q63.add_var_change({1: "Yes", 0: "No"})
    q63.add_var_order([1, 0])
    q63.add_label(["Lack of financial resources",
                   "Lack of market access for products/services",
                   "Environmental/climate-related factors",
                   "Lack of community support",
                   "Government or policy-related challenges",
                   "Other"])
    indicators.append(q63)
    
    q67 = bd.Indicator(df, "Q67", 0, ['67'], i_cal=None, i_type='count', description='Were community members involved in designing or adapting project activities?', period='endline', target = None)
    q67.add_breakdown({ '1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q67.add_var_order(["Yes, extensively",
                       "Yes, but only in minor ways",
                       "No, decisions were made without community input",
                       "Not sure"])
    indicators.append(q67)
    
    q68 = bd.Indicator(df, "Q68", 0, ['68'], i_cal=None, i_type='count', description='Do you think the CREATE project addressed the most pressing needs of your community?', period='endline', target = None)
    q68.add_breakdown({'1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q68.add_var_order(["Yes, very well",
                       "Somewhat, but gaps remain",
                       "No, it did not address key issues"])
    indicators.append(q68)
    
    q70 = bd.Indicator(df, "Q70", 0, ['70'], i_cal=None, i_type='count', description='Do you think women and men had equal opportunities to engage in CREATE activities?', period='endline', target = None)
    q70.add_breakdown({ '1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q70.add_var_order(["Yes, completely",
                       "Mostly",
                       "Somewhat",
                       "Not really",
                       "Not at all"])
    indicators.append(q70)
    
    q71 = bd.Indicator(df, "Q71", 0, ['71'], i_cal=None, i_type='count', description='Were the types of activities appropriate for women/youth?', period='endline', target = None)
    q71.add_breakdown({ '1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q71.add_var_order(["Yes, completely",
                       "Mostly",
                       "Somewhat",
                       "Not really",
                       "Not at all"])
    indicators.append(q71)
    
    q72 = bd.Indicator(df, "Q72", 0, ['72'], i_cal=None, i_type='count', description='Did you feel safe/able to take part in all activities?', period='endline', target = None)
    q72.add_breakdown({'1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q72.add_var_order(["Yes, completely",
                       "Mostly",
                       "Somewhat",
                       "Not really",
                       "Not at all"])
    indicators.append(q72)
    
    q74 = bd.Indicator(df, "Q74", 0, ['74'], i_cal=None, i_type='count', description='Do you feel that people with disabilities in your community have equal access to migration safety information?', period='endline', target = None)
    q74.add_breakdown({'1':'Country',"Age Group":"Age Group", "4":"Gender"})
    q74.add_var_order(["Yes, fully",
                       "Somewhat, but with challenges",
                       "No, they face major barriers"])
    indicators.append(q74)
    
    return indicators
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    
    df_p = df[df['1'] == 'Philippines'].copy()
    df_e = df[df['1'] == 'Ethiopia'].copy()
    q20_e = bd.Indicator(df_e, "Q20_Ethiopia", 0, ['20'], i_cal=None, i_type='count', description='What was your average household monthly income from this livelihood activity?', s_test = 'stats', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q20_e)
    
    q25_e = bd.Indicator(df_e, "Q25_Ethiopia", 0, ['25'], i_cal=None, i_type='count', description='On an average month, how much additional income have you generated from these additional income sources you created since you took part in the project?', s_test = 'stats', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q25_e)
    
    q26_e = bd.Indicator(df_e, "Q26_Ethiopia", 0, ['26'], i_cal=None, i_type='count', description='If no additional income has been generated yet due to seasonality or some other factor, how much additional income do you EXPECT to generate?', s_test = 'stats', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q26_e)
    
    q20_p = bd.Indicator(df_p, "Q20_Philippines", 0, ['20'], i_cal=None, i_type='count', description='What was your average household monthly income from this livelihood activity?', s_test = 'stats', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q20_p)
    
    q25_p = bd.Indicator(df_p, "Q25_Philippines", 0, ['25'], i_cal=None, i_type='count', description='On an average month, how much additional income have you generated from these additional income sources you created since you took part in the project?', s_test = 'stats', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q25_p)
    
    q26_p = bd.Indicator(df_p, "Q26_Philippines", 0, ['26'], i_cal=None, i_type='count', description='If no additional income has been generated yet due to seasonality or some other factor, how much additional income do you EXPECT to generate?', s_test = 'stats', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q26_p)
    
    impact1_t = bd.Indicator(df, "impact1", 0, ['impact1'], i_cal=None, i_type='count', description='impact1', s_test = 'chi', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(impact1_t)
    
    impact2_t = bd.Indicator(df, "impact2", 0, ['impact2'], i_cal=None, i_type='count', description='impact2', s_test = 'chi', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(impact2_t)
    
    q23_t = bd.Indicator(df, "Q23", 0, ['23'], i_cal=None, i_type='count', description='To what extent did the CREATE project influence your decision to pursue the livelihood activities mentioned above? ', s_test = 'chi', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q23_t)
    
    q31_t = bd.Indicator(df, "Q31", 0, ['31'], i_cal=None, i_type='count', description='If your household lost its main source of income today, how long could you sustain your basic needs?', s_test = 'chi', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q31_t)
    
    q34_t = bd.Indicator(df, "Q34", 0, ['34'], i_cal=None, i_type='count', description='Since the CREATE project how able is your primary livelihood to cope with the effects of climate change?', s_test = 'chi', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q34_t)
    
    q46_t = bd.Indicator(df, "Q46", 0, ['46'], i_cal=None, i_type='count', description='How would you rate your ability to recover from climate disasters now?', s_test = 'chi', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q46_t)
    
    q48_t = bd.Indicator(df, "Q48", 0, ['48'], i_cal=None, i_type='count', description='How would you rate your ability to prepare for climate related challenges now?', s_test = 'chi', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q48_t)
    
    q55_t = bd.Indicator(df, "Q55", 0, ['55'], i_cal=None, i_type='count', description='Since the CREATE project activities how likely are you to have to migrate because of limited livelihoods?', s_test = 'chi', s_group = {'1':'Country', "Age Group":"Age Group", "2":"Region", "4":"Gender"})
    indicators.append(q55_t)
    return indicators

# Create the PMF class ('Project Title', 'Evaluation')
mango = pmf.PerformanceManagementFramework('mango', 'Evaluation')

indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
mango.add_indicators(indicators)

file_path1 = 'data/25-IOM-GLO-1 - Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/25-IOM-GLO-1 - Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/' # File path for saving visuals
mango.PMF_generation(file_path1, file_path2, folder) # Run the PMF

