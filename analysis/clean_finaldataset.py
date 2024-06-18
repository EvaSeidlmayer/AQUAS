import pandas as pd
import re


def clean_pmc(base_url):
    df = pd.read_csv(base_url+'before_cleaning/scientific_pmc_texts_2024-06-07.csv')

    df.to_csv(base_url + '/cleaned/scientific_pmc_texts_cleaned.csv', index=False)
def clean_webmd(base_url):
    df_1 = pd.read_csv(base_url+'before_cleaning/popular_WebMed_text.csv')
    df_2 = pd.read_csv(base_url+'before_cleaning/popular_WebMed_text-2.csv')
    df = pd.concat([df_1, df_2], axis=0, ignore_index=True)
    df['text'] = df['text'].str.replace('Skip to main content', '')
    df['text'] = df['text'].str.replace('Home Conditions  Back Conditions', '')
    df['text'] = df['text'].replace(to_replace='(?<=View All).*?(?=View All)', value='', regex=True)
    df['text'] = df['text'].replace(to_replace='(?<=View All).*?(?=View Full Guide)', value='', regex=True)
    df['text'] = df['text'].replace(to_replace='(?<=View All).*?(?=min read)', value='', regex=True)
    df['text'] = df['text'].str.replace('View Allmin read', '')
    df.to_csv(base_url+'/cleaned/popular_WebMed_text_cleaned.csv', index=False)

def clean_harvardHealthPublishing(base_url):
    df_1 = pd.read_csv(base_url+'/before_cleaning/popular_HarvardHealthPublishing_text.csv')
    df_2 = pd.read_csv(base_url+'/before_cleaning/popular_HarvardHealthPublishing_text-2.csv')
    df = pd.concat([df_1, df_2], axis=0, ignore_index=True)
    df['text'] = df['text'].str.replace('Harvard Health Publishing', '')
    df['text'] = df['text'].str.replace('Harvard Health', '')
    df['text'].replace(to_replace='(?<=Search).*?(?=Common Conditions)', value='', regex=True)
    df['text'] = df['text'].str.replace('Search', '').str.replace('Common Conditions', '')
    df['text'].replace(to_replace='(?<=Executive Editor).*?(?=Editor in Chief,)', value='', regex=True)
    df['text'] = df['text'].str.replace('Executive Editor', '')
    df['text'] = df['text'].str.replace('Editor in Chief,', '')
    df['text'].replace(to_replace='(?<=, Harvard).*?(?=Editor,)', value='', regex=True)
    df['text'] = df['text'].str.replace('Editorial Advisory Board Member,', '')
    df['text'] = df['text'].str.replace('Reviewed by', '')
    df['text'] = df['text'].str.replace('Health Writer ', '')
    df['text'] = df['text'].str.replace(', Harvard Women\'s Health WatchReviewed by', '')
    df['text'] = df['text'].str.replace(", Harvard Men's Health Watch", '')
    df['text'] = df['text'].str.replace('Close          Shopping Cart                  Customer Service                       Content Licensing                       About Us          Login      Open mobile menu      Menu             Free HealthBeat Signup         Shop      Subscriptions Special Health Reports Online Courses            Pay Subscription Bill ', '')
    df['text'] = df['text'].str.replace('    Staying Healthy                                       Resources                                       Blog                     Helpful Links                Customer Service                         About Us           Login               Content Licensing                                Free Healthbeat Signup                               Subscriptions                               Special Health Reports                               Online Courses                               Pay Subscription Bill                     Recent Blog Articles', '')
    df['text'] = df['text'].str.replace('Staying Healthy   Resources   Blog   COVID-19 Updates       Close menu    Close    Main Content', '')
    df['text'] = df['text'].str.replace("Dupuytren's contracture of the hand        Moving from couch to 5K        How — and why — to fit more fiber and fermented food into your meals        Tick season is expanding: Protect yourself against Lyme disease        What? Another medical form to fill out?        How do trees and green spaces enhance our health?", '')
    df['text'] = df['text'].str.replace("  A muscle-building obsession in boys: What to know and do         Ad Watch: New drug, old song, clever tagline        Concussion in children: What to know and do        What color is your tongue? What's healthy, what's not?      / ", '')
    df['text'] = df['text'].str.replace('Contributor\; ', '')
    df['text'] = df['text'].str.replace("Harvard Women's Health Watch", '')
    df['text'] = df['text'].str.replace('Harvard Heart Letter', '')
    df['text'] = df['text'].str.replace('Sign Me Up', '')
    df['text'] = df['text'].str.replace('Already a member? Login ».', '')
    df['text'] = df['text'].str.strip()
    df['text'].replace(to_replace='(?<=Close).*?(?=Main Content)', value='', regex=True)
    df['text'].replace(to_replace="(?<=CloseShopping Cart).*?(?=What's healthy, what's not?)", value='', regex=True)
    df['text'].replace(to_replace="(?<=Recent Blog Articles).*?(?=Terms of Service apply.)", value='', regex=True)
    #df['text'].replace(to_replace="(?<=).*?(?=Terms of Service apply.)", value='', regex=True)

    df.to_csv(base_url+'/cleaned/popular_HHP_text_cleaned.csv', index=False)

