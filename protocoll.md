# deNBI VM
deNBI VM: scp -P 30327  -i ~/.ssh/id_rsa.pub  data/final_dataset.csv ubuntu@129.70.51.6:/home/ubuntu
VM parameter: VM: 1; Flavour: de.NBI GPU medium
total core: 14
total RAM: 64GB
total GPUs: 1
Storage Limit 500 GB
Volume Counter 
Bert: https://github.com/huggingface/transformers/blob/v4.28.1/src/transformers/models/bert/modeling_bert.py#L1533

# Conferences
- EU DisinfoLab 2024 Annual Conference 9-10 October  2024, Riga, Latvia: 	https://www.disinfo.eu/conference/
- EMBL Science and Society Conference In science we trust? 16 - 17 Jun 2025 , Heidelberg,  https://www.embl.org/about/info/course-and-conference-office/events/sns25-01/

# Definition disinformation 
- "We define **misinformation** as the intentional or unintentional spread of inaccurate information, including through unchecked opinions. This differs from **disinformation**, where intent is a required factor." (https://www.dictionary.com/e/misinformation-vs-disinformation-get-informed-on-the-difference/)
- **Disinformation** is Intentionally spread false  information that follows another purpose than truth. such as profit or a political or religious agenda. 
- Currently, a working group of the Institute of Electrical and Electronics Engineers (IEEE) is currently drafting a **standard for the credibility of news sites**.\footnote{\href{https://development.standards.ieee.org/myproject-web/public/view.html\#pardetail/6318}{https://development.standards.ieee.org/myproject-web/public/view.html\#pardetail/6318}, retrieval date Sep 20, 2023.} Although  teh standard is not related to scientific information sources, it may provide guidance for the context described here. A standard for scientificity itself is not currently available  to our knowledge.
- as two categories misinformation form together with disinformation  **fake news** for Lazer et al. as fabricated information (D. M. J. Lazer, M. A. Baum, Y. Benkler, A. J. Berinsky, K. M. Greenhill, F. Menczer, M. J. Metzger, B. Nyhan, G. Pennycook, D. Rothschild, M. Schudson, S. A. Sloman, C. R. Sunstein, E. A. Thorson, D. J. Watts, and J. L. Zittrain, “The science of fake news,” Science, vol. 359, no. 6380, pp. 1094–1096, 2018.)
- "Moreover, Waldrop observes the seven different types of mis- and disinformation: satire, misleading content, imposter content, fabricated content, false connection, false context, and manipulated content. The seven different types of fake news vary in their degree of intent to deceive." (citation Garima Chaphekar 2022:1) . M. Waldrop, “The genuine problem of fake news,” Proceedings of the National Academy of Sciences, vol. 114, no. 48, pp. 12631–12634, 2017. 
- "Disinformation, in this context, is viewed as 'a product of a carefully planned and technically sophisticated deceit process' (Fallis, 2009) by grabbing attention and monetizing it to meet rentseeking ends. Rent seekers pursue interests in the competition for this attention and use disinformation to attract that attention. Disinformation affects public opinion, which not only affects businesses but also has other socio-economic and public policy consequences (Lewandowsky, Ecker, Seifert, Schwarz, & Cook, 2012; Paarlberg, 2014)." (cited after Ryan et al. 2020)
- Literture review on Disinformation in contrast to misinformation, on disinformation in the context of an interconnected world, and on Monetizing disinformation in the attention economy (Ryan et al. 2020)  
- "Bad science is where data have been cherry-picked -- when some data have ben deliberately lft out -- or it's impossible for the reader to understand the steps that were taken, to produce or analyze the data." (Oreskes/Conway 2012, page 153.)
- Santos-d'amorim/miranda 2021: own definition "Hence, (2) misinformation is imprecise information,  open  to  multiple  comprehensions  and  uses; (2)  disinformation  is  information deliberately deceptive, intending to deceive or not; and (3) malinformation is the sensitive information(true)that  is  strategically  used  to  cause advantage." / "Hence,   (i)   misinformation   is   inaccurate information, open to multiple comprehensions and uses, being the prefix mis–,an indication of  mistake  or  something  wrong. (ii) disinformation  is  information  deliberately  deceptive, intending to deceive;and (iii) malinformationis thesensitiveinformation that is strategically used to cause advantage, whetherpersonalorinstitutional." 
- 
- Santos-d'amorim/Miranda 2021 provide a chart of definitions: ![definitionsMisMalDisinformation_Santos-d'amorim-miranda.png](/home/ruth/ProgrammingProjects/AQUS/AQUAS/definitionsMisMalDisinformation_Santos-d'amorim-miranda.png)

# Initatives for science quality
- https://www.newsguardtech.com/
- MediaBias/FactCheck: https://mediabiasfactcheck.com/, "MBFC is an independent organization that aims to detect bias of media and other information sources by following a very strict manual methodology [ 19 ], that makes use of a combination of objective measures" (Papadogiannakis 2023)
- Center for inquiry, USA: https://centerforinquiry.org/
- "Quackwatch - Your Guide to Quackery, Health Fraud, and Intelligent Decisions", U.S.A.: https://quackwatch.org/
- Institue for strategic dialogue, London: https://www.isdglobal.org/
- Medwatch, Hamburg: https://medwatch.de/
- Check my Ads Initiative: https://checkmyads.org/
- Global Disinformation Index: https://www.disinformationindex.org/
- American Council of Science and health, "Promoting science and debunking junk science since 1978": https://www.acsh.org/
- Climate investigations Centre: https://climateinvestigations.org
- University of California: An archive of 14 million documents created by tobacco companies about their advertising, manufacturing, marketing, scientific research and political activities, hosted by the UCSF Library. https://www.industrydocuments.ucsf.edu/tobacco/
- Heidelberger Appeal: Unknown. HEIDELBERG APPEAL TO HEADS OF STATES AND GOVERNMENTS. 1992 April 14. Philip Morris Records; Master Settlement Agreement. Unknown. https://www.industrydocuments.ucsf.edu/docs/ztdg0111 "According to SourceWatch the appeal was "a scam perpetrated by the asbestos and tobacco industries in support of the Global Climate Coalition".[4] Both industries had no direct reason to deny global warming, but rather wanted to promote their "sound science" agenda, which basically states that industry-funded science is good science and science contradicting those science (such as environmental science) is bad science or "junk science"." (Wikipedia)

# No Fact-checking but semantic charactristics
- Fact checking only works for short statments, currently. Not for full texts. Only support to dive deeper analysis .  (Wang 2023, Wadden et al. 2020)
- fact checking: truth depends on the evidence dataset; it's only truth-related-to-evidence-data; which is not up-to-date to research; is the evidence really trustable?  
- Truth is defined as the corpus knowledge used for evidence (Wang 2023)
- Fact-checking/claim verification is no disinformation detection, as this depends on the intentionality
- Problematic statements hidden behind a true core or only become false due to a faulty or missing context (Gensing 2020)
- "Kiner werden nicht geschlagen." - normative correct. descriptive false. 




# BERT problems with long texts
- maximum position embedding is 512 tokens in BERT; also when more tokens are set the memory consumption is "unaffordable because all the activations are stored for back-propagation during training" (Ding et al. 2020:2) 
- sliding window approach: 
  - disadvantages: lack of long-distance attention (Ding et al. 2020:2); special relevance of first and last sentence of text paragraph cannot be considerd by sliding window (Ding et al. 2020:6)
  - SLED approach: only for encoder-decoder models (e.g. BART) Maor Ivgi, Uri Shaham, Jonathan Berant; Efficient Long-Text Understanding with Short-Text Models. Transactions of the Association for Computational Linguistics 2023; 11 284–299. doi: https://doi.org/10.1162/tacl_a_00547 
  - RoBert: Raghavendra Pappagari, Piotr Żelasko, Jesús Villalba, Yishay Carmiel, Najim Dehak (2019): Hierarchical Transformers for Long Document Classification, https://doi.org/10.48550/arXiv.1910.10781

# evaluation of long text understanding
  - SROLLS: Aurko Roy, Mohammad Saffar, Ashish Vaswani, David Grangier; Efficient Content-Based Sparse Attention with Routing Transformers. Transactions of the Association for Computational Linguistics 2021; 9 53–68. doi: https://doi.org/10.1162/tacl_a_00353

# first results on small first data set 927items < July 2023 documentend in EAHIL presentation

# current categorisation
new: 1) scientific (specialized?) 2) non-scientific 
              2a) popular science, 
              2b) disinformation,
              2c) homeopathy and antroposophic medicine (questonable?) 

