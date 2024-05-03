#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__description__ = "improve text data, esp. remove NBSP"
__author__ = "Eva Seidlmayer <seidlmayer@zbmed.de>"
__copyright__ = "2023 by Eva Seidlmayer"
__license__ = "ISC license"
__email__ = "seidlmayer@zbmed.de"
__version__ = "1 "


import pandas as pd
import re

df = pd.read_csv('/AQUS/AQUAS/data/data-set_2023/2023-10-12-3_final_dataset_even-more-clean.csv', index_col=False)
print('XXXXXXXXXXXXXXXXXxx', df.groupby('category_id').count())
for i,row in df.iterrows():
    txt = row['text']
    if "BMJ Open" in txt:
        txt = re.sub(r"BMJ Open \d+", '', txt)
    if 'doi10' in txt:
        txt = re.sub('doi\d+/\w+', '', txt)
    if 'httporcid.org' in txt:
        txt = re.sub('httporcid.org\d+', '', txt)
    if '.html' in txt:
        txt = re.sub('\w+.html', '', txt)
    if 'Reference Desk' in txt:
        txt = txt.replace('Reference Desk', '')
    if 'Wikimedia Commons' in txt:
        txt = txt.replace('Wikimedia Commons', '')
    if 'See also' in txt:
        txt = txt.replace('See also', '')
    if 'MedlinePlus Magazine' in txt:
        txt = txt.replace('MedlinePlus Magazine', '')
    if 'MedlinePlus' in txt:
        txt= txt.replace('MedlinePlus', '')
    if 'ClinicalTrials.gov' in txt:
        txt=txt.replace('ClinicalTrials.gov', '')
    if 'MedlinePlus Health Topic' in txt:
        txt = txt.replace('MedlinePlus Health Topic', '')
    if 'Further reading' in txt:
        txt = txt.replace('Further reading', '')
    if 'What You Need to Know' in txt:
        txt = txt.replace('What You Need to Know', '')
    if 'homeopathy' in txt:
        txt = txt.replace('homeopathy', '')
    try:
        txt = re.sub('\d{1,2} \w{3}\. \d{4}', '', txt)
    except Exception as e:
        print(e)
    if 'Retrieved' in txt:
        txt = txt.replace('Retrieved', '')
    try:
        txt = re.sub('\w+ \d{1,2} \d{4}', '', txt)
    except Exception as e:
        print(e)
    if 'ISBN' in txt:
        txt =re.sub('ISBN \d{3}-\d-\d{4}-\d{3}-\d', '', txt)




    row['text'] = txt
print('YYYYYYY', df.groupby('category_id').count())

df.to_csv('data/2023-10-13-1_final_dataset_even-more-clean.csv', index=False)




