#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "compilation of data set for AQUAS project"
("composing ratio refers to 13 topics and several data sources. "
 "see /home/ruth/ProgrammingProjects/AQUS/AQUAS/protocoll.md for ratio numbers."
"CompMedTherapies = "
 "WebMD = WebMD = 316 items"
 "HHP  = HarvardMedicalSchool = 92 items "
 "MH = MensHealth = 80 items "
 "WH = WomensHealth: 81 "
 "MP = MedlinePlus: 95"
"JEBIM = sage journal of evidence based integrative medicine = "
 "NN = Naturals news"
 "HIN = Health impact news"
 "MCL = Mercolas Censored Library "
 )
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2024 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "FSoLS 2024-v1 "


import pandas as pd





def load_datasets(base_url, col_list):
    # scientific
    #pmc_df = pd.read_csv(base_url+'/cleaned/scientific_pmc_texts_cleaned.csv', usecols=col_list)
    pmc_df_2 = pd.read_csv(base_url + '/before_cleaning/scientific_pmc_text_2024-06-13.csv', usecols=col_list)
    #scientific_df = pmc_df.drop_duplicates()
    scientific_df = pmc_df_2




## popular science
    webmd_df = pd.read_csv(base_url+'/cleaned/popular_WebMed_text_cleaned.csv', usecols=col_list).drop_duplicates()
    hhp_df= pd.read_csv(base_url+'/cleaned/popular_HHP_text_cleaned.csv', usecols=col_list).drop_duplicates()
    MH_df = pd.read_csv(base_url+'/cleaned/popular_MH_text_cleaned.csv', usecols= col_list).drop_duplicates()
    WH_df = pd.read_csv(base_url+'/cleaned/popular_WH_text_cleaned.csv', usecols=col_list).drop_duplicates()
    MP_df = pd.read_csv(base_url+'/cleaned/popular_MedlinePlus_text_cleaned.csv',  usecols=col_list).drop_duplicates()
    Mayo_df =pd.read_csv(base_url+'/cleaned/popular_mayoclinic_texts_FSoLS-24-v2.csv', usecols=col_list).drop_duplicates()


    popular_df_list = [webmd_df, hhp_df, MH_df, WH_df, MP_df,Mayo_df]
    popular_df = pd.concat(popular_df_list, axis=0)


## alternative science
    JBIM_df= pd.read_csv(base_url+'/cleaned/alternative_JEBIM_text_cleaned_FSoLS-24-v2.csv', usecols=col_list)
    CMT_df =pd.read_csv(base_url+'/cleaned/alternative_CMT_text_cleaned_FSoLS-24-v2.csv', usecols=col_list)
    HomeoJ_df = pd.read_csv(base_url+'/cleaned/alternative_homeoJ_text_cleaned.csv', usecols=col_list)
    Goethe_df = pd.read_csv(base_url+'/cleaned/alternative_goethe_text_cleaned.csv', usecols=col_list)
    IJRH_df = pd.read_csv(base_url+'/cleaned/alternative_IJRH_text_cleaned_FoLS-24-v2.csv', usecols=col_list)


    alt_df_list= [JBIM_df, CMT_df, HomeoJ_df, Goethe_df, IJRH_df]
    alternative_df = pd.concat(alt_df_list, axis=0, ignore_index=True).drop_duplicates()

## disinformation
    NN_df = pd.read_csv(base_url+'/cleaned/disinfo_NaturalNews_text_cleaned.csv', usecols=col_list)
    HIN_df  = pd.read_csv(base_url+'/cleaned/disinfo_healthimpactnews_text_cleaned.csv', usecols=col_list)
    Mercola_df = pd.read_csv(base_url+'/cleaned/disinfo_mercola_text_cleaned_4SoLF-24-v2.csv', usecols=col_list)
    HN_df = pd.read_csv(base_url+'/cleaned/disinfo_healthDOTnews_text_cleaned.csv', usecols=col_list)
    IW_df = pd.read_csv(base_url+'/cleaned/disinfo_infowars_text_cleaned.csv', usecols=col_list)

    disi_df_list = [NN_df, HIN_df, Mercola_df, HN_df, IW_df]
    disinfo_df = pd.concat(disi_df_list, axis=0, ignore_index=True).drop_duplicates()
    
    return scientific_df, popular_df, alternative_df, disinfo_df

def filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo):
    pop_df = popular_df.loc[popular_df['tags'] == f'{topic}']
    pop_df_WebMD = pop_df.loc[pop_df['data-source'] == 'WebMD'].head(number_WebMD)
    pop_df_HHP = pop_df.loc[pop_df['data-source'] =='HarvardMedicalSchool'].head(number_HHP)
    pop_df_MH = pop_df.loc[pop_df['data-source'] == 'MensHealth'].head(number_MH)
    pop_df_WH = pop_df.loc[pop_df['data-source']== 'WomensHealth'].head(number_WH)
    pop_df_MP = pop_df.loc[pop_df['data-source'] == 'MedlinePlus'].head(number_MP)
    pop_df_Mayo = pop_df.loc[pop_df['data-source'] == 'mayoclinic'].head(number_Mayo)
    filtered_popular_df = pd.concat([pop_df_WebMD, pop_df_HHP, pop_df_MH, pop_df_WH, pop_df_MP, pop_df_Mayo], axis=0, ignore_index=True)
    return filtered_popular_df


def filter_alternative(alternative_df, topic,number_JEBIM,number_CMT,number_goethe,number_homeoj, number_ijrh):
    alt_df = alternative_df.loc[alternative_df['tags'] == f'{topic}']

    alt_df_JEBIM = alt_df.loc[alt_df['data-source'] == 'JEBIM'].head(number_JEBIM)
    alt_df_CMT = alt_df.loc[alt_df['data-source'] == 'CompMedTherapies'].head(number_CMT)
    alt_df_Goethe = alt_df.loc[alt_df['data-source'] == 'PAAM/Goetheaneum-list'].head(number_goethe)
    alt_df_HomeoJ = alt_df.loc[alt_df['data-source'] == 'homeopathicjournal'].head(number_homeoj)
    alt_df_IJRH = alt_df.loc[alt_df['data-source'] == 'Indian-research-Homeopathy'].head(number_ijrh)
    filtered_alternative_df = pd.concat([alt_df_JEBIM, alt_df_CMT,  alt_df_Goethe, alt_df_HomeoJ, alt_df_IJRH], axis=0, ignore_index=True)
    return filtered_alternative_df


def filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN, number_IW):
    disi_df = disinfo_df.loc[disinfo_df['tags']==f'{topic}']
    disi_df_NN = disi_df.loc[disi_df['data-source']== 'NaturalNews'].head(number_NN)
    disi_df_HIN = disi_df.loc[disi_df['data-source']== 'HealthImpactNews'].head(number_HIN)
    disi_df_MCL = disi_df.loc[disi_df['data-source']== 'Mercola'].head(number_MCL)
    disi_df_HN = disi_df.loc[disi_df['data-source']== 'HealthDOTNews'].head(number_HN)
    disi_df_IW = disi_df.loc[disi_df['data-source']== 'InfoWars'].head(number_IW)
    filtered_disinform_df = pd.concat([disi_df_NN, disi_df_HIN, disi_df_MCL, disi_df_HN, disi_df_IW], axis=0, ignore_index=True)
    return filtered_disinform_df


def filter_for_cumin(scientific_df, popular_df, alternative_df, disinfo_df):
    topic = 'cumin'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] =='cumin'].head(2)

    ## popular
    number_WebMD = 0
    number_HHP = 0
    number_MH = 1
    number_WH = 0
    number_MP = 0
    number_Mayo = 1
    filtered_popular_df = filter_popular(popular_df, topic,number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative-science
    number_JEBIM = 1
    number_CMT = 1
    number_goethe = 0
    number_homeoj = 0
    number_ijrh = 0
    filtered_alternative_df = filter_alternative(alternative_df, topic, number_JEBIM,number_CMT,number_goethe,number_homeoj, number_ijrh)


    ## disinformation
    number_NN = 0
    number_HIN = 1
    number_MCL =  1
    number_HN =  0
    number_IW = 0
    filtered_disinformation_df = filter_disinformation(disinfo_df,topic, number_NN, number_HIN, number_MCL, number_HN, number_IW)

    all_cumin_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_cumin_df


def filter_for_dementia(scientific_df, popular_df, alternative_df, disinfo_df):
    topic = 'dementia'

    ## scientific
    #filtered_scientific_df = scientific_df.loc[scientific_df['tags']=='dementia']
    filtered_scientific_df = scientific_df[scientific_df['tags'].str.contains('dementia', case=False, na=False)].head(86)

    ## popular
    number_WebMD =34
    number_HHP = 22
    number_MH = 5
    number_WH = 6
    number_MP = 19
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM = 33
    number_CMT = 38
    number_homeoj = 12
    number_goethe = 1
    number_ijrh = 2
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe, number_homeoj,
                                     number_ijrh)
    ## disinformation
    number_NN =8
    number_HIN =49
    number_MCL =23
    number_HN =5
    number_IW =1
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)
    all_dementia_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_dementia_df


def filter_for_heartattack(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'heartattack'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'heartattack'].head(72)

    ## popular
    number_WebMD = 35
    number_HHP = 6
    number_MH = 12
    number_WH = 10
    number_MP = 9
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM = 35
    number_CMT =  34
    number_homeoj = 3
    number_goethe = 0
    number_ijrh = 0
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)
    ## disinformation
    number_NN = 18
    number_HIN =22
    number_MCL =30
    number_HN =2
    number_IW =0
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_heartattack_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_heartattack_df