def clean_MH(base_url):
    df_1 = pd.read_csv(base_url+'/before_cleaning/popular_MensHealth_text.csv')
    df_2 = pd.read_csv(base_url+'/before_cleaning/popular_MensHealth_text-2.csv')
    df = pd.concat([df_1, df_2], axis=0, ignore_index=True)
    df['text'] = df['text'].str.replace("Men's Health", '')
    df['text'] = df['text'].str.replace("Subscribe to Men's Health", '')
    df['text'] = df['text'].str.replace('Shop at Amazon', '')
    df['text'] = df['text'].str.replace('Watch Next', '')
    df['text'] = df['text'].str.replace('Related Story', '')
    df.to_csv(base_url+'/cleaned/popular_MH_text_cleaned.csv', index=False)

def clean_WH(base_url):
    df_1 = pd.read_csv(base_url+'before_cleaning/popular_WomensHealth_text.csv')
    df_2 = pd.read_csv(base_url+'before_cleaning/popular_WomensHealth_text-2.csv')
    df = pd.concat([df_1, df_2], axis=0, ignore_index=True)
    df['text'] = df['text'].str.replace("Women's Health", '')
    df['text'] = df['text'].str.replace('Watch Next', '')

    df.to_csv(base_url + '/cleaned/popular_WH_text_cleaned.csv', index= False)

def clean_MedlinePlus(base_url, col_list):
    ##### ? remove "Image credit Courtesy by <name>"
    ##### ? NIH MedlinePlus Magazine

    df_1 = pd.read_csv(base_url+'before_cleaning/popular_MedlinePlus_text_2024-06-12.csv', usecols=col_list)
    df_2 = pd.read_csv(base_url+'before_cleaning/popular_MedlinePlus_text-2_2024-06-12.csv', usecols=col_list)
    df = pd.concat([df_1, df_2], axis=0, ignore_index=True)
    print(df.head)
    df['text'] = df['text'].replace(to_replace='(?<=NIH MedlinePlus Magazine).*?(?=Espaol)', value='', regex=True, )
    df['text'] = df['text'].str.replace("NIH MedlinePlus MagazineEspaol     Espaol  rss facebook  youtube        Search  Search                  Health AZ    Anxiety   Antidepressants   Breast Cancer   Cholesterol   COVID19   Hypothyroidism   Palliative Care   Physical Activity   Skin Conditions   View all topics      NIH Research    Research Highlights   NIH Technology Breakthroughs   Meet the Researchers   Resources at NIH      Issues    Current Issue   Past Issues   Archived Issues      Multimedia    Video   Infographics   Health Fast Facts   All Multimedia      About    Contact us      Subscribe    Email Updates         Search  Search          ",'')

    df.to_csv(base_url + '/cleaned/popular_MedlinePlus_text_cleaned.csv', index= False)