'''
'REFERENCES'
    'Bibliography'
'''
'''
    if 'Related Issues' in txt:
        txt = txt.replace('Related Issues', '')
    if 'See Play and Learn' in txt:
        txt = txt.replace('See Play and Learn', '')
    if 'Videos and Tutorials' in txt:
        txt = txt.replace('Videos and Tutorials', '')
    if 'No links available' in txt:
        txt = txt.replace('No links available', '')
    if r'(\w+ \d{1,2} \d{4})' in txt:
        txt = re.sub('(\w+ \d{1,2} \d{4})', '', txt)
    if r'https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,4}' in txt:
        txt = re.sub('https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', '', txt)
    if '                    ' in txt:
        txt = txt.replace('                    ', '')
    if 'Videos and Tutorials' in txt:
        txt = txt.replace('Videos and Tutorials', '')
    if 'Videos and Tutorials' in txt:
        txt = txt.replace('Videos and Tutorials', '')




    if 'httporcid\.org\d+' in txt:
        txt = txt.replace('httporcid\.org\d+', '')
    if 'This is an open access article distributed in accordance with the Creative Commons Attribution  license' in txt:
        txt = txt.replace('This is an open access article distributed in accordance with the Creative Commons Attribution  license', '')
    if 'which permits others to distribute remix adapt build upon this work noncommercially and license their derivative works on different terms provided the original work is properly cited appropriate credit is given any changes made indicated and the use is noncommercial.' in txt:
        txt = txt.replace('which permits others to distribute remix adapt build upon this work noncommercially and license their derivative works on different terms provided the original work is properly cited appropriate credit is given any changes made indicated and the use is noncommercial.', '')
    if ' See httpcreativecommons.orglicensesbync4.0.' in txt:
        txt = txt.replace(' See httpcreativecommons.orglicensesbync4.0.', '')
    if 'the .gov website.' in txt:
        txt = txt.replace(' the .gov website.', '')
    if 'Diagnosis and Tests' in txt:
        txt = txt.replace('Diagnosis and Tests', '')
    if 'see more articles' in txt:
        txt = txt.replace('see more articles', '')
    if 'Medical Encyclopedia' in txt:
        txt = txt.replace('Medical Encyclopedia', '')
    if 'Find an Expert' in txt:
        txt = txt.replace('Find an Expert', '')
    if 'External links' in txt:
        txt = txt.replace('External links', '')
    if '                                                                   ' in txt:
        txt = txt.replace('                                                                   ', '')
    if 'the .gov website.' in txt:
        txt= txt.replace('the .gov website.', '')
    if 'Summary' in txt:
        txt = txt.replace('Summary', '')
    if 'Learn More' in txt:
        txt = txt.replace('Learn More', '')
    if 'Medical Encyclopedia' in txt:
        txt = txt.replace('Medical Encyclopedia', '')
    if 'Department of Health and Human Services Office on Womens Health' in txt:
        txt = txt.replace('Department of Health and Human Services Office on Womens Health', '')
    if 'Mayo Foundation for Medical Education and Research' in txt:
        txt = txt.replace('Mayo Foundation for Medical Education and Research', '')
    if 'American College of Radiology' in txt:
        txt = txt.replace('American College of Radiology', '')
    if 'Clinical Trials                                                                                        ClinicalTrials.gov' in txt:
        txt = txt.replace('Clinical Trials                                                                                        ClinicalTrials.gov', '')
    if 'National Institutes of Health' in txt:
        txt = txt.replace('National Institutes of Health', '')
    if 'Journal Articles' in txt:
        txt = txt.replace('Journal Articles', '')
    if 'References and abstracts from MEDLINENational Library of MedicineArticle' in txt:
        txt = txt.replace(' References and abstracts from MEDLINENational Library of MedicineArticle', '')
    if 'Patient Handouts' in txt:
        txt = txt.replace('Patient Handouts', '')
    if 'National Institutes of Health' in txt:
        txt = txt.replace('National Institutes of Health', '')
    if 'Disclaimers' in txt:
        txt = txt.replace('Disclaimers', '')
    if 'MEDICAL ENCYCLOPEDIA' in txt:
        txt = txt.replace('MEDICAL ENCYCLOPEDIA', '')
    if 'â'in txt:
        txt = txt.replace('â', '')
    if 'Agree and close' in txt:
        txt = txt.replace('Agree and close', '')
    if 'â' in txt:
        txt = txt.replace('â', '')
    if 'â' in txt:
        txt = txt.replace('â', '')
    if 'By continuing to browse our site you agree to our use of cookies and our Privacy Policy.' in txt:
        txt = txt.replace('By continuing to browse our site you agree to our use of cookies and our Privacy Policy.', '')
    if 'Subscribe  x'in txt:
        txt = txt.replace('Subscribe  x', '')
    if 'Subscription confirmation required.CommentsPlease enable JavaScript to view the comments powered by Disqus.comments powered by DisqusGet Our Free Email NewsletterGet independent news alerts on natural cures, food lab tests, cannabis medicine, science, robotics, drones, privacy and more.' in txt:
        txt = txt.replace('Subscription confirmation required.CommentsPlease enable JavaScript to view the comments powered by Disqus.comments powered by DisqusGet Our Free Email NewsletterGet independent news alerts on natural cures, food lab tests, cannabis medicine, science, robotics, drones, privacy and more.', '')
    if 'Your privacy is protected. Subscription confirmation required.RECENT NEWS & ARTICLES' in txt:
        txt = txt.replace('Your privacy is protected. Subscription confirmation required.RECENT NEWS & ARTICLES', '')
    if 'Sources include:' in txt:
        txt = txt.replace('Sources include:', '')
    if 'Submit a correction' in txt:
        txt = txt.replace('Submit a correction', '')
    if '>>Tagged Under:' in txt:
        txt = txt.replace('>>Tagged Under:', '')
    if 'This article may contain statements that reflect the opinion of the authorGet Our Free Email NewsletterGet independent news alerts on natural cures, food lab tests, cannabis medicine, science, robotics, drones, privacy and more.Your privacy is protected. Subscription confirmation required.' in txt:
        txt = txt.replace('This article may contain statements that reflect the opinion of the authorGet Our Free Email NewsletterGet independent news alerts on natural cures, food lab tests, cannabis medicine, science, robotics, drones, privacy and more.Your privacy is protected. Subscription confirmation required.', '')
    if '/ By ' in txt:
        try:
            txt = re.sub('(\d{2}/\d{2}/\d{4}) / By (\w+ \w+)', '', txt)
        except Exception as e:
            print(e)
'''


