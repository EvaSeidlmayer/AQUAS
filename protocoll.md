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
| topic          | scientific | popular_scientific                                        | alternative_scientific                                           | disinformativ                                        | smalest amount*4 |
|----------------|--------|-----------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------|---------------|
| cumin          | **2** PMC | 4 WebMD, 0 HHP, 2 MH, 0 WH, 0 MPM, 1 Mayo        **[7]**  | 15 JEBIM, 30 CMT,  0 HomeoJour, 0 Goethe, 0 IJRH   [45]          | 4 NN,  10 HIN, 1 MCL, 0 H.N, 0 IW  [15]              | 2           |
| dementia       | 1166 PMC | 122 WebMD, 22 HHP, 5 MH, 6 WH, 19 MPM                     | 33 JEBIM, 172 CMT, 12 HomeoJour, 1 Goethe, 5 IJRH       [223]    | 8 NN,  49 HIN, 23 MCL, 5 H.N, 1 IW  **[86]**  <-     | [86]          |
| heart attack   | 902 PMC | 84 WebMD, 6 HHP, 12 MH, 10 WH, 9 MPM                      | 45 JEBIM, 45 CMT, 3 HomeoJour, 0 Goethe, 0 IJRH         [93]     | 18 NN, 22 HIN, 30 MCL, 2 H.N, 0 IW    **[72]** <-    | [72]          |
| insomnia       | 130 PMC | 132 WebMD, 11 HHP, 0 MH, 6 WH, 5 MPM                      | 40 JEBIM,84 CMT, 16 HomeoJour, 3 Goethe, 7 IJRH           [152]  | 32 NN, - HIN, 11 MCL, 0 H.N, 0 IW     **[43]**  <-   | [43]          |
| menopause      | 388 PMC | 129 WebMD, 9 HHP, 0 MH, 5 WH, 4 MPM                       | 12 JEBIM,42 CMT, 25 HomeoJour, 2 Goethe, 6 IJRH           [87]   | 10 NN,  21 HIN, 6 MCL, 2 H.N, 1 IW    **[40]**  <-   | [40]          |
| stroke         | 1162 PMC | 117 WebMD, 1 HHP, 6 MH, 3 WH, 22 MPM                      | 46 JEBIM,40 CMT, 28 HomeoJour, 0 Goethe,  12 IJRH  **[126]**  <- | 130 NN,  23 HIN, 32 MCL, 5 H.N, 1 IW     [191]       | [126]         |
| tobacco        | 133 PMC | 0 WebMD, 1 HHP, 6 MH, 1 WH, 5 MPM, 8 Mayo      **[21]**   <- | 61 JEBIM, 25 CMT, 19 HomeoJour, 1 Goethe, 6 IJRH         [112]   | 24 NN, 3 HIN, 6 MCL, 1 H.N, 0 IW              [34]   | [21] <-       |
| turmeric       | **28** PMC | 31 WebMD, 3 HHP, 10 MH, 5 WH, 0 MPM, 4 Mayo  **[53]** <-  | 11 JEBIM,  121 CMT, 1 HomeoJour, 0 Goethe, 2 IJRH  [135]         | 71 NN, 2 HIN, 11 MCL, 6 H.N, 0 IW  [90]              | [53] <-       |           
| measles        | 139 PMC | 34 WebMD, 5 HHP, 3 MH, 1 WH, 14 MPM                       | 8 JEBIM, 6 CMT, 8 HomeoJour, 2 Goethe, 1 IJRH   **[25]**         | 16 NN, 63 HIN, 5 MCL, - H.N., 0 IW          [84]     | 25            |
| inflammation   | 2582 PMC | 32 WebMD, 21 HHP, 37 MH, 19 WH, 13 MPM       [122]        | 31 JEBIM, 364 CMT, 122 HomeoJour, 5 Goehte, 11 IJRH       [533]  | 8 NN,  21 HIN, 87 MCL, - H.N., 1 IW   **[117]**  <-- | [117]         |
| vaccination    | 2907 PMC | 18 WebMD, 53 HHP,50 MH, 42 WH, 29 MPM                     | 17 JEBIM, 15 CMT, 13 HomeoJour,  2 Goethe, 14 IJRH **[61]** <-   | 46 NN, 94 HIN, 45 MCL,  - H.N., 10 IW     [195]      | 61            |
| transgender    | 121 PMC | 21 WebMD, 10 HHP, 35 MH, 19 WH, 0 MPM                     | 1 JEBIM,  - CMT, 0 HomeoJour, 0 Goethe, 0 IJRH      **[1]**      | 72 NN, 10 HIN, 1 MCL, - H.N., 5 IW          [88]     | 1             |
| abortion       | 215 PMC | 18 WebMD, 3 HHP, 9 MH, 37 WH, 0 WPM                       | 12 JEBIM, 13 CMT,  15 HomeoJour, 1 Goethe, 3 IJRH   **[44]** <-  | 48 NN, 29 HIN, 1 MCL, - H.N., 2 IW         [80]      | 44            |
| climate change ||                                                           |                                                                  |                                                      |
| pandemic       ||                                                           |                                                                  |                                                      |
| adrenochrome   ||                                                           |                                                                  |                                                      |
| urotherapy     ||                                                           |                                                                  |                                                      |
| chakra         ||                                                           |                                                                  |                                                      |
| sum            | 2058 PMC | 742 WebMD, 145 HHP, 175 MH, 155 WH, 120 MPM               | 334 JEBIM,  958 CMT, 262 HomeoJour, 18 Goethe, IJRH              | 560 NN, 347 HIN, 175 MCL, 21 H.N, 26 IW              | 664           |
| complete       | 2058   | 1337                                                      | 1574                                                             | 1129                                                 | 2656          |



