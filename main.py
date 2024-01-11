from openai import OpenAI
import requests
from api_key import api_key, search_engine_id, OPENAI_API_KEY

num_results = 3
ean_code = '5900694412941'

def find_search_results_with_snippets(ean_code, num_results):
    all_results_text = ""

    # Call the Google Search API
    search_url = f"https://www.googleapis.com/customsearch/v1?q={ean_code}&key={api_key}&cx={search_engine_id}&num={num_results}"
    response = requests.get(search_url)

    # Check the response status code
    if response.status_code != 200:
        return f"Error: Received status code {response.status_code}"

    search_results = response.json()
    # Check if any items are returned
    if 'items' not in search_results:
        return "No search results found."

    # Process the search results
    for result in search_results['items']:
        url = result['link']
        snippet = result.get('snippet', 'No description available')
        all_results_text += f"URL: {url}\nSnippet: {snippet}\n\n"

    return all_results_text

def analyze_text_and_get_product_name(text_to_analyze):
    # Initialize the OpenAI client with API key
    client = OpenAI(api_key=OPENAI_API_KEY)

    # Create a chat completion
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are an assistant skilled in analyzing text to extract specific information."},
            {"role": "user", "content": f"Analyze this text and identify the product name: {text_to_analyze}, return only one name in content result without any description"}
        ]
    )

    # Extracting the response
    response_message = completion.choices[0].message
    content_response = response_message.content   # Extract the content field from the response
    return content_response

results_text = find_search_results_with_snippets(ean_code, num_results)
print(results_text)
product_name = analyze_text_and_get_product_name(results_text)

print("Ean code:", ean_code, "is for product: ", product_name)