'''   
    if 'EDITORIAL' in txt:
        txt = txt.replace('EDITORIAL', '')
    if 'httpsdoi.org10.' in txt:
        try:
            txt = re.sub('httpsdoi.org10\.\d+/\w+', '', txt)
        except Exception as e:
            print(e)
    if 'doi10.' in txt:
        try:
            txt = re.sub('doi0\.\d+/\w+', '', txt)
        except Exception as e:
            print(e)
            
    if 'DOI 10.' in txt:
        try:
            txt = re.sub('DOI 10\.\d+/\w+', '', txt)
        except Exception as e:
            print(e)
    if 'Received' in txt:
        try:
            txt = re.sub('Received \d+ \w+ \d+', '', txt)
        except Exception as e:
            print(e)
    if 'Accepted' in txt:
        try:
            txt = re.sub('Accepted \d+ \w+ \d+', '', txt)
        except Exception as e:
            print(e)
    if 'The copyright holder for this preprint which was not certified by peer review is the authorfunder who has granted medRxiv a license to display the preprint in perpetuity. It is made available under a CCBYNCND 4.0 International license .' in txt:
        txt = txt.replace('The copyright holder for this preprint which was not certified by peer review is the authorfunder who has granted medRxiv a license to display the preprint in perpetuity. It is made available under a CCBYNCND 4.0 International license .', '')
    if 'medRxiv preprint doi' in txt:
        try:
            txt = re.sub('medRxiv preprint doi httpsdoi.org10.[\d+\w+.] this version posted \w+ \d+ \d+.', '', txt)
        except Exception as e:
            print(e)
    if 'International Journal of Homoeopathic Sciences' in txt:
        txt = txt.replace('International Journal of Homoeopathic Sciences', '')
    if 'Homeopathic' in txt:
        txt = txt.replace('Homeopathic', '')
    if 'Homeopathy' in txt:
        txt = txt.replace('Homeopathy', '')
    if 'This is an Open Access article distributed under the terms of the Creative Commons' in txt:
        txt = txt.replace('This is an Open Access article distributed under the terms of the Creative Commons', '')
    if 'This is an Open Access article' in txt:
        txt = txt.replace('This is an Open Access article', '')
    if 'Open access' in txt:
        txt = txt.replace('Open access', '')
    if 'Non Commercial CC BYNC 4.0' in txt:
        txt = txt.replace('Non Commercial CC BYNC 4.0', '')
    if 'license which permits others to distribute remix adapt build upon this work noncommercially and license their derivative works on different terms provided the original work is properly cited and the use is noncommercial.' in txt:
        txt = txt.replace('license which permits others to distribute remix adapt build upon this work noncommercially and license their derivative works on different terms provided the original work is properly cited and the use is noncommercial.', '')
    if 'Introduction' in txt:
        txt = txt.replace('Introduction', '')
    if 'Acknowledgements' in txt:
        txt = txt.replace('Acknowledgements', '')
    if 'Conflict of interest The authors declare no conflict of interest.' in txt:
        txt = txt.replace('Conflict of interest The authors declare no conflict of interest.', '')
    if 'Conflict of interest' in txt:
        txt = txt.replace('Conflict of interest', '')
    if 'Epub' in txt:
        try:
            txt = re.sub('Epub \d+.', '', txt)
        except Exception as e:
            print(e)
    if 'PubMed' in txt:
        try:
            txt = re.sub('PubMed.', '', txt)
        except Exception as e:
            print(e)
    if 'PMID' in txt:
        try:
            txt = re.sub('PMID \d+', '', txt)
        except Exception as e:
            print(e)
    if 'PubMed Central' in txt:
        try:
            txt = re.sub('PubMed Central', '', txt)
        except Exception as e:
            print(e)
    if 'PMCID' in txt:
        txt = txt.replace('PMCID', '')
    if 'PMC' in txt:
        txt = txt.replace('PMC', '')
    if 'Administration' in txt:
        txt = txt.replace('Administration', '')
'''