-scientific
  - PMC = PubMed Central (10% most cited-by)
    - via XML
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
    - HTML/beautifulsoup
  - HHP =  Harvard Health Publishing - Harvard Medical School: https://www.health.harvard.edu/ 
    - HTML/beautifulsoup
  - MH = Men's Health: https://www.menshealth.com
    - HTML/beautifulsoup
  - WH = Women's Health: https://www.womenshealthmag.com
    - HTML/beautifulsoup
    - cleaning "Related Story"? 
  - MPM = Medline Plus Magazin:  https://magazine.medlineplus.gov
    - HTML/beautifulsoup
  - Mayo = Mayo Clinic https://www.mayoclinic.org/
    - only checkted for: cumin, tobacco, turmeric
    - manually from websites 
  - CDC = 

- alternative scientific
  - JEBIM = Journal of evidence based integrative medicine
    - PDF/PyPDF2 all pages
  - CMT = BMC Complementary Medicine and Therapies
    - PDF/PyPDF2 all pages
  - HomeoJour = Homeopathic Journal: https://www.homoeopathicjournal.com/archives
    - PDF/pdftotext all pages
  - Goethe = School of Spiritual Science Medical Section at the Goetheanum https://medsektion-goetheanum.org/en/research/publications/journal-contributions-on-research-in-anthroposophic-medicine-2017-2019
    - PDF/pdftotext all pages
  - IJRH = Indian Journal of Research in Homeopathy: https://www.ijrh.org/
    - PDF/pypdf.PDFReader
- 
- disinformation
  - NN = Natural News
    - HTML/beautiful soup
  - HIN = Health Impact News
    - HTML/beautiful soup
  - MCL = Mercola's Censored Library (harvesting continues)
    - HTML/beautiful soup
  - H.N = Health.News (harvesting continues)
    - HTML/beautiful soup
  - IW = https://www.infowars.com/category/4/  category 4 "health"
    - HTML/beautiful soup


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