def filter_for_insomnia(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'insomnia'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'insomnia'].head(43)

    ## popular
    number_WebMD = 21
    number_HHP = 11
    number_MH = 0
    number_WH = 6
    number_MP = 5
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM = 15
    number_CMT = 15
    number_homeoj =10
    number_goethe = 3
    number_ijrh = 0
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)
    ## disinformation
    number_NN = 32
    number_HIN =0
    number_MCL =11
    number_HN =0
    number_IW =0
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_insomnia_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_insomnia_df

def filter_for_menopause(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'menopause'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'menopause'].head(40)

    ## popular
    number_WebMD = 22
    number_HHP = 9
    number_MH = 0
    number_WH = 5
    number_MP = 4
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM = 10
    number_CMT = 14
    number_homeoj = 10
    number_goethe = 2
    number_ijrh = 4
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)
    ## disinformation
    number_NN = 10
    number_HIN =21
    number_MCL =6
    number_HN =2
    number_IW =1
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_menopause_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_menopause_df

def filter_for_stroke(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'stroke'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'stroke'].head(126)

    ## popular
    number_WebMD = 94
    number_HHP = 1
    number_MH = 6
    number_WH = 3
    number_MP = 22
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM =46
    number_CMT =40
    number_homeoj =28
    number_goethe =0
    number_ijrh =12
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)
    ## disinformation
    number_NN =71
    number_HIN =23
    number_MCL =26
    number_HN =5
    number_IW =1
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_stroke_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_stroke_df

def filter_for_tobacco(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'tobacco'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'tobacco'].head(21)

    ## popular
    number_WebMD = 0
    number_HHP = 1
    number_MH = 6
    number_WH = 1
    number_MP = 5
    number_Mayo = 8
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM = 4
    number_CMT = 5
    number_homeoj =5
    number_goethe =1
    number_ijrh =6
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)
    ## disinformation
    number_NN =11
    number_HIN =3
    number_MCL =6
    number_HN =1
    number_IW =0
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)
    all_tobacco_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_tobacco_df


def filter_for_turmeric(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'turmeric'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'turmeric'].head(28)

    ## popular
    number_WebMD = 9
    number_HHP = 3
    number_MH = 10
    number_WH = 6
    number_MP = 0
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM = 11
    number_CMT =15
    number_homeoj =1
    number_goethe =0
    number_ijrh =1
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)

    ## disinformation
    number_NN =13
    number_HIN =2
    number_MCL =7
    number_HN =6
    number_IW =0
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_turmeric_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_turmeric_df

def filter_for_measles(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'measles'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'measles'].head(25)

    ## popular
    number_WebMD =8
    number_HHP = 5
    number_MH = 3
    number_WH = 1
    number_MP = 8
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM =8
    number_CMT =6
    number_homeoj =8
    number_goethe = 2
    number_ijrh =1
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)

    ## disinformation
    number_NN =11
    number_HIN =11
    number_MCL =3
    number_HN =0
    number_IW =0
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_measles_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_measles_df

def filter_for_inflammation(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'inflammation'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'inflammation'].head(117)

    ## popular
    number_WebMD = 32
    number_HHP = 21
    number_MH = 32
    number_WH = 19
    number_MP = 13
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM =31
    number_CMT =40
    number_homeoj =30
    number_goethe =5
    number_ijrh =11
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)
    ## disinformation
    number_NN =8
    number_HIN =21
    number_MCL =87
    number_HN =0
    number_IW =1
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_inflammation_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_inflammation_df

def filter_for_vaccination(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'vaccination'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'vaccination'].head(61)

    ## popular
    number_WebMD = 18
    number_HHP = 13
    number_MH = 10
    number_WH = 10
    number_MP = 10
    number_Mayo = 0
    filtered_popular_df= filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM =17
    number_CMT =15
    number_homeoj =13
    number_goethe =2
    number_ijrh =14
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)

    ## disinformation
    number_NN =18
    number_HIN =19
    number_MCL =14
    number_HN =0
    number_IW =10
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_vaccination_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_vaccination_df

def filter_for_transgender(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'transgender'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'transgender'].head(1)

    ## popular
    number_WebMD = 0
    number_HHP = 1
    number_MH = 0
    number_WH = 0
    number_MP = 0
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM =1
    number_CMT =0
    number_homeoj =0
    number_goethe =0
    number_ijrh =0
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)
    ## disinformation
    number_NN =0
    number_HIN =0
    number_MCL =0
    number_HN =0
    number_IW =1
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_transgender_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_transgender_df