'''
    try:
        txt = re.sub('pISSN \d+', '', txt)
    except Exception as e:
        print(e)
    try:
        txt = re.sub('ISSN \d+', '', txt)
    except Exception as e:
        print(e)

    if "httpsorcid.org" in txt:
        try:
            txt = re.sub('httpsorcid.org"[\d]+', '', txt)
        except Exception as e:
            print(e)
    if 'httpsdoi.org10.' in txt:
        try:
            txt = re.sub('httpsdoi.org\b10\.\d+/\w+', '', txt)
        except Exception as e:
            print(e)
    if 'DOI' in txt:
        try:
            txt = re.sub('DOI \b(10\.\d+/\w+)', '', txt)
        except Exception as e:
            print(e)

    if 'Vol.' in txt:
        try:
            txt = re.sub('Vol. \d+', '', txt)
        except Exception as e:
            print(e)
    if 'VOLUME' in txt:
        try:
            txt = re.sub('VOLUME \d+', '', txt)
        except Exception as e:
            print(e)
    if 'NUMBER' in txt:
        try:
            txt = re.sub('NUMBER \d+', '', txt)
        except Exception as e:
            print(e)
'''








'''
    if 'Original article' in txt:
        txt = txt.replace('Original article', '')
    if 'ORIGINAL ARTICLE' in txt:
        txt = txt.replace('ORIGINAL ARTICLE', '')
    if 'Cite this' in txt:
        txt = txt.replace('Cite this', '')
    if 'PUBMED' in txt:
        txt = txt.replace('PUBMED', '')
    if 'CROSSREF' in txt:
        txt = txt.replace('CROSSREF', '')
    if 'ORIGINAL RESEARCH' in txt:
        txt = txt.replace('ORIGINAL RESEARCH', '')
    if 'Research Article' in txt:
        txt = txt.replace('Research Article', '')
    if 'Corresponding author' in txt:
        txt = txt.replace('Corresponding author', '')
    if ' lock   ' in txt:
        txt = txt.replace(' lock   ', '')
    if 'Topics' in txt:
        txt = txt.replace('Topics', '')
    if 'URL of this page ' in txt:
        txt = txt.replace('URL of this page ', '')
    if 'URL of this page' in txt:
        txt = txt.replace('URL of this page', '')
    if 'httpsmedlineplus.gov' in txt:
        txt = txt.replace('httpsmedlineplus.gov', '')
    if 'On this pageBasicsSummaryStart' in txt:
        txt = txt.replace('On this pageBasicsSummaryStart ', '')
    if 'HereSymptomsDiagnosis and Tests' in txt:
        txt = txt.replace('HereSymptomsDiagnosis and Tests', '')
    if 'Learn MoreRelated IssuesSpecificsGeneticsSee ' in txt:
        txt = txt.replace('Learn MoreRelated IssuesSpecificsGeneticsSee', '')
    if 'Play and LearnNo links availableResearchClinical Trials' in txt:
        txt = txt.replace('Play and LearnNo links availableResearchClinical Trials', '')
    if 'Play and LearnNo links availableResearchClinical Trials' in txt:
        txt = txt.replace('Play and LearnNo links availableResearchClinical Trials', '')
    if 'Journal ArticlesResourcesReference DeskFind an ExpertFor YouChildrenPatient Handouts' in txt:
        txt = txt.replace('Journal ArticlesResourcesReference DeskFind an ExpertFor YouChildrenPatient Handouts', '')
    if 'Start Here' in txt:
        txt = txt.replace('Start Here', '')
    if 'The primary NIH organization for research on' in txt:
        txt = txt.replace('The primary NIH organization for research on', '')
    if 'Find health information in languages other than English on' in txt:
        txt = txt.replace('Find health information in languages other than English on', '')
    if 'Other Languages' in txt:
        txt = txt.replace('Other Languages', '')
    if 'Disclaimers' in txt:
        txt = txt.replace('Dsiclaimers', '')
    if 'PDF' in txt:
        txt = txt.replace('PDF', '')
    if 'Topic Image' in txt:
        txt = txt.replace('Topic Image', '')
    if 'The primary NIH organization for research on ' in txt:
        txt = txt.replace('The primary NIH organization for research on ', '')
   
'''