# other data sets
 - overview on used possible data sources for data sets on health emergencies: Twitter, search terms, newspaper, CDC official guidlines, fact checked news articles, Wikipedia, You Tube (Ankit Aich and Natalie Parde. 2022. Telling a Lie: Analyzing the Language of Information and Misinformation during Global Health Events. In Proceedings of the Thirteenth Language Resources and Evaluation Conference, pages 4135–4141, Marseille, France. European Language Resources Association.)
- Kinsora et al. 2017: dataset on medical misinformation in health forums (A. Kinsora, K. Barron, Q. Mei and V. G. V. Vydiswaran, "Creating a Labeled Dataset for Medical Misinformation in Health Forums," 2017 IEEE International Conference on Healthcare Informatics (ICHI), Park City, UT, USA, 2017, pp. 456-461, doi: 10.1109/ICHI.2017.93.)
  - 4,7 mio comments and responses user generated texts 
  - verified as "misinformation" and "non-misinformation" by Snopes.com and MedlinePlus, CDC websites, mayoclinic.com 
- Aich/Parde 2022: global health events from 1917
  - news paper texts and social media
- Ambesh Shekhar 2020: Covid19-misinformation data. Misleading Facts about Covid19, Kaggle, https://www.kaggle.com/datasets/ambityga/covid19misinformation
- Health and Well Beeing (HWB) (https://dcs.uoc.ac.in/cida/resources/hwb.html)  -> requested again at 2023-09-08
- PubHealth: (https://github.com/neemakot/Health-Fact-Checking) dataset of 11 800 statements from Reuters News, Asssociated Press, Health News Review, and fact checker websites (including Politifact, FactCheck, FullFact) for the field of public health, which they evaluate using natural language processing (NLP) models pre-trained on biomedical topics. They calculate the coherence between statements in order to infer the correctness or incorrectness of a statement.   
- standard fake news data sets but on political topics: LIAR, BuzzFeed, ISOT, etc. 

# Data Sets 
## Data Set, third approach: topic wise
| topic       | scientific | popular_scientific                                 | alternative_scientific                                       | disinformativ                                  | smalest amount*4 |
|-------------|--------|----------------------------------------------------|--------------------------------------------------------------|------------------------------------------------|------------------|
| cumin       | **2** PMC | 4 WebMD, 0 HHP, 2 MH, 0 WH, 0 MPM        **[6]**   | 15 JEBIM, 30 CMT,  0 HomeoJour, 0 Goethe, 0 IJRH   [45]      | 4 NN,  10 HIN, 1 MCL, 0 H.N, 0 IW  [15]        | 2                |
| dementia    | 1166 PMC | 122 WebMD, 22 HHP, 5 MH, 6 WH, 19 MPM              | 33 JEBIM, 172 CMT, 12 HomeoJour, 1 Goethe, 2 IJRH            | 8 NN,  49 HIN, 18 MCL, 5 H.N, 1 IW  **[81]**   | 81               |
| heart attack | 902 PMC | 84 WebMD, 6 HHP, 12 MH, 10 WH, 9 MPM               | 45 JEBIM, 45 CMT, 3 HomeoJour, 0 Goethe, 0 IJRH              | 18 NN, 22 HIN, 19 MCL, 2 H.N, 0 IW    **[61]** | 61               |
| insomnia    | 130 PMC | 132 WebMD, 11 HHP, 0 MH, 6 WH, 5 MPM               | 40 JEBIM,84 CMT, 16 HomeoJour, 3 Goethe, 0 IJRH              | 32 NN, - HIN, 9 MCL, 0 H.N, 0 IW     **[41]**  | 41               |
| menopause   | 388 PMC | 129 WebMD, 9 HHP, 0 MH, 5 WH, 4 MPM                | 12 JEBIM,42 CMT, 25 HomeoJour, 2 Goethe, 2 IJRH              | 10 NN,  21 HIN, 5 MCL, 2 H.N, 1 IW    **[38]** | 38               |
| stroke      | 1162 PMC | 117 WebMD, 1 HHP, 6 MH, 3 WH, 22 MPM               | 46 JEBIM,40 CMT, 28 HomeoJour, 0 Goethe,  4 IJRH  **[118]**  | 130 NN,  23 HIN, 18 MCL, 5 H.N, 1 IW           | 118              |
| tobacco     | 133 PMC | 0 WebMD, 1 HHP, 6 MH, 1 WH, 5 MPM      **[13]**    | 61 JEBIM, 25 CMT, 19 HomeoJour, 1 Goethe, 0 IJRH             | 24 NN, 3 HIN, 4 MCL, 1 H.N, 0 IW               | 13               |
| turmeric    | **28** PMC | 31 WebMD, 3 HHP, 10 MH, 5 WH, 0 MPM  **[49]**      | 11 JEBIM,  121 CMT, 1 HomeoJour, 0 Goethe, 1 IJRH  [134]     | 71 NN, 2 HIN, 7 MCL, 6 H.N, 0 IW  [86]         | 28               |           
| measles     | 139 PMC | 34 WebMD, 5 HHP, 3 MH, 1 WH, 14 MPM                | 8 JEBIM, 6 CMT, 8 HomeoJour, 2 Goethe, 1 IJRH   **[25]**     | 16 NN, 63 HIN, 3 MCL, - H.N., 0 IW             | 25               |
| inflammation | 2582 PMC | 32 WebMD, 21 HHP, 37 MH, 19 WH, 13 MPM       [122] | 31 JEBIM, 364 CMT, 122 HomeoJour, 5 Goehte, 11 IJRH          | 8 NN,  21 HIN, 53 MCL, - H.N., 1 IW   **[83]** | 83               |
| vaccination | 2907 PMC | 18 WebMD, 53 HHP,50 MH, 42 WH, 29 MPM              | 17 JEBIM, 15 CMT, 13 HomeoJour,  2 Goethe, 4 IJRH **[51]**   | 46 NN, 94 HIN, 37 MCL,  - H.N., 10 IW          | 51               |
| transgender | 121 PMC | 21 WebMD, 10 HHP, 35 MH, 19 WH, 0 MPM              | 1 JEBIM,  - CMT, 0 HomeoJour, 0 Goethe, 0 IJRH      **[1]**  | 72 NN, 10 HIN, 1 MCL, - H.N., 5 IW             | 1                |
| abortion    | 215 PMC | 18 WebMD, 3 HHP, 9 MH, 37 WH, 0 WPM                | 12 JEBIM, 13 CMT,  15 HomeoJour, 1 Goethe, 0 IJRH   **[41]** | 48 NN, 29 HIN, 1MCL, - H.N., 2 IW              | 41               |
| sum         | 2058 PMC | 742 WebMD, 145 HHP, 175 MH, 155 WH, 120 MPM        | 334 JEBIM,  958 CMT, 262 HomeoJour, 18 Goethe, IJRH          | 560 NN, 347 HIN, 175 MCL, 21 H.N, 26 IW        | 664              |
| complete    | 2058   | 1337                                               | 1574                                                         | 1129                                           | 2656             |



-scientific
  - PMC = PubMed Central (10% most cited-by)  
    - Cuminum [B01.875.800.575.912.250.075.233]
    - Dementia [C10.228.140.380, F03.615.400] 
    - Myocardial Infarction [C14.280.647.500, C14.907.585.500, C23.550.513.355.750, C23.550.717.489.750]
    - Sleep Initiation and Maintenance Disorders [C10.886.425.800.800, F03.870.400.800.800]
    - Menopause [G08.686.157.500, G08.686.841.249.500]
    - Stroke [C10.228.140.300.775, C14.907.253.855]
    - Tobacco Use [F01.145.958] / Tobacco Smoking [F01.145.805.375,  F01.145.958.875]
    - Curcuma [B01.875.800.575.912.250.618.937.900.166]
    - Measles [C01.925.782.580.600.500.500]
    - Inflammation [C23.550.470]
    - Vaccines [D20.215.894]
    - Transgender Persons [M01.270.988.750]
    - Abortion, Induced [E04.520.050]
- popular_scientific
  - WebMD: Web MD https://www.webmd.com/
  - HHP =  Harvard Health Publishing - Harvard Medical School: https://www.health.harvard.edu/ 
  - MH = Men's Health: https://www.menshealth.com
  - WH = Women's Health: https://www.womenshealthmag.com
    - cleaning "Related Story"?
  - MPM = Medline Plus Magazin:  https://magazine.medlineplus.gov
    - CDC = 

- alternative scientific
  - JEBIM = Journal of evidence based integrative medicine
  - CMT = BMC Complementary Medicine and Therapies
    - texts complete?
  - HomeoJour = Homeopathic Journal: https://www.homoeopathicjournal.com/archives
  - Goethe = School of Spiritual Science Medical Section at the Goetheanum https://medsektion-goetheanum.org/en/research/publications/journal-contributions-on-research-in-anthroposophic-medicine-2017-2019
  - IJRH = Indian Journal of Research in Homeopathy: https://www.ijrh.org/
- 
- disinformatation
  - NN = Natural News
  - HIN = Health Impact News
  - MCL = Mercola's Censored Library (harvesting continues)
  - H.N = Health.News (harvesting continues)
  - IW = https://www.infowars.com/category/4/  category 4 "health"


- not harvested yet:  
  - popular: https://www.prevention.com/  
  - popular: https://www.health.com/
  - popular: CDC
  - popular: mayo clinic
  - popular: wikipedia
  - unclear: https://healthnews.com
  - disinfo: breitbart
  - - 
  
- deleted:
  - alternative_sciecne: AM = Anthropmed.org: https://www.anthromed.org/
 

## Data set, first and second approach 
- categories: scientific, popular science, disinformation, homeopathy/anthroposophic-medicine 
- retrieval modi: <span style="color:purple"> Python library retrieval </span> <span style="color:lightblue">HTML webscraping</span>, <span style="color:blue">PDF webscraping</span> , <span style="color:green">reuse of dataset</span>, <span style="color:red"> crowdsourcing </span>  
- public call for crowdsourcing on website (e.g. Maor Ivgi, Uri Shaham, Jonathan Berant; Efficient Long-Text Understanding with Short-Text Models. Transactions of the Association for Computational Linguistics 2023; 11 284–299. doi: https://doi.org/10.1162/tacl_a_00547)
- there need to be a ratio - not only about categories - but also on topics from categories. therefor we will add tags to each item, to ensure balance regarding topics 
- linguistic analysis: Aich/Parde 2022 show a differences in texts belonging to their data set class "misiformation" and "accurate information". accurate information labled text are more 1) complex (91%) compared to 38% in misinfo-class. 2) misinfo class has a higher presence of personal pronouns (Aich/Pardo 2022) 
-  "signs of the times" is a christian Seventh-day Adventist magazin. - a christian view is not necessary disisnformative...    

- scientific: 
  - <span style="color:green">451 + 312+ 4616 PubMed Central von PDFs: https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/ </span>; we assume all journnlas are peer reviewed therefore, scientifc
- 
- non-scientific: 
  - popular science: 
    - <span style="color:purple">Wikipedia: 1365 </span>
    - <span style="color:lightblue">MedlinePlus: 1.200 https://medlineplus.gov/healthtopics.html </span>
    - Centers for deseaese Control and Prevention https://www.cdc.gov/index.htm
    - World Health organization
    - Aich/Parde 2022 dataset dataset requested per email Aug-28-2023
    - Mayo Clinic: mayoclinic.org 
   
  - disinformation including misinformation: 
    - <span style="color:lightblue">99 items: healthnews.com </span>
    - <span style="color:lightblue">78  items: healthimpactnews.com </span>
    - <span style="color:lightblue">10 items: cevo.mykajabi.com </span>
    - <span style="color:lightblue">17 items: Mercola's Censored Library </span>
    - <span style="color:lightblue">58 items: Breitbart: on Transgender </span>
    - <span style="color:green">7553 items: Covid-misinformation data </span> set retrieved from Poynter.org: https://www.kaggle.com/datasets/ambityga/covid19misinformation
    - chemtrails? -> email for advise to poynter.org -> reply, they do not know about an according data set (email by  Enock Nyariki <enyariki@poynter.org>
Do 24.08.2023 23:14)  - Aich/Parde 2022 dataset requested per email Aug-28-2023
    - National Research Council. 1983. Changing Climate: Report of the Carbon Dioxide Assessment Committee. Washington, DC: The National Academies Press. https://doi.org/10.17226/18714.:  harsh critic and qotes at Oreskes/Conway page 2012, 181/12
    - “What the Experts Say About Global Climate Change” (1993), https://www.climatefiles.com/denial-groups/global-climate-coalition-collection/1993-selected-climate-change-quotes/
    - Documents of Global Climate Coalition (GCC): https://climateinvestigations.org/global-climate-coalition-documents-index/
    - APCO ASSOCIATES. JUNK SCIENCE AT THE EPA. 1993 May 12. Philip Morris Records; Master Settlement Agreement. Unknown. https://www.industrydocuments.ucsf.edu/docs/gmfj0130 (Oreskes/Conway 143-144), OCR file
    - Unknown. BAD SCIENCE A RESOURCE BOOK. 1993 March 26. Philip Morris Records; Master Settlement Agreement. Unknown. https://www.industrydocuments.ucsf.edu/docs/gmdj0065 (Oreskes/Conway 144), OCR file  
  - 
  - alternative/integrative science
    - Homeopathy
      - Indian Journal of Research in Homoeopathy https://www.ijrh.org/journal/ ; 
    - Antroposophy
      - AnthroMed Library https://www.anthromed.org/
      - 913 items International Journal of Homeopathic Sciences 
      - Physicians' Association for Antroposophic Medicine (PAAM, https://anthroposophicmedicine.org/)
      - literature lists 2017-2020: Anthroposophic Medicine School of Spiritual Science Medical Section at the Goetheanum (https://medsektion-goetheanum.org/en/research/publications/journal-contributions-on-research-in-anthroposophic-medicine-2017-2019)
      - Complementary Medicine Research, ISSN: 2504-2092 (Print), e-ISSN: 2504-2106 (Online), DOI: 10.1159/issn.2504-2092; 
      Vol. 1-6 (1994-1999) were published under the journal's former title Forschende Komplementärmedizin / Research in Complementary Medicine and Vol. 7-12 (2000-2005) as Forschende Komplementärmedizin und Klassische Naturheilkunde / Research in Complementary and Classical Natural Medicine. 
      - Integrative Cancer Therapies (ICT) https://journals.sagepub.com/home/ICT
      - https://journals.sagepub.com/toc/ICT/current

      
  
 

# structure of dataset. 


# why and how disinformation works
- you cannot determine if a single event (cancer, catastrophe,  forestfire, flood) was caused by smoking or global warming. these events just increase the  probability  (Oreskes/conway: 31, 34, )
- media wants to provide a "balanced view" (oreskes/conway: 17,19, 215)
    - "balance was interpreted, it seems, as giving equal weight to both sides, rather than giving 'accurate' weight to both sides." (oreskes/conway 19)
    - while global warming was scientifically established in 1997. the media still wanted to give a balanced view. the kyoto protocol ws refused by the senat "scientifically, global warming was an established fact. Politicaly, global warming was dead" (oreskey/conway: 215)
- due to six factors: 1) democratization of content creation, 2) rapid news cycle and economic incentives, 3) wide and immediate reach and interactivity, 4) organic and intentionally created filter bibbles, 5) algorithmic curation and lack of transparanciy, and 6) scale and anonymity in online accounts (AKERS, J. et al. Technology-Enabled Disinformation: Summary, Lessons, and Recommendations. arXiv.org, [S. l.], v. 1, 2019. Available at:https://arxiv.org/abs/1812.09383. Access onMay 28,2020. (cited from Santos-d’amorim/miranda 2021)) 