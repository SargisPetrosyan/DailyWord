import requests

def get_verb_example(request):
    # Fetch the JSON data
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
    response.raise_for_status()
    data = response.json()  # Convert the JSON response to a Python object (list)

    # Navigate to the specific example
    verb_meaning = data[0]["meanings"][2]  # Get the third meaning (verb)
    verb_example = verb_meaning["definitions"][0]["example"]  # Get the example for the first definition

    print(verb_example)

get_verb_example()