'''
for i, row in df.iterrows():
    txt = row['text']
    txt = txt.replace('\r', '')
    if 'Accepted 05042022' in txt:
        txt = txt.replace('Accepted 05042022', '')
    if 'PMC free article' in txt:
        txt = txt.replace('PMC free article', '')
    if 'PubMed Google Scholar' in txt:
        txt = txt.replace('PubMed Google Scholar', '')
    if 'homeopathy' in txt:
        txt = txt.replace('homeopathy', '')
    if 'Homoeopathic' in txt:
        txt = txt.replace('Homoeopathic', '')
    if "httpsorcid.org" in txt:
        try:
            txt = re.sub('["httpsorcid.org"\d*]', '', txt)
        except Exception as e:
            print(e)
    if 'httpsdoi.org10.' in txt:
        try:
            txt = re.sub('["httpsdoi.org"\b(10[.]]', '', txt)
        except Exception as e:
            print(e)

    if '>>Disclaimer: The entire contents of this website are based upon the opinions of Dr. Mercola, unless otherwise noted.' in txt:
        txt = txt.replace('>>Disclaimer: The entire contents of this website are based upon the opinions of Dr. Mercola, unless otherwise noted.', '')
    if 'today to begin accessing must-read information you won\'t find anywhere else. Over 351,000 subscribersSubscribeContinue readingSign in' in txt:
        txt = txt.replace('today to begin accessing must-read information you won\'t find anywhere else. Over 351,000 subscribersSubscribeContinue readingSign in', '')
    if 'Individual articles are based upon the opinions of the respective author, who retains copyright as marked.' in txt:
        txt = txt.replace('Individual articles are based upon the opinions of the respective author, who retains copyright as marked.', '')
    if 'The information on this website is not intended to replace a one-on-one relationship with a qualified health care professional and is not intended as medical advice. ' in txt:
        txt = txt.replace('The information on this website is not intended to replace a one-on-one relationship with a qualified health care professional and is not intended as medical advice.', '')
    if 'It is intended as a sharing of knowledge and information from the research and experience of Dr. Mercola and his community.' in txt:
        txt = txt.replace('It is intended as a sharing of knowledge and information from the research and experience of Dr. Mercola and his community.', '')
    if ' Dr. Mercola encourages you to make your own health care decisions based upon your research and in partnership with a qualified health care professional. ' in txt:
        txt = txt.replace(' Dr. Mercola encourages you to make your own health care decisions based upon your research and in partnership with a qualified health care professional.', '')
    if 'The subscription fee being requested is for access to the articles and information posted on this site, and is not being paid for any individual medical advice.' in txt:
        txt = txt.replace('The subscription fee being requested is for access to the articles and information posted on this site, and is not being paid for any individual medical advice.', '')
    if 'If you are pregnant, nursing, taking medication, or have a medical condition, consult your health care professional before using products based on this content.' in txt:
        txt = txt.replace('If you are pregnant, nursing, taking medication, or have a medical condition, consult your health care professional before using products based on this content.', '')
    if '\nDr. Mercola\'s Censored Library' in txt:
        txt = txt.replace('\nDr. Mercola\'s Censored Library', '')
    if 'Dr. Mercola\'s Censored Library' in txt:
        txt = txt.replace('Dr. Mercola\'s Censored Library', '')
    if '(Private Membership)SubscribeSign' in txt:
        txt = txt.replace('(Private Membership)SubscribeSign', '')
    if '(Private Membership)' in txt:
        txt = txt.replace('(Private Membership)', '')

    if 'Join the private membership of' in txt:
        txt = txt.replace('Join the private membership of', '')
    if 'inShare this' in txt:
        txt = txt.replace('inShare this ', '')
    if 'takecontrol.substack.comCopy' in txt:
        txt = txt.replace('takecontrol.substack.comCopy', '')
    if 'takecontrole' in txt:
        txt = txt.replace('takecontrol', '')
    if 'linkFacebookEmailNotesOtherDiscover' in txt:
        txt = txt.replace('linkFacebookEmailNotesOtherDiscover', '')
    if 'NEXT ARTICLE' in txt:
        txt = txt.replace('NEXT ARTICLE', '')
    if 'Tag an attorney general in your post.' in txt:
        txt = txt.replace('Tag an attorney general in your post.', '')
    if 'Read the full article' in txt:
        txt = txt.replace('Read the full article', '')

    row['text']= txt
df.to_csv('data/2023-10-10_final_dataset_even-more-clean.csv', index= False)
'''