def clean_JEBIM(base_url, col_list):
    df_1 = pd.read_csv(base_url+'before_cleaning/alternative_sagejournalofevidencebasedintegrativemedicine_text.csv', usecols=col_list)
    df_2 = pd.read_csv(base_url + 'before_cleaning/alternative_sagejournalofevidencebasedintegrativemedicine-2.csv', usecols=col_list)
    df = pd.concat([df_1, df_2], axis=0, ignore_index=True).drop_duplicates()
    df['text'] = df['text'].str.replace("Original Article", '')
    df['text'] = df['text'].str.replace('Topical Review Article', '')
    df['text'] = df['text'].str.replace('Review Article', '')
    df['text'] = df['text'].str.replace('Creative Commons Non Commercial CC BYNC This article is distributed under the terms of the Creative Commons AttributionNonCommercial 4.0 Licens e httpscreativecommons.orglicensesbync4.0 which permits noncommercial use reproduction and distribution of the work without furth er permission provided the original work is attributed as specified on the SAGE and Open Access pages httpsus.sagepub.comenusnamopenaccessatsage', '')
    df['text'] = df['text'].str.replace('Creative Commons Non Commercial CC BYNC This article is distributed under the terms of the Creative Commons AttributionNonCommercial 4.0 Licens e httpwww.creativecommons.orglicensesbync4.0 which permits noncommercial use reproduction and distribution of the work without fu rther permission provided the original work is attributed as specified on the SAGE and Open Access pages httpsus.sagepub.comenusnamopenacces satsage', '')
    df['text'] = df['text'].str.replace('Creative Commons Non Commercial CC BYNC This article is distributed under the terms of the Creative Commons AttributionNonCommercial 3.0 Licens e httpwww.creativecommons.orglicensesbync3.0 which permits noncommercial use reproduction and distribution of the work without fu rther permission provided the original work is attributed as specified on the SAGE and Open Access pages httpsus.sagepub.comenusnamopenacces satsage.', '')
    df['text'] = df['text'].str.replace('Creative Commons Non Commercial CC BY NC This article is distributed under the terms of the Creative Commons AttributionNonCommercial 4.0 Licens e httpscreativecommons.orglicensesbync4.0 which permits noncommercial use reproduction and distribution of the work without furth er permission provided the original work is attributed as speci ed on the SAGE and Open Access page httpsus.sagepub.comenusnamopenaccessatsage.Original Manuscript Journal of EvidenceBased Integrative Medicine', '')
    df['text'] = df['text'].str.replace('Creative Commons Non Commercial CC BY NC This article is distributed under the terms of the Creative Commons AttributionNonCommercial 4\.0 Licens e httpscreativecommons\.orglicensesbync4\.0 which permits noncommercial use reproduction and distribution of the work without furth er permission provided the original work is attributed as speci ed on the SAGE and Open Access page httpsus\.sagepub\.comenusnamopenaccessatsage\.', '')
    df['text'] = df['text'].str.replace('journals.sagepub.comhomecam', '')
    df['text'] = df['text'].str.replace('Springer Publishing Company', '')
    df['text'] = df['text'].str.replace('Reprints and permission sagepub.comjournalsPermissions.nav', '')
    df['text'] = df['text'].str.replace('The Authors', '')

    df['text'].replace(to_replace='(?<=Reprints and permission).*?(?=satsage)', value= '', regex=True)
    df['text'].replace(to_replace='(?<=Reprints and permission).*?(?=comhomecam)', value= '', regex=True)
    df['text'] = df['text'].str.replace('httpsus\.sagepub\.comenusnamopenacces satsage', '')

    df.to_csv(base_url + '/cleaned/alternative_JEBIM_text_cleaned.csv', index= False)