# cleaning of FSoLS-24-v4
- category "alternative" - not just find&replace by "alterative_science" - this will change the word in the text as well!
- no cleaning of "infowars" in the text since it is used as a reference there. 
- British Medical Journal: Cleaning of    "Br Med J Clin Res Ed      British Medical Journal Clinical research ed.      02670623      6805607      1498437          Letter        Measles eradication policies.        22        5        1982      284      6328      1559      1560"
but not when it is referneced in the text (e.g. "A two and a halfyear study conducted by Kripkel Langer and Kline called Hypnotics sleeping pills association with mortality or cancer a matched cohort study was published by the British Medical Journal BMJ in February 2012.")
- "BMJ Open" was deleted
- BMJ: deleted as simple literature fragments or literature citation, such as "  BMJ Case Rep      BMJ Case Rep      bmjcr      bmjcasereports        BMJ Case Reports      1757790X        BMJ Publishing Group        BMA House Tavistock Square London WC1H 9JR      33622754      7907863      bcr2020240536      10.1136bcr2020240536          Case Report          2474          1330          508          232          200          220        Acute confusional state as a prognostic sign of COVID19 largevessel occlusion LVO          httporcid.org0000000152399533            Deliwala            Smit Sunil            Hussain            Murtaza            Ponnapalli            Anoosha            Awuah            Dominic            Dawood            Thair          httporcid.org0000000167634508            Bachuwa            Ghassan      Internal Medicine Hurley Medical Center Flint Michigan USA        Correspondence to Dr Ghassan Bachuwa gbachuw2hurleymc.com        2021        23        2        2021        23        2        2021      14      2      e240536          05          2          2021         BMJ Publishing Group Limited 2021. No commercial reuse. See rights and permissions. Published by BMJ.        2021          This article is made freely available for use in accordance with BMJs website terms and conditions for the duration of the covid19 pandemic or until otherwise determined by BMJ. You may use download and print the article for any lawful noncommercial purpose including text and data mining provided that all copyright notices and trade marks are retained.          httpsbmj.comcoronavirususage  ";
  - also deleted from DOI: "10.1136bmjgh2021007211 " -> "10.1136gh2021007211 "
- BMJ was not deleted when it is a part of a sentence: e.g. "A 2021 BMJ Open meta-analysis suggested that drinking several cups of coffee a day was linked to a lower risk of developing prostate cancer. The study found that each additional cup of coffee a day reduced relative risk by 1 percent."
-  ".com" alle webseiten rausnehmen??
- "naturalnews":
  - deleted between author statement and articel, e.g.; "High protein intake puts extreme dieters at risk for heart attack and stroke by Raw Michelle NaturalNews A study from Sweden recently found concerning health implications for individuals"
  - not, when it is part of" a sentence, e.g.: "Today NaturalNews publishes The Great HPV Vaccine Hoax Exposed a special report that cites from numerous FDA documents and clinical studies to show that HPV vaccines are not only ineffective they may actually be dangerous As revealed in the special report the Gardasil vaccine has been linked to a 44.6 increase in precancerous lesions in some women raising serious doubts over the sensibility of mandatory vaccination policies.", or "A NaturalNews investigation has revealed that the FDA knew as early as 2003 that Human Papilloma Virus HPV was not linked to cervical cancer." 
  -  "naturalnews.com printable article" deleted
