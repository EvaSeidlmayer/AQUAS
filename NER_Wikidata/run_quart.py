from quart import Quart, request, render_template_string
import urllib
import urllib.parse, urllib.request, json
import aiohttp
import json
import urllib.request


app = Quart(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Text Input</title>
</head>
<body>
    <h1>Enter Text for Wikifier</h1>
    <form action="/" method="POST">
        <textarea name="user_text" rows="10" cols="50" placeholder="Enter your text here..."></textarea><br>
        <button type="submit">Submit</button>
    </form>
    <h2>Response:</h2>
    <pre>{{ response }}</pre>
</body>
</html>
"""



@app.route('/posts')
async def quatsch():
    return 'quatsch'


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
    '''
    req = urllib.request.Request(url, data=data.encode("utf8"), method="POST")
    with urllib.request.urlopen(req, timeout=60) as f:
        response = f.read()
        response = json.loads(response.decode("utf8"))

    for annotation in response["annotations"]:
        print("%s (%s) (%s)" % (annotation["title"], annotation["url"], annotation['wikiDataItemId']))
    '''

'''
async def wikify():
    text = "Syria's foreign minister has said Damascus is ready to offer a prisoner exchange with rebels."
    lang =  'en'
    threshold = 0.8

    annotations = await CallWikifier(text, lang, threshold)
    return json.dumps(annotations, indent=2)

def hello_du():
    return 'hello_12345'
'''


@app.route('/', methods=["GET", "POST"])
async def input():
    if request.method == "POST":
        # Retrieve the user input from the form
        form_data = await request.form
        user_text = form_data.get("user_text", "")

        # Process the input with Wikifier
        annotations = await CallWikifier(user_text)
        response = json.dumps(annotations, indent=2)
    else:
        response = "Submit text to see the results."

    # Render the response in the HTML template
    return await render_template_string(HTML_TEMPLATE, response=response)










'''
@app.route('/')
async def root():
    # Call the helper functions
    output_one = hello_du()
    output_two =  await input()

    return f"{output_one}\n{output_two}"


@app.route('/', methods=["GET", "POST"])
async def input():
    if request.method == "POST":
        # Retrieve the user input from the form
        form_data = await request.form
        user_text = form_data.get("user_text", "")

        # Process the input with Wikifier
        annotations = await CallWikifier(user_text)
        response = json.dumps(annotations, indent=2)
    else:
        response = "Submit text to see the results."

    # Render the response in the HTML template
    return await render_template_string(HTML_TEMPLATE, response=response)
'''

if __name__ == '__main__':
    app.run()