def clean_CMT(base_url):
    df = pd.read_csv(base_url+'before_cleaning/alternative_CompMedTherapies_texts_2024-06-05.csv').drop_duplicates()
    #### ? delete items: STUDY PROTOCOL, MEETING ABSTRACTS, REVIEW Open Access, POSTER PRESENTATION, POSTER PRESENTATION ?
    #### delete terms: "alternative" ?
    #### delete: "BMC Complementary and Alternative Medicine"
    df['text'] = df['text'].str.replace("RESEARCH ARTICLE Open Access", '')
    df['text'] = df['text'].str.replace('The Authors', '')
    df['text'] = df['text'].str.replace('This is an Open Access article distributed under the terms of the Creative Commons Attribution License httpcreativecommons.orglicensesby2.0 which permits unrestricted use distribution and reproduction in any medium provided the original work is properly cited.', '')

    df.to_csv(base_url + '/cleaned/alternative_CMT_text_cleaned.csv', index= False)

def clean_homeoJ(base_url):
    df = pd.read_csv(base_url+'before_cleaning/alternative_homeopathicjournal_text_2024-06-05.csv')
    df = df.drop_duplicates(subset=None,keep="first", inplace=False)

    ####### realy remove "received  date" and accepted date"??
    ####### drop_duplicates() does not work

    df['text'].replace(to_replace='(?<=International Journal of Homoeopathic Sciences).*?(?=PISSN)', value='', regex=True)
    df['text'] = df['text'].str.replace(r'International Journal of Homoeopathic Sciences \d{4} \d{2} \d{4,6} EISSN \d{8} PISSN \d{8} www.homoeopathicjournal.com', '', regex=True)
    df['text'] = df['text'].str.replace(        r'International Journal of Homoeopathic Sciences \d{4} \d{2} \d{4,6} EISSN \d{8} PISSN \d{8} www.ho moeopathicjournal.com',        '', regex=True)
    df['text'] = df['text'].str.replace(        r'International Journal of Homoeopathic Sciences \d{4} \d{2} \d{4,6} EISSN \d{8} PISSN \d{8} IJHS \d{4} \d{2} \d{4}',
                                                '', regex=True)
    df['text'] = df['text'].str.replace(r'IJHS \d{4} \d{2} \d{4,6}', '', regex=True)
    df['text'] = df['text'].str.replace(r'Received \d{8}', '', regex=True)
    df['text'] = df['text'].str.replace(r'Accepted \d{8}', '', regex=True)

    df['text'] = df['text'].str.replace('httpwww.homoeopathicjournal.com', '')
    df['text'] = df['text'].str.replace("International Journal of Homoeopathic Sciences", '')

    df.to_csv(base_url + '/cleaned/alternative_homeoJ_text_cleaned.csv', index= False)

def clean_goethe(base_url):
    df = pd.read_csv(base_url+'before_cleaning/alternative_PAAM-goetheaneum_text.csv')
    #### delete: "BMC Complementary and Alternative Medicine
    df['text'] = df['text'].str.replace("RESEARCH ARTICLE Open Access", '')
    df['text'] = df['text'].str.replace('httpwww.hindawi.com', '')
    df['text'] = df['text'].str.replace('www.hindawi.com', '')
    df['text'] = df['text'].str.replace('Hindawi', '')

    df.to_csv(base_url + '/cleaned/alternative_goethe_text_cleaned.csv', index= False)

def clean_IJRH(base_url):
    df = pd.read_csv(base_url+'before_cleaning/alternative_Indian-researchHomeopathy_text.csv')

    df['text'] = df['text'].str.replace(r"\© \d{4} Indian Journal of Research in Homoeopathy \| Published by Wolters Kluwer \- Medknow\d{1,3}", '', regex=True)
    df['text'] = df['text'].str.replace(r'Indian Journal of Research in Homoeopathy', '', regex=True)
    df['text'] = df['text'].str.replace(r'ORIGINAL ARTICLE', '', regex=True)
    df['text'] = df['text'].str.replace(r'For reprints contact: reprints@medknow.com', '', regex=True )
    df['text'] = df['text'].str.replace('medknow', '')
    df['text'] = df['text'].str.replace(r' \[Downloaded free from http\:\/\/www\.ijrh\.org on .+]', '', regex= True)

    df.to_csv(base_url + '/cleaned/alternative_IJRH_text_cleaned.csv', index= False)

