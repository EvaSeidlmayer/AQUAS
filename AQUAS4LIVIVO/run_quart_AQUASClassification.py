from quart import Quart, request, render_template_string, jsonify
import joblib
import numpy as np
import json
from transformers import BertTokenizer, AutoModelForSequenceClassification
import torch
import sklearn
import aiohttp

app = Quart(__name__)



HTML_TEMPLATE = HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>NLP strategies to handle disinformation</title>
    <style>
        body {
            background-color: #0EA2AB; 
            font-family: Arial, sans-serif;
            margin:100px;
            padding:0;
        }
        h1, h2 {
            color: #333;
        }
        
        .container {
            display: flex;
            justify-content: space-between;
            margin: 15px;
        }
        .container {
            display: flex;
            justify-content: space-between;
            margin: 15px;
        }
        .form-section {
            width: 45%;
            padding: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-height: 700px; /* Adjust the height as needed */
            overflow-y: auto; /* Add scrollbar if content overflows */
        }
        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        pre {
            background-color: #e9e9e9;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        #chart-container {
            width: 90%; 
            max-width: 800px; 
            background-color: #b6e3e5
            margin: 0 auto; /* Center the chart */
        }
        footer {
            margin: 20px;
            text-align: center;
            color: #333;
        }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
</head>
<body>
    <h1>NLP strategies to handle disinformation</h1>
        <p> The increasing prevalence of misinformation and disinformation represents a serious threat to our democratic society. Spread by political lobby groups or companies to manipulate public discourse, it can be hard for users to determine whether the information at hand is true or false. Disinformation is also prevalent in scientific settings and can therefore has a direct impact on scientists’ work. <b>Experience different methods to explore a questionable texts passage.</b>   </p> 
        <p>Disinformation are characterized by the <b>1. (Correctnes) ICH WÜRDE HIER EHER SAGEN Accuracy of information</b> and by the <b>2. Intention to spread misinformation</b>. Their intention is driven by the pursuit of money and influence aiming to discriminate other competitors.</p>        
    <div class="container">
        <div class="form-section">
       <h3>1. Wikifier Annotator</h3>
        <p> Currently it is not easy to validate facts in full texts automatically. However, we can use <a href='https://en.wikipedia.org/wiki/Named-entity_recognition'>Named-entity Recognition</a> (NER) to identify crucial terms and use the <i>entity linking service</i> <b>Wikifier</b> to retrieve <b>Wikidata</b> and <b>Wikipedia</b> records in order to verify the proposed information.</p>
        <p> Try to annotate the questionable text using <b>Wikifier</b> and get more information on the <a href='https://www.wikifier.org/'>Wikifier</a> was implemented by Janez Brank.  </p>  
         
         
         <p> Use <b>Wikifier</b> for additional information by Wikipedia or Wikidata. The text is cut off after 1000 characters. </p>
        <form action="/" method="POST">
            <textarea name="user_text_A" rows="10" cols="50" placeholder="Enter your text here..."></textarea><br>
            <button type="submit">Submit</button>
        </form>
    <h2>Response:</h2>
    <pre>{{ response_1 }}</pre>
        </div>
        
        
    <div class="form-section"> 
        <h3> 2. Four Shades of Life Sciences Intention Classifier </h3>
        <p>The hypothesis of project AQUAS is that the goals for spreading disinformation (attention, money, influence for political claims) shape syntax and semantic of texts. Applying machine learning techniques HIER FEHLT WAS a language model can learn the characteristics of texts, specific terms and language styles. In order to train a langugage model, we compiled a dataset on life science documents related to the four categories ("four shades of Life sciences"):</p> 
            <ol>
                <li>scientific text style</li> 
                <li>popular scientific text style</li>  
                <li>disinformative text style
                <li>alternative scientific text style</li>
            </ol>     
        <p>Based on this data set several models had been fine tuned to classifiy similar language styles.  
        You can choose between standard <a href='https://en.wikipedia.org/wiki/Bag-of-words_model'>Bag of Words</a> methods, such as <a href="https://en.wikipedia.org/wiki/Random_forest">Random Forest</a>, <a href='https://en.wikipedia.org/wiki/Support_vector_machine'>Support Vector Machine</a>,<a href='https://en.wikipedia.org/wiki/Logistic_regression'>Logistic Regression</a> ,  and  <a href='https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)'>Transformer</a> language models, such as Bert, Scibert, and Specter.</p>    
    
        <form action="/" method="POST">
            <textarea name="user_text_B" rows="10" cols="50" placeholder="Enter your text here..."></textarea><br>
            <label>
                <input type="radio" name="option" value="option_1" > Random Forest Classifier
            </label>
            <label>
                <input type="radio" name="option" value="option_5" > Support Vector Machine
            </label>
            <label>
                <input type="radio" name="option" value="option_6" > Logistic Regression 
            </label>
            <label>
                <input type="radio" name="option" value="option_2" > Fine tuned Bert-base uncased model
            </label>
            <label>
                <input type="radio" name="option" value="option_3"> Fine tuned SciBert model
            </label>
            <label>
                <input type="radio" name="option" value="option_4"> Fine tuned Specter model
            </label><br>
            <button type="submit">Submit</button>
        </form>
            <h3>Response:</h3>
            <div id="chart-container">
             <canvas id="predictionsChart"></canvas>
            </div>
            
            <pre>{{ response_2 }}</pre>

        </div>
    </div>
    <div class="footer">
        <h2> On the project AQUAS</h2>
        <p>The project "Automatic Quality Assessment: NLP methods for semantic mapping of life-science texts" (AQUAS) is funded by German Research Foundation. The project runs from November 2022 till November 2025. Please notice the project website: <a href='https://www.zbmed.de/en/research/current-projects/aquas'>AQUAS at ZBMED</a>  </p>
        <p> <b>Contact:</b> Eva Seidlmayer, Dr. phil., M.LIS<br> Data Sciences and Services, Research Fellow<br> ORCID: 0000-0001-7258-0532<br>
        Mastodon: @eta_kivilih | Bluesky: @etakivilih.bsky.social<br> ZB MED – Informations Centre for Life Sciences<br> Gleueler Straße 60<br>
        50931 Cologne <br> Germany<br> <a href ='www.zbmed.de'>www.zbmed.de</a><br> INFORMATION. KNOWLEDGE. LIFE.      </p>
        <img src="{{ url_for('static', filename='ZBMED17_e_rgb_cl_www.svg') }}" alt="Logo of ZB MED https://www.zbmed.de/en/" style="width:2000px;height:1250px;">
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', (event) => {
            const predictions = {{ predictions|tojson }};
            const ctx = document.getElementById('predictionsChart').getContext('2d');
            const labels = ['Scientific Text Style', 'Popular Scientific Text Style', 'Disinforming Text Style', 'Alternative Scientific Text Style'];
            const data = {
                labels: labels,
                datasets: [{
                    label: 'of 100%', 
                    data: predictions[0],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)'
                    ],
                    borderWidth: 1
                }]
            };
            const config = {
                type: 'bar',
                data: data,
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                     plugins: {
                    legend: {
                        labels: {
                            color: '#000000',
                            boxWidth: 20, // Width of the colored box
                            boxHeight: 20, // Height of the colored box
                            usePointStyle: true, // Use point style for the legend item
                            pointStyle: 'rectRounded', // Style of the point (e.g., 'circle', 'rect', 'rectRounded', etc.)
                            padding: 10 // Padding around the legend item
                        }
                    }
                }                   
                    
                }
            };
            new Chart(ctx, config);
        });
    </script>
    