- "Harvard Medical School" complete Website derivat removed 
  - "Recent Blog Articles                     Free Healthbeat Signup  Get the latest in health news delivered to your inbox!                Sign Up                   Footer        Facebook    Twitter    Linkedin    YouTube        My Account    Customer Service      Log in       Order Now    Online Learning Courses      Digital Subscriptions      Special Health Reports      Print Subscriptions       More    About Us      Permissions      Content Licensing      Topics      Trademark Notice                               © 2024 ® of The President and Fellows of Harvard College                  Do not sell my personal information | Privacy Policy and Terms of Use      Scroll To Top           Close    Thanks for visiting. Don't miss your FREE gift. The Best Diets for Cognitive Fitness, is yours absolutely FREE when you sign up to receive Health Alerts from Harvard Medical School Sign up to get tips for living a healthy lifestyle, with ways to  fight inflammation and improve cognitive health, plus the latest advances in preventative medicine, diet and exercise, pain relief, blood pressure and cholesterol management, and more.           I want to get healthier                   This site is protected by reCAPTCHA and the Google         Privacy Policy and         Terms of Service apply.               Close   Health Alerts from Harvard Medical School Get helpful tips and guidance for everything from fighting inflammation to finding the best diets for weight loss...from exercises to build a stronger core to advice on treating cataracts. PLUS, the latest news on medical advances and breakthroughs from Harvard Medical School experts.   BONUS! Sign up now and get a FREE copy of theBest Diets for Cognitive Fitness             I want to get healthier                   This site is protected by reCAPTCHA and the Google         Privacy Policy and         Terms of Service apply.                Close      Stay on top of latest health news from Harvard Medical School. Plus, get a FREE copy of the Best Diets for Cognitive Fitness.            Sign me up                   This site is protected by reCAPTCHA and the Google         Privacy" 
  - "Share This Page  Share this page to Facebook    Share this page to Twitter    Share this page via Email     Print This Page  Click to Print  "
- "infowars" 
  - deleted when it is website derivate, eg.: "Increase in Deaths Following Covid Vaccination — Study  News1,236% Increase in Deaths Following Covid Vaccination — StudySean Miller | InfowarsMay 28th 2024, 8:12 am When the county's death data is applied nationwide, researchers estimate"
- " This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts'" -deleted
- "inkFacebookEmailNoteOtherShareCommentsTopNewCommunityNo"
- Open access license " licensesby4.0."/"Creative Commons":
  - "This is an open access article under the terms of the    licensesbyncnd4.0 License which permits use and distribution in any medium provided the original work is properly cited the use is noncommercial and no modifications or adaptations are made.", "licensesby4.0 Open Access This article is licensed under a Creative Commons Attribution 4.0 International License which permits use sharing adaptation distribution and reproduction in any medium or format as long as you give appropriate credit to the original authors and the source provide a link to the Creative Commons licence and indicate if changes were made.", "licensesby4.0 Open Access This article is licensed under a Creative Commons Attribution 4.0 International License which permits use sharing adaptation distribution and reproduction in any medium or format as long as you give appropriate credit to the original authors and the source provide a link to the Creative Commons license and indicate if changes were made. The images or other third party material in this article are included in the articles Creative Commons license unless indicated otherwise in a credit line to the material. If material is not included in the articles Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use you will need to obtain permission directly from the copyright holder. To view a copy of this license visit    licensesby4.0.", "licensesby4.0 Licensee MDPI Basel Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution CC BY license  licensesby4.0."
  - - "  The images or other third party material in this article are included in the articles Creative Commons licence unless indicated otherwise in a credit line to the material. If material is not included in the articles Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use you will need to obtain permission directly from the copyright holder. To view a copy of this licence visit    licensesby4.0. The Creative Commons Public Domain Dedication waiver    publicdomainzero1.0 applies to the data made available in this article unless otherwise stated in a credit line to the data.", "licensesby4.0 Open AccessThis article is licensed under a Creative Commons Attribution 4.0 International License which permits use sharing adaptation distribution and reproduction in any medium or format as long as you give appropriate credit to the original authors and the source provide a link to the Creative Commons licence and indicate if changes were made. The images or other third party material in this article are included in the articles Creative Commons licence unless indicated otherwise in a credit line to the material. If material is not included in the articles Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use you will need to obtain permission directly from the copyright holder. To view a copy of this licence visit    licensesby4.0. The Creative Commons Public Domain Dedication waiver    publicdomainzero1.0 applies to the data made available in this article unless otherwise stated in a credit line to the data."
  - "This is an open access article under the terms of the    licensesby4.0 License which permits use distribution and reproduction in any medium provided the original work is properly cited."
  - "This is an Open Access article distributed under the terms of the Creative Commons Attribution License    licenses by 2.0   which permits unrestricted use  distribution  and reproduction in any medium  provided the original work is properly cited.", "This is an open access journal, and articles are distributed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License, which allows others to remix, tweak, and build upon the work non-commercially, as long as appropriate credit is given and the new creations are licensed under the identical terms."
  - " Open Access This article is licensed under a Creative Commons Attribution 4.0 International License  which permits use  sharing  adaptation  distribution and reproduction in any medium or format  as long as you give appropriate credit to the original author s  and the source  provide a link to the Creative Commons licence  and indicate if changes were made. The images or other third party material in this article are included in the article s Creative Commons licence  unless indicated otherwise in a credit line to the material. If material is not included in the article s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use  you will need to obtain permission directly from the copyright holder. To view a copy of this licence  visit   licenses by 4.0  . The Creative Commons Public Domain Dedication waiver  publicdomain zero 1.0    applies to the data made available in this article  unless otherwise stated in a credit line to the data. "
