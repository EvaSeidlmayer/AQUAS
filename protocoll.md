# deNBI VM
deNBI VM: scp -P 30327  -i ~/.ssh/id_rsa.pub  data/ready_dataset.csv ubuntu@129.70.51.6:/home/ubuntu
VM parameter: VM: 1; Flavour: de.NBI GPU medium
total core: 14
total RAM: 64GB
total GPUs: 1
Storage Limit 500 GB
Volume Counter 
Bert: https://github.com/huggingface/transformers/blob/v4.28.1/src/transformers/models/bert/modeling_bert.py#L1533

# Definition disinformation 
- "We define **misinformation** as the intentional or unintentional spread of inaccurate information, including through unchecked opinions. This differs from **disinformation**, where intent is a required factor." (https://www.dictionary.com/e/misinformation-vs-disinformation-get-informed-on-the-difference/)
- **Disinformation** is Intentionally spread false  information that follows an other purpose than truth. such as profit or a political or religious agenda. 


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


# data set
- categories: scientific, popular science, disinformation, homeopathy/anthroposophic-medicine 
- retrieval modi: <span style="color:purple"> Python library retrieval </span> <span style="color:lightblue">HTML webscraping</span>, <span style="color:blue">PDF webscraping</span> , <span style="color:green">reuse of dataset</span>, <span style="color:red"> crowdsourcing </span>  
- public call for crowdsourcing on website (e.g. Maor Ivgi, Uri Shaham, Jonathan Berant; Efficient Long-Text Understanding with Short-Text Models. Transactions of the Association for Computational Linguistics 2023; 11 284–299. doi: https://doi.org/10.1162/tacl_a_00547)
- there need to be a ratio - not only about categories - but also on topics from categories. therefor we will add tags to each item, to ensure balance regarding topics 
- linguistic analysis: Aich/Parde 2022 show a differences in texts belonging to their data set class "misiformation" and "accurate information". accurate information labled text are more 1) complex (91%) compared to 38% in misinfo-class. 2) misinfo class has a higher presence of personal pronouns (Aich/Pardo 2022) 

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
   
  - disinformation including disinformation: 
    - <span style="color:lightblue">99 items: health.news </span>
    - <span style="color:lightblue">78  items: healthimpactnews.com </span>
    - <span style="color:lightblue">10 items: cevo.mykajabi.com </span>
    - <span style="color:green">7553 items: Covid-misinformation data </span> set retrieved from Poynter.org: https://www.kaggle.com/datasets/ambityga/covid19misinformation
    - chemtrails? -> email for advise to poynter.org -> reply, they do not know about an according data set (email by  Enock Nyariki <enyariki@poynter.org>
Do 24.08.2023 23:14)
    - Aich/Parde 2022 dataset requested per email Aug-28-2023
  
  - alternative/integrative science
    - Homeopathy
      - Indian Journal of Research in Homoeopathy https://www.ijrh.org/journal/ ; 
    - Antroposophy
      - AnthroMed Library https://www.anthromed.org/
      - Physicians' Association for Antroposophic Medicine (PAAM, https://anthroposophicmedicine.org/)
      - literature lists 2017-2020: Anthroposophic Medicine School of Spiritual Science Medical Section at the Goetheanum (https://medsektion-goetheanum.org/en/research/publications/journal-contributions-on-research-in-anthroposophic-medicine-2017-2019)
      - Complementary Medicine Research, ISSN: 2504-2092 (Print), e-ISSN: 2504-2106 (Online), DOI: 10.1159/issn.2504-2092; 
      Vol. 1-6 (1994-1999) were published under the journal's former title Forschende Komplementärmedizin / Research in Complementary Medicine and Vol. 7-12 (2000-2005) as Forschende Komplementärmedizin und Klassische Naturheilkunde / Research in Complementary and Classical Natural Medicine. 
      - Integrative Cancer Therapies (ICT) https://journals.sagepub.com/home/ICT
      - https://journals.sagepub.com/toc/ICT/current

      
  
 

 