def clean_naturalnews(base_url):
    df = pd.read_csv(base_url+'before_cleaning/disinfo_naturalnews_2024-05-24.csv')

    df['text'] = df['text'].str.replace(r'Originally published \b(?:January|Febuary|March|April|May|June|July|August|September|October|November|December?) \d{1,2} \d{4}', '', regex=True)
    df['text'] = df['text'].str.replace('NaturalNews.com', '')
    df['text'] = df['text'].str.replace('medknow', '')
    df['text'] = df['text'].apply(lambda x: x.split('Sources for this article include')[0])
    df['text'] = df['text'].apply(lambda x: x.split('Sources include')[0])
    df['text'] = df['text'].apply(
        lambda x: x.split('Take Action Support Natural News by linking to this article from your website.')[0])
    df['text'] = df['text'].str.replace(
        'Home Brighteon Prep with Mike Interviews Audio Books Download Our App About Us FAQs Search Sections Follow Us Podcast Store Subscribe Live TV Home Politics Culture Health  Medicine Finance  Economy Prepping  Survival Science Technology Popular Articles Today Week Month Year See More Popular Articles Health Ranger Report 5744 Trends Journal pioneer Gerald Celente joins Mike Adams with breaking news analysis of world events and financial outcomes 20913 Brighteon Broadcast News',
        '')
    df['text'] = df['text'].apply(lambda x: x.split('Permalink to this article')[0])
    df['text'] = df['text'].apply(lambda x: x.split('This site is part of the Natural News Network')[0])
    df['text'] = df['text'].str.replace('May 24 2024 WOKE medical schools spontaneously exploding Boeing airliners and other insanities of a wrecked society 1638 Get ready for HISTORIC ANNOUNCEMENT on Memorial Day 2424 Blinken and Nuland push DANGEROUS war escalation with Russia BEGGING for nuclear retaliation 5806 A whole new take on HISTORY Author Christopher Bjerknes challenges everything you think you know about the history of our world 23422 Brighteon Broadcast News May 23 2024 A new Golden Age era of WEALTH and ABUNDANCE is about to commence for nonwestern nations 1119 Priestess of DEATH Victoria Nuland still trying to start World War III with Russia Home', '')

    df.to_csv(base_url+'/cleaned/disinfo_NaturalNews_text_cleaned.csv', index= False)


def clean_HIN(base_url):
    df_1 = pd.read_csv(base_url + 'before_cleaning/disinfo_healthimpactnews-2.csv')
    df_2 = pd.read_csv(base_url + 'before_cleaning/disinfo_healthimpactnews_2024-04-10.csv')
    df = pd.concat([df_1, df_2], axis=0, ignore_index=True).drop_duplicates()

    df['text'] = df['text'].apply(lambda x: x.split('Read the full article here')[0])
    df['text'] = df['text'].apply(lambda x: x.split('Read the Full Article Here')[0])
    df['text'] = df['text'].apply(lambda x: x.split('Read the Full article Here')[0])
    df['text'] = df['text'].apply(lambda x: x.split('Done Please check your email inbox or spam folder for our confirmation email.')[0])
    df['text'] = df['text'].apply(lambda x: x.split('We respect your email privacy')[0])

    df.to_csv(base_url + '/cleaned/disinfo_healthimpactnews_text_cleaned.csv', index=False)