#DOI httpsdoi.org10.3354526164485.2020.v4.i2d.178



'  '
'takecontrol.substack.comCopy linkFacebookEmailNotesOther1Share1 CommentShare this discussion'
'Joseph MercolaPrivacy ∙ Terms ∙ Collection notice Start WritingGet the appSubstack is the home for great writingOur use of cookies\n  We use necessary cookies to make our site work. We also set performance and functionality cookies that help us make\n  improvements by measuring traffic on our site. For more detailed information about the cookies we use, please see our\n  privacy policy.\n  ✖        This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts'
# 'at Popular Rationalism Substack.RelatedVideo source.')







'''
for i, row in df.iterrows():

        txt  =row['text']
        if 'MedlinePlus links to health information from the National Institutes of Health and other federal government agencies.' in txt:
            txt= txt.replace('MedlinePlus links to health information from the National Institutes of Health and other federal government agencies.', '')
        if 'MedlinePlus also links to health information from nongovernment Web sites. See our disclaimer about external links and our quality guidelines.' in txt:
            txt = txt.replace('MedlinePlus also links to health information from nongovernment Web sites. See our disclaimer about external links and our quality guidelines.', '')
        if 'The information on this site should not be used as a substitute for professional medical care or advice. Contact a health care provider if you have questions about your health.Learn how to cite this pageAbout' in txt:
            txt = txt.replace('The information on this site should not be used as a substitute for professional medical care or advice. Contact a health care provider if you have questions about your health.Learn how to cite this pageAbout', '')
        if 'MedlinePlusWhats' in txt:
            txt = txt.replace('MedlinePlusWhats','')
        if 'NewSite' in txt:
            txt = txt.replace('NewSite', '')
        if 'MapCustomer' in txt:
            txt = txt.replace('MapCustomer', '')
        if 'SupportGet' in txt:
            txt = txt.replace('SupportGet', '')
        if 'updatesSubscribe to RSSFollow' in txt:
            txt = txt.replace('updatesSubscribe to RSSFollow', '')
        if 'usSocial Media'  in txt:
            txt = txt.replace('usSocial Media', '')
        if 'ToolkitNLM Web' in txt:
            txt = txt.replace('ToolkitNLM Web', '')
        if 'PoliciesCopyrightAccessibilityGuidelines for LinksViewers' in txt:
            txt = txt.replace('PoliciesCopyrightAccessibilityGuidelines for LinksViewers', '')
        if 'PlayersHHS Vulnerability' in txt:
            txt = txt.replace('PlayersHHS Vulnerability', '')
        if 'DisclosureMedlinePlus' in txt:
            txt = txt.replace('DisclosureMedlinePlus', '')
        if 'Connect for EHRsFor' in txt:
            txt = txt.replace('Connect for EHRsFor', '')
        if 'DevelopersNational Library of Medicine8600 Rockville Pike Bethesda MD 20894U.S.' in txt:
            txt = txt.replace('DevelopersNational Library of Medicine8600 Rockville Pike Bethesda MD 20894U.S.', '')
        if 'Department of Health and Human ServicesNational Institutes of HealthLast updated' in txt:
            txt = txt.replace('Department of Health and Human ServicesNational Institutes of HealthLast updated', '')
        if 'Share sensitive information only on official              secure websites.' in txt:
            txt = txt.replace('Share sensitive information only on official              secure websites.', '')
        if 'Original Article' in txt:
            txt = txt.replace('Original Article', '')
        if  "RESEARCH ARTICLE" in txt:
            txt = txt.replace( "RESEARCH ARTICLE", '')
        if '. . .' in txt:
            txt = txt.replace('. . .', '')
        if 'Also in Spanish' in txt:
            txt = txt.replace('Also in Spanish', '')
        if 'MedlinePlusSkip navigation' in txt:
            txt = txt.replace('MedlinePlusSkip navigation', '')
        if 'An official website of the United States government' in txt:
            txt = txt.replace('An official website of the United States government', '')

        if 'Heres how you know' in txt:
            txt = txt.replace('Heres how you know', '')
        if 'Official websites use .govA' in txt:
            txt = txt.replace('Official websites use .govA', '')
        if '.gov website belongs to an official government' in txt:
            txt = txt.replace('.gov website belongs to an official government', '')
        if 'organization in the United States.' in txt:
            txt = txt.replace('organization in the United States.', '')
        if 'Secure .gov websites use HTTPSA' in txt:
            txt = txt.replace('Secure .gov websites use HTTPSA', '')
        if 'LockLocked padlock icon  or https means youve safely connected to' in txt:
            txt = txt.replace('LockLocked padlock icon  or https means youve safely connected to', '')
        if 'the .gov website. Share sensitive information only on official' in txt:
            txt = txt.replace('the .gov website. Share sensitive information only on official secure websites.', '')
        if 'National Library of MedicineMenuHealth' in txt:
            txt = txt.replace('National Library of MedicineMenuHealth', '')
        if  'TopicsDrugs' in txt:
            txt = txt.replace('TopicsDrugs' , '')
        if 'SupplementsGeneticsMedical'  in txt:
            txt = txt.replace('SupplementsGeneticsMedical' , '')
        if 'TestsMedical' in txt:
            txt = txt.replace('TestsMedical', '')
        if 'EncyclopediaAbout' in txt:
            txt = txt.replace('EncyclopediaAbout', '')
        if 'MedlinePlusSearchSearch' in txt:
            txt = txt.replace('MedlinePlusSearchSearch', '')
        if 'MedlinePlusGOAbout' in txt:
            txt = txt.replace('MedlinePlusGOAbout', '')
        if 'MedlinePlusWhats' in txt:
            txt = txt.replace('MedlinePlusWhats', '')
        if  'NewSite' in txt:
            txt = txt.replace('NewSite', '')
        if 'MapCustomer' in txt:
            txt = txt.replace('MapCustomer', '')
        if 'SupportHealth' in txt:
            txt = txt.replace('SupportHealth', '')
        if 'TopicsDrugs' in txt:
            txt = txt.replace('TopicsDrugs', '')
        if 'Open Access Full Text Article' in txt:
            txt = txt.replace('Open Access Full Text Article', '')
        if 'journal homepage www.sciencedirect.com' in txt:
            txt = txt.replace('journal homepage www.sciencedirect.com', '')
        if 'SupplementsGeneticsMedical' in txt:
            txt = txt.replace('SupplementsGeneticsMedical', '')
        if 'TestsMedical' in txt:
            txt = txt.replce('TestsMedical', '')
        if 'EncyclopediaEspaolYou Are' in txt:
            txt = txt.replace('EncyclopediaEspaolYou Are', '')
        if 'HereHomeHealth' in txt:
            txt = txt.replace('HereHomeHealth', '')
        if 'TopicsSclerodermaURL of this page' in txt:
            txt = txt.replace('TopicsSclerodermaURL of this page', '')
        if 'httpsmedlineplus.govscleroderma.html' in txt:
            txt = txt.replace('httpsmedlineplus.govscleroderma.html', '')

        try:
            text = re.sub('[Received \d* [a-zA-Z]+ \d+]' , '',txt)
        except Exception as e:
            print(e)
        try:
            text = re.sub('[Revised \d* [a-zA-Z]+ \d+]' , '',txt)
        except Exception as e:
            print(e)
        try:
            text = re.sub('[Accepted \d* [a-zA-Z]+ \d+]' , '',txt)
        except Exception as e:
            print(e)
        try:
            text = re.sub('[Print ISSN \d*]' , '',txt)
        except Exception as e:
            print(e)
        try:
            text = re.sub('[Online ISSN \d*]' , '',txt)
        except Exception as e:
            print(e)
            
        row['text'] = txt    
#df.to_csv('data/2023-10_final_dataset_even-more-clean.csv', index= False)

'''