</body>
</html>
"""


async def Call_AQUAS_RandomForest(text, classifier, vectorizer):
    text_list = [text]
    #vectorize!
    text_vectorized = vectorizer.transform(text_list)
    #predict!
    predictions = classifier.predict(text_vectorized)
    predictions_int = predictions.astype(int).tolist()

    return {'predictions': predictions_int}

async def Call_AQUAS_Bert(text, model, Bert_tokenizer):
    tokens = Bert_tokenizer(text, max_length=512, padding="max_length", truncation=True, return_tensors='pt')
    input_ids = tokens['input_ids']
    attn_mask = tokens['attention_mask']

    with (((torch.no_grad()))):
        output = model(input_ids=input_ids, attention_mask= attn_mask)
        logits = output['logits']
        sigmoid_output =torch.sigmoid(logits)
        soft_output = torch.softmax(logits, -1)
        print('DAS IST DER SOFT OUTPUT', soft_output)
        sigmoid = sigmoid_output.tolist()
        pred_sci, pred_pop, pred_dis, pred_alt = sigmoid[0][0], sigmoid[0][1], sigmoid[0][2], sigmoid[0][3]
        print('DAS IST DER sigmoid OUTPUT', pred_sci, pred_pop, pred_dis, pred_alt)
        outp=[]
        outpu = []
        outp.append(pred_sci)
        outp.append(pred_pop)
        outp.append(pred_dis)
        outp.append(pred_alt)
        outpu.append(outp)
        output = torch.Tensor(outpu)
        print('xxxxxxxxxx', output)

    predicted_class = torch.argmax(output, dim=-1).item()
    predicted_probability = output[0][predicted_class].item()

    return {
        'predicted_class': predicted_class+1,
        'predicted_probability': predicted_probability,
        'probabilities': output.tolist()
    }

    #return pred_sci, pred_pop, pred_dis, pred_alt

async def CallWikifier(text, lang="en", threshold=0.8):
    # Prepare the URL.
    url = "http://www.wikifier.org/annotate-article"
    data = {
        "text": text, "lang": lang,
        "userKey": "amfkqziidvlmqytlboyaoxrysxgvgw",
        "pageRankSqThreshold": "%g" % threshold, "applyPageRankSqThreshold": "true",
        "nTopDfValuesToIgnore": "200", "nWordsToIgnoreFromList": "200",
        "wikiDataClasses": "true", "wikiDataClassIds": "false",
        "support": "true", "ranges": "false", "minLinkFrequency": "2",
        "includeCosines": "false", "maxMentionEntropy": "3"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as resp:
            response = await resp.json()
            return response.get("annotations", [])



# Load the trained classifier from the file
RF_classifier = joblib.load(
    '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/BoW/2025-01-06_FSoLF-25-v5_random_forest_classifier.pkl')

# Load the vectorizer from the file
RF_vectorizer = joblib.load(
    '/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/BoW/2025-01-06_FSoLF-25-v5_vectorizer.pkl')

SVM_classifier = joblib.load('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/BoW/2025-01-10_FSoLF-25-v5_SVM_classifier.pkl')
SVM_vectorizer = joblib.load('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/BoW/2025-01-10_FSoLF-25-v5_SVM_vectorizer.pkl')

LRG_classifier = joblib.load('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/BoW/2025-01-10_FSoLF-25-v5_LRG_classifier.pkl')
LRG_vectorizer = joblib.load('/home/ruth/ProgrammingProjects/AQUS/AQUAS/data/data-set-topic-wise_2024/BoW/2025-01-10_FSoLF-25-v5_LRG_vectorizer.pkl')
Bertbase_model = AutoModelForSequenceClassification.from_pretrained('/home/ruth/ProgrammingProjects/AQUS/AQUAS/models/FSoLS-24-v5_Bertbase_e1_lr3e-5_mlclass', num_labels = 4)
Scibert_model = AutoModelForSequenceClassification.from_pretrained('/home/ruth/ProgrammingProjects/AQUS/AQUAS/models/FSoLS-24-v5_SciBert_e3_lr3e-5_mlclass', num_labels = 4)
SPECTER_model = AutoModelForSequenceClassification.from_pretrained('/home/ruth/ProgrammingProjects/AQUS/AQUAS/models/FSoLS-24-v5_Specter_e3_lr3e-5_mlclass', num_labels = 4)
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')



@app.route('/', methods=['GET','POST'])
async def input():
    response_1 = 'Please submit text for Wikifier Annotation'
    response_2 = 'Please submit text for text style classification'
    predictions = [[0,0,0,0]]

    if request.method == "POST":
        # Get user input from form
        form_data = await request.form
        text_A = form_data.get('user_text_A', '')
        text_A = text_A[:1000]
        print('text lenght:', len(text_A))
        text_B = form_data.get('user_text_B', '')
        option = form_data.get('option')

        if text_A:
            annotations = await CallWikifier(text_A)
            response_1 = json.dumps(annotations, indent=2)

        if text_B:
            # Handle the selected option
            if option == 'option_1':
                # Process for Option 1
                results = await Call_AQUAS_RandomForest(text_B, RF_classifier, RF_vectorizer)
                response_2 = json.dumps(results, indent=2)
            if option == 'option_5':
                # Process for Option 1
                results = await Call_AQUAS_RandomForest(text_B, SVM_classifier, SVM_vectorizer)
                response_2 = json.dumps(results, indent=2)
            if option == 'option_6':
                # Process for Option 1
                results = await Call_AQUAS_RandomForest(text_B, LRG_classifier, LRG_vectorizer)
                response_2 = json.dumps(results, indent=2)
            elif option == 'option_2':
                # Process for Option 2
                results = await Call_AQUAS_Bert(text_B, Bertbase_model, bert_tokenizer)
                predictions = results['probabilities']
                response_2 = json.dumps(results, indent=2)
            elif option == 'option_3':
                # Process for Option 3
                results = await Call_AQUAS_Bert(text_B, Scibert_model, bert_tokenizer)
                predictions = results['probabilities']
                response_2 = json.dumps(results, indent=2)
            elif option == 'option_4':
                # Process for Option 4
                results = await Call_AQUAS_Bert(text_B, SPECTER_model, bert_tokenizer)
                predictions = results['probabilities']
                response_2 = json.dumps(results, indent=2)

    return await render_template_string(HTML_TEMPLATE, response_1=response_1, response_2=response_2,  predictions=predictions)




if __name__ == '__main__':
    app.run(debug=True)