- "Continued from previous page"
- website:
  - "httpscreativecommons.org" deleted
  - "httpsorcid.org" delted
  - "httpdx.doi.org" deleted
  - other .org domain such as httpwww.cancer.org, tobaccoatlas.org, anhusa.org, chiropractic.org, facit.org .... deleted
  - "httpwww.beatingcancergently.com", naturalnews.com, face.com, time.com, ageofautism.com, httpwww.sciencedirect.com
  - .com - deleted
  - .gov deleted
  - .ca deleted
  - www.biomedcentral.com deleted
  - doi.org
  - html: harryimosflmver721downloads.html, nistjaroffarticle09565106953800.html, scenarios.html, lebengesundheitsfoerderungundpraeventionimpfungenprophylaxeschweizerischerimpfplan.html, virusquestionsandanswers.html,  acupuncture.html
  - "Save Article" deleted
- PDF
  - "___tion" -> connected "tion"
  - "__tive" -> connected "tive"
  - "__ ammatory" -> "inflammatory" etc
  - "__ing" ->"aginging"
  - "__ment" "treatment"
  - "__ity"
  - "sig__" -> "signiture"
  - "acupunc___ture" -> "acupuncture "
  - "Experi__ments" -> "Experiments"
  - "clin__ical" -> "clinical"
  - "pharmaceuti_cal" -> "pharmaceutical"
  - "sig_nificant" -> "significant"
  - "you\" -> "you", "it\" -> "it" -> "dont't", "Alzheimer\'s" -> "Alzheimer's" -> "body\'s" -> "body's"