'''
"1661 13 except w i t h mouse strains such as A K R which s p o n t a n e o u s l y p r o d u c e ecotropic virus. 2 T h e differential effects o f B r d U t r e a t m e n t on fibroblasts B cells a n d T cells suggest t h a t virus i n d u c i b i l i t y is d e p e n d e n t on the cell differentiation stage. T h e observation t h a t B r d U a p p e a r s to a m p l i f y x e n o t r o p i c virus p r o d u c t i o n from B cells r a t h e r t h a n i n d u c i n g it as in fibroblasts raises the question w h e t h e r the m e c h a n i s m o f B r d U action on x e n o t r o p i c virus expression is the s a m e in B cells a n d fibroblasts. T o e x a m i n e this question we have t a k e n a genetic a p p r o a c h to ask w h e t h e r L P S a n d B r d U plus L P S in fact i n d u c e one a n d the s a m e virus m e a s u r e d b o t h in infectivity assays a n d b y reverse transcriptase a n d w h e t h e r this is the s a m e virus i n d u c e d from fibroblasts. F u r t h e r m o r e  we h a v e asked w h e t h e r a d d i t i o n a l proviruses are induced. T h e results p r e s e n t e d here c o n f i r m the results o f K o z a k a n d R o w e 10 t h a t infectious x e n o t r o p i c virus i n d u c t i o n b y B r d U plus L P S from spleen cells is u n d e r the control o f t h e s a m e gene as in fibroblasts. In a d d i t i o n they show that i n d u c t i o n b y L P S  LP L P  B r d U  a n d C o n A  B r d U are c o n t r o l l e d b y the same genetic locus a n d t h a t L P S induces the expression in l y m p h o c y t e s o f a second i n d e p e n d e n t l y segregating e n d o g e n o u s g e n o m e c o d i n g for an a p p a r e n t l y defective virus."



"Author manuscript available in PMC 2015 March 18. Published in final edited form as Nature."

" PUBLISHED BY ELSEVIER ON BEHALF OF THE AMERICAN COLLEGE OF CARDIOLOGY FOUNDATION. THIS IS AN OPEN ACCESS ARTICLE UNDER THE CC BYNCND LICENSE"
'''