def filter_for_abortion(scientific_df,popular_df, alternative_df, disinfo_df):
    topic = 'abortion'

    ## scientific
    filtered_scientific_df = scientific_df.loc[scientific_df['tags'] == 'abortion'].head(44)

    ## popular
    number_WebMD = 14
    number_HHP = 3
    number_MH = 9
    number_WH = 18
    number_MP = 0
    number_Mayo = 0
    filtered_popular_df = filter_popular(popular_df, topic, number_WebMD, number_HHP, number_MH, number_WH, number_MP, number_Mayo)

    ## alternative science
    number_JEBIM =12
    number_CMT =13
    number_homeoj =12
    number_goethe =1
    number_ijrh =3
    filtered_alternative_df = filter_alternative(alternative_df, topic,  number_JEBIM, number_CMT, number_goethe,
                                                 number_homeoj,
                                                 number_ijrh)

    ## disinformation
    number_NN =22
    number_HIN =19
    number_MCL =1
    number_HN =0
    number_IW =2
    filtered_disinformation_df = filter_disinformation(disinfo_df, topic, number_NN, number_HIN, number_MCL, number_HN,
                                               number_IW)

    all_abortion_df = pd.concat([filtered_scientific_df,filtered_popular_df,filtered_alternative_df,filtered_disinformation_df], axis=0, ignore_index=True)
    return all_abortion_df




def main():
    base_url = "/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content"
    col_list = ['category_id', 'tags', 'data-source', 'text']

    scientific_df, popular_df, alternative_df, disinfo_df  = load_datasets(base_url, col_list)
    print('datasets loaded')

    ## filter for topics
    all_cumin_df = filter_for_cumin(scientific_df, popular_df, alternative_df, disinfo_df)
    all_dementia_df = filter_for_dementia(scientific_df, popular_df, alternative_df, disinfo_df)
    all_heartattack_df = filter_for_heartattack(scientific_df, popular_df, alternative_df,disinfo_df)
    all_insomnia_df = filter_for_insomnia(scientific_df, popular_df, alternative_df, disinfo_df)
    all_menopause_df = filter_for_menopause(scientific_df, popular_df, alternative_df, disinfo_df)
    all_stroke_df = filter_for_stroke(scientific_df, popular_df, alternative_df, disinfo_df)
    all_tobacco_df = filter_for_tobacco(scientific_df, popular_df, alternative_df, disinfo_df)
    all_turmeric_df = filter_for_turmeric(scientific_df, popular_df, alternative_df, disinfo_df)
    all_measles_df = filter_for_measles(scientific_df, popular_df, alternative_df,disinfo_df)
    all_inflammation_df = filter_for_inflammation(scientific_df, popular_df, alternative_df, disinfo_df)
    all_vaccination_df = filter_for_vaccination(scientific_df, popular_df, alternative_df, disinfo_df)
    all_transgender_df = filter_for_transgender(scientific_df, popular_df, alternative_df, disinfo_df)
    all_abortion_df = filter_for_abortion(scientific_df, popular_df, alternative_df,disinfo_df)

    print('cumin', all_cumin_df.shape)
    print('dementia', all_dementia_df.shape)
    #print('dementia scie', len(all_dementia_df[all_dementia_df['category_id']=='scientific']))
    #print('dementia pop', len(all_dementia_df[all_dementia_df['category_id']=='popular']))
    #print('dementia alt', len(all_dementia_df[all_dementia_df['category_id'] == 'alternative_science']))
    #print('dementia dis', len(all_dementia_df[all_dementia_df['category_id'] == 'disinfo']))

    print('heartattack', all_heartattack_df.shape)
    print('insomnia', all_insomnia_df.shape)
    print('menopause', all_menopause_df.shape)
    print('stroke', all_stroke_df.shape)
    print('tobacco', all_tobacco_df.shape)
    print('turmeric', all_turmeric_df.shape)
    print('measles', all_measles_df.shape)
    print('inflammation', all_inflammation_df.shape)
    print('vaccination', all_vaccination_df.shape)
    print('transgender', all_transgender_df.shape)
    print('abortion', all_abortion_df.shape)




    print('filtered for topics and data sources')
    all_df_list = [all_cumin_df, all_dementia_df, all_heartattack_df, all_insomnia_df, all_menopause_df, all_stroke_df, all_tobacco_df, all_turmeric_df, all_measles_df, all_inflammation_df, all_vaccination_df,all_transgender_df, all_abortion_df ]
    all_df = pd.concat(all_df_list, axis=0, ignore_index=True)
    #all_df = all_df[['category_id', 'text']]
    print(all_df.shape)
    all_df.to_csv(base_url+'/final_set/final-set_super-balanced_all-infos_2024-08-06_LSoLF-24-v2.csv', index=False)


if __name__ == '__main__':
    main()