- deleted "NEXT ARTICLE >>Disclaimer: The entire contents of this website are based upon the opinions of Dr. Mercola, unless otherwise noted. Individual articles are based upon the opinions of the respective author, who retains copyright as marked.The information on this website is not intended to replace a one-on-one relationship with a qualified health care professional and is not intended as medical advice. It is intended as a sharing of knowledge and information from the research and experience of Dr. Mercola and his community. Dr. Mercola encourages you to make your own health care decisions based upon your research and in partnership with a qualified health care professional. The subscription fee being requested is for access to the articles and information posted on this site, and is not being paid for any individual medical advice.If you are pregnant, nursing, taking medication, or have a medical condition, consult your health care professional before using products based on this content."
- deleted "Disclaimer: The entire contents of this website are based upon the opinions of Dr. Mercola, unless otherwise noted. Individual articles are based upon the opinions of the respective author, who retains copyright as marked.The information on this website is not intended to replace a one-on-one relationship with a qualified health care professional and is not intended as medical advice. It is intended as a sharing of knowledge and information from the research and experience of Dr. Mercola and his community. Dr. Mercola encourages you to make your own health care decisions based upon your research and in partnership with a qualified health care professional. The subscription fee being requested is for access to the articles and information posted on this site, and is not being paid for any individual medical advice.If you are pregnant, nursing, taking medication, or have a medical condition, consult your health care professional before using products based on this content."
- deleted:  "Copy linkFacebookEmailNotesOtherDiscover", "Copy linkFacebookEmailNotesOtherDiscover", "Copy linkFacebookEmailNotesOther", "Copy linkFacebookEmailNoteOtherDiscover", "Copy linkFacebookEmailNoteOtherShare", "Copy linkFacebookEmailNoteOther"
- delteted: "Copy linkFacebookEmailNotesOtherShareCommentsTopNewCommunityNo postsReady for more?Subscribe© 2023 Privacy ∙ Terms ∙ Collection notice Start WritingGet the appSubstack is the home for great writingOur use of cookies\n  We use necessary cookies to make our site work. We also set performance and functionality cookies that help us make\n  improvements by measuring traffic on our site. For more detailed information about the cookies we use, please see our\n  privacy policy.\n  ✖  ""]""
- deleted everything after "Sources  Update History Share View privacy policy"    e.g. "Sources  Update History Share View privacy policy copyright and trust info Share View privacy policy copyright and trust info  Next Therapy Dogs for Cancer PatientsMore on CancerUnderstanding Cancer BasicsHow to Spot the Early Warning Signs of CancerMost Common Cancers and Their Symptoms Recommended FEATURED Top doctors in  Find more top doctors on Search Related LinksCancer HomeBladder CancerBrain CancerBreast CancerCervical CancerColorectal CancerLeukemia  LymphomaLung CancerMelanomaMultiple MyelomaOvarian CancerPancreatic CancerProstate CancerCancer NewsCancer ReferenceCancer SlideshowsCancer QuizzesCancer VideosFind an OncologistBook Take Control of Your Cancer RiskCancer AZMore Cancer TopicsPoliciesPrivacy PolicyCookie PolicyEditorial PolicyAdvertising PolicyCorrection PolicyTerms of UseAboutContact UsAbout WebMDCareersNewsletterCorporateWebMD Health ServicesSite MapAccessibilityOur AppsWebMD MobileWebMD AppPregnancyBabyAllergyFor AdvertisersAdvertise with UsAdvertising Policy  2005  2024 WebMD LLC an Internet Brands company. All rights reserved. WebMD does not provide medical advice diagnosis or treatment. See additional information."
- mercola "share this post" two times in texts of mercola. after second "share this post" text was removed
- deleted "Share This Story Choose Your Platform Join the DiscussionCancel reply"
- alt: deleted: "Publish with BioMed Central " and following text
- deleted "This is an Open Access article distributed under the terms of the Creative Commons Attribution License    licenses by 2.0   which permits unrestricted use  distribution  and reproduction in any medium  provided the original work is properly credited.", "This is an Open Access article distributed under the terms of the Creative Commons Attribution License   creativecommons. org licenses by 2.0    which permits unrestricted use  distribution  and reproduction in any medium  provided the orig inal work is properly cited.", "This is an Open Access article distributed under the terms of the Creative Commons Attribution License   creativecommons. org licenses by 2.0    which permits unrestricted use  distribution  and reproduction in any medium  provided the original work is properly cited.", "This is an Open Access article distributed under the terms of the Creative Commons Attribution License    licenses by 2.0   which permits unrestricted use  distribution  and reproduction in any medium  provided the original work is properly cited."
- "BMC Complementary and Alternative Medicine "
- "1472 6882" - ID of MNC Complementary and alternative medicine
- "SearchAbout My BookmarksMVP ExclusivesShopHealthFitnessWorkoutsWeight LossEntertainmentSex &amp; RelationshipsLifeTechnology &amp; GearStyleNutritionGroomingVideoNewsletterFollowPromotions Supply KitSubscribeOther EditionsPrivacy NoticeTerms Of UseSkip to ContentFitnessHealthGearStyleGroomingSubscribesign inGuide to TherapyBest Running ShortsBiohack Your SkinBest Food ScalesMuscle Building at 50Nutrition"
- "usepackageamssymb" and "usepackageamsfonts" deletd; "documentclass12ptminimalusepackageamsmathusepackagewasysym" left ->  math formula
- "enddocument" deleted
-  "Additional file" delted
- " Article reuse guidelines sagepub.comjournalspermissions" delted
- fragment of PDF reader
  - "Page (0-99) of (1-99)" deleted
  - "page number not for citation purposes" delted
- "issuecopyrightstatement" deleted
- "All Rights Reserved."
- "copyright"
- "NEXT ARTICLE >>Disclaimer: The entire contents of this website are based upon the opinions of Dr. Mercola, unless otherwise noted. Individual articles are based upon the opinions of the respective author, who retains copyright as marked.The information on this website is not intended to replace a one-on-one relationship with a qualified health care professional and is not intended as medical advice. It is intended as a sharing of knowledge and information from the research and experience of Dr. Mercola and his community. Dr. Mercola encourages you to make your own health care decisions based upon your research and in partnership with a qualified health care professional. The subscription fee being requested is for access to the articles and information posted on this site, and is not being paid for any individual medical advice. If  you are pregnant, nursing, taking medication, or have a medical condition, consult your health care professional before using products based on this content.
- "Read thefull article here."
- "share This Story Choose Your Platform Comments are closed"
- Harvard Medical School: " About the Authors    Toni Golen, MD, ......" deleted
- MedlinePlus: "Image credit Adobe Stock", "Image credit courtesy of David Goff   July 12 2018" -> deleted
- MedlinePlus: "What you need to know" deleted
- "Cite this article as " deleted
- "Access this article online Website:    Quick Respon Code:" deleted
- DOI
  - doi: 10.\d{4,9}/[-._;()-/:A-Z0-9]+
  - doi 10.\d{4,9}[-._;()/:A-Z0-9]+
  - doi 10.\d{4,9} \d{4,9}.\d{4,9}
  - doi 10.\d{4,9} [-._;()/:A-Z0-9]+ [-._;()/:A-Z0-9]+
  - doi 10.\d{4,9}  [-._;()/:A-Z0-9]+ [-._;()/:A-Z0-9]+ [-._;()/:A-Z0-9]+

# interpretation
- "usepackageamssymb" -> is used when special signs are used for mathemathical formula 

- disinfo
  - "ppis" : "proton pump inhibitors (PPIs)"
  - "rfr" : "radiofrequency radiation (RFR)"
  - "lupron" : "Puberty-blocking medications like Lupron"
  - "vaers" """Vaccine Adverse Events Reporting System (VAERS)"
  - "emf" : "electromagnetic field (EMF)"
  - democrats -> political opposition against US party of democrats
  - "near-infrared" -> ''
  - " nanoplastics" -> ''
  - "microplastics" -> ''
  - " plastics" -> ''
  - "e-cigarettes" -> ''
  -" all-cause" -> ''
  - cellphone > ''
  - "astaxanthin" -> ''
  - "doi" -> ''
  - "stress-related" -> ' '
  - " earns" -> ''
  - " ng/ml" -> ''
  - "Gerberding" -> "Julie Gerberding"
  - "Huff " -> "Ethan Huff "
  - " whistleblower" -> ''
  - " infanticide" -> ''
  - "ssaovap1" -> "SSAOVAP1 "
  - "ssao" -> SSAO
  - "pcv20" -> PCV20
  - "psci" -> "PSCI"
  - "iph" -> IPH
  - "advs" -> AdVs
  - "hcws" -> "HCWs"
  - "bmdm " -> BMDM
  - "igg22" -> "IgG22"
  - "rfr" -> "radiofrequency radiation (RFR) "
  - "tams" -> "Tumorassociated macrophages TAMs"
  - "dmcao" -> "Electrocoagulation of the left distal middle cerebral artery dMCA"
  - " gardasil " -> '' vaccination again human papiloma virus
  - "smallpox " -> '' vaccine
  - " armhand " -> ''
  - "headlines" -> ' ' no website atarvismus
  - "headline" -> ' ' actually, no, website derivate
  - -
  


- alt
  - "ovx" -> "OVX group"
  - "axSpA"
  - "axial spondyloarthritis (axSpA)"
  - "afib"
  - "homoeopathic" -> '' correct spelling!
  - "homeopathic" -> ''
  - "homoeopathy" -> ''
  - "fig" -> ''
  - "0.05" -> ''
  - "repertory" -> ''
  - "vol" -> ''
  - "anthroposophic" -> ''
  - 0.001
  - "nhp" -> "NHP"
  - "cal" -> ?
  - "dcm" -> 'DCM'
  - " mcao" -> MCAO
  - 'thj' -> "THJ"
  - "shr" -> "SHR"
  - "gv20" -> "GV20"
  - "psr" ->"PSR
  - "pm014" -> "PM014"
  - "mistletoe" -> ''
  - "dysmenorrhoea" -> ''
  - leucorrhoea -> ''
  - "acupoints" -> ''
  - "rafieiankopaei" -> "Mahmoud RafieianKopaei "
  - "hahnemann" -> "Dr Samuel Hahnemann "
  - " propolis " -> ''
  - "signicant" -> ''
  - "acad" -> abbr. in bibliography
  - "viscum" -> '' "viscum album"
  - " climaxis" -> ''
- 
- pop
  - "lewine" """Howard E. LeWine"
  -  "Salamon" -> "Maureen Salamon"
  - "Gadir" -> Azza Gadir
  - "Whyte" -> "John Whyte"
  - "fasciits" -> "Fasciitis nodularis" 
  - "Sjgrens" -> "Sjgrens syndrome"
  - "Shmerling" -> "Robert Shmerling" 
  - "Raniere" -> "Keith Raniere"
  - "Zeichner" -> "Joshua Zeichner"
  - "Restivo" -> "Jenette Restivo"
  - "Jenette" -> "Jenette Restivo"
  -  "golen" -> Toni Golen
  - "peloton" -> ''
  - "cosentyx" -> COSENTYX®
  - "pimple" -> ''
  - "ozempic" -> Ozempic
  - "plantar" -> ''
  - "colostrum" ->  ''
  - "m.d." -> "Doctor of Medicine"
  - "afib" -> "atrial fibrillation AFib "
  - "spondyloarthritis" -> "axial spondyloarthritis (axSpA)"
  - "axspa" -> "axial spondyloarthritis (axSpA)"
  - "nr-axspa" -> non-radiographic axial spondyloarthritis (nr-axSpA)
  - "fasciitis" -> ''
  - " freelance" -> ''
  - "lbd" -> "LBD"
  - "nightshades" -> ''
  - "hiphop" -> ''

- sci
  - "postcr" -> "postCR"
  - postuc -> postUC 
  - "postuc" -> "postUC"
  - "postac" -> "postAC"
  - "preuc" -> "preUC"
  - "preac" -> "preAC"
  - "HCWs"
  - "irf3" -> "IRF3"
  - "etal" -> et al.
  - "monthsprecr" """monthspreCR" 
  - "hdac3" -> "Hdac3"
  - "evs " -> "EVs "
  - "aldh2" -> "ALDH2"
  - "crao" -> "CRAO"
  - "ssaovap1" -> "SSAOVAP1"
  - "rtg4510" -> "rTg4510 Mice"
  - "fgf23" -> "FGF23"
  - "vte" -> "VTE"
  - "asu" -> "ASU"
  -  "a42" -> "A42"
  - "aldh2" -> "ALDH2"
  - " hdac3" -> "Hdac3" 
  - "hhf" -> "HHF"
  - "t2d" -> "T2D"
  - -"pni" -> "PNI"
  - "r62" -> "R62"
  - "suvr" -> "SUVR"
  - "stemi" -> "STEMI"
  - "timi" -> "TEMI"
  - "phaeocaulis" -> ''
  - "documentclass12ptminimalusepackageamsmathusepackagewasysym" -> math formula 
  - "monthsprecr" -> "monthspreCR"
  - "ntail" -> "NTAIL"
  - p0.001
  - 0.05
  - "fig" -> ''
  - "supplementary" -> ''