def clean_mercola(base_url):
    df = pd.read_csv(base_url + 'before_cleaning/disinfo_mercola_2024-05-28.csv')
    df.drop_duplicates(inplace=True)

    df['text'] = df['text'].str.replace("['", '')
    df['text'] = df['text'].replace('["', '')
    df['text'] = df['text'].str.replace('by Dr. Joseph Mercola', '')
    df['text'] = df['text'].str.replace(r"Dr\. Mercola\\\'s Censored Library \(Private Membership\)", '', regex=True)
    df['text'] = df['text'].str.replace(r"Dr\. Mercola\'s Censored Library \(Private Membership\)", '', regex=True)
    df['text'] = df['text'].replace(r"SubscribeSign inShare this post", '', regex=True)
    df['text'] = df['text'].str.replace('takecontrol\.substack\.comCopy linkFacebookEmailNoteOther', '')
    df['text'] = df['text'].str.replace(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec?) \d{2}, \d{5}Share this post', '', regex=True)
    df['text'] = df['text'].str.replace('Dr. Joseph Mercola', '')
    df['text'] = df['text'].str.replace('STORY AT-A-GLANCE', '')
    df['text'] = df['text'].str.replace('Copy linkFacebookEmailNoteOther1Share', '')
    df['text'] = df['text'].str.replace('takecontrol.substack.com', '')
    df['text'] = df['text'].apply(lambda x: x.split('\-\-Expand full comment')[0])
    df['text'] = df['text'].apply(lambda x: x.split('Expand full comment')[0])

    df.to_csv(base_url + '/cleaned/disinfo_mercola_text_cleaned.csv', index=False)

def clean_HealthDOTNews(base_url):
    df = pd.read_csv(base_url + 'before_cleaning/disinfo_HealthDOTNews_text.csv')

    df['text'] = df['text'].str.replace('      Your Name Your email Message  or Cancel                      SCIENCE FOOD HEALTH MEDICINE POLLUTION CANCER CLIMATE', '')
    df['text'] = df['text'].str.strip()
    df['text'] = df['text'].str.replace('                                                                      ', '')

    df.to_csv(base_url + '/cleaned/disinfo_healthDOTnews_text_cleaned.csv', index=False)


def clean_infowars(base_url):
    ### attention: we first cleaned and filtered for topics afterwards

    df = pd.read_csv(base_url + 'raw_content/disinfo_infowars_all.csv', on_bad_lines='skip')

    df['text'] = df['text'].dropna()
    df['text'] = df['text'].str.replace('Banned.VideoInfowars StoreNews WarsInfowars LifeSearchSearch ResultsNo Search Results FoundLIVESearchSearch ResultsNo Search Results Found Explore HomeNewsPodcastsBreaking NewsSocial Watch Live Infowars NetworkThe Alex Jones ShowThe War Room with Owen ShroyerThe American Journal More Banned.VideoInfowars StoreArchiveRSSDownload Our AppTerms of ServiceDMCAAdvertise with usAffiliatesMedia', '')
    df['text'] = df['text'].str.replace('InquiriesAbout', '')
    df['text'] = df['text'].str.replace('SharePostTweetMessageEmailLIVESharePostTweetMessageEmailLIVEposted Invalid date agoView More From Terms of ServiceDMCAAdvertise with usAffiliatesMedia InquiriesAbout', '')
    df['text'] = df['text'].str.replace('SharePostTweetMessageEmailLIVESharePostTweetMessageEmailLIVEposted Invalid date agoView More From Terms of ServiceDMCAAdvertise with usAffiliatesMedia', '')
    df['text'] = df['text'].str.replace('DMCAAdvertise with usAffiliatesMedia', '')
    df['text'] = df['text'].str.replace('Terms of Service', '')
    df['text'] = df['text'].str.replace('| Infowars.com', '')

    df.to_csv(base_url + '/cleaned/disinfo_infowars_text_cleaned_topic_not_filtered.csv', index=False)

def main():
    base_url = "/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/content/"
    col_list = ['category_id', 'tags', 'data-source', 'text']

    #clean_pmc(base_url)
    #clean_webmd(base_url)
    #clean_harvardHealthPublishing(base_url)
    #clean_MH(base_url)
    #clean_WH(base_url)
    #clean_MedlinePlus(base_url, col_list)
    #clean_JEBIM(base_url, col_list)
    clean_CMT(base_url)
    #clean_homeoJ(base_url)
    #clean_goethe(base_url)
    #clean_IJRH(base_url)
    #clean_naturalnews(base_url)
    #clean_HIN(base_url)
    #clean_mercola(base_url)
    #clean_HealthDOTNews(base_url)
    #clean_infowars(base_url)

if __name__ == '__main__':
    main()