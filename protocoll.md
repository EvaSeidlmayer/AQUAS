# deNBI VM
deNBI VM: scp -P 30327  -i ~/.ssh/id_rsa.pub  data/ready_dataset.csv ubuntu@129.70.51.6:/home/ubuntu
VM parameter: VM: 1; Flavour: de.NBI GPU medium
total core: 14
total RAM: 64GB
total GPUs: 1
Storage Limit 500 GB
Volume Counter 
Bert: https://github.com/huggingface/transformers/blob/v4.28.1/src/transformers/models/bert/modeling_bert.py#L1533

# BERT problems with long texts
- maximum position embedding is 512 tokens in BERT; also when more tokens are set the memory consumption is "unaffordable because all the activations are stored for back-propagation during training" (Ding et al. 2020:2) 
- sliding window approach: 
  - disadvantages: lack of long-distance attention (Ding et al. 2020:2); special relevance of first and last sentence of text paragraph cannot be considerd by sliding window (Ding et al. 2020:6)
  - SLED approach: only for encoder-decoder models (e.g. BART) Maor Ivgi, Uri Shaham, Jonathan Berant; Efficient Long-Text Understanding with Short-Text Models. Transactions of the Association for Computational Linguistics 2023; 11 284–299. doi: https://doi.org/10.1162/tacl_a_00547 

# evaluation of long text understanding
  - SROLLS: Aurko Roy, Mohammad Saffar, Ashish Vaswani, David Grangier; Efficient Content-Based Sparse Attention with Routing Transformers. Transactions of the Association for Computational Linguistics 2021; 9 53–68. doi: https://doi.org/10.1162/tacl_a_00353

# first results < July 2023 documentend in EAHIL presentation 

# data set
- three categories: scientific (0), popular science (1), disinformation (2)
- scientific: 451 + 312+ 4616 PubMed Central: https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/
- popular science: 
  - Wikipedia: 648 
  - MedlinePlus: 1.200 https://medlineplus.gov/healthtopics.html 
   
- desinformation: 
  - 99 items: health.news 
  - 78  items: healthimpactnews.com
  - 10 items: cevo.mykajabi.com
  - 7553 items: Covid-misinformation data set retrieved from Poynter.org: https://www.kaggle.com/datasets/ambityga/covid19misinformation
  - Homeopathy?, e. g.  Indian Journal of Research in Homoeopathy https://www.ijrh.org/journal/ ; Journal of Evidence-Based Integrative Medicine (JEBIM) is a peer-reviewed open access journal which focuses on hypothesis-driven and evidence-based research in all fields integrative medicine. Previously the Journal of Evidence-Based Complementary and Alternative Medicine (JEBCAM): https://journals.sagepub.com/home/chp
  - chemtrails? 
 
 
