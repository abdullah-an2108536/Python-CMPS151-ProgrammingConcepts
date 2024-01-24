import requests
from bs4 import BeautifulSoup

# Define a function to retrieve Google Scholar citations
def get_google_scholar_citations(article_title):
    # Construct the Google Scholar URL
    search_query = f'https://scholar.google.com/scholar?q={article_title}'

    # Send an HTTP GET request to Google Scholar
    response = requests.get(search_query)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the citation count (if available)
        citation_element = soup.find('a', {'class': 'gs_nph'})
        if citation_element:
            citation_count = citation_element.text
            return citation_count
        else:
            return "Citation count not found"
    else:
        return "Error accessing Google Scholar"

# Initialize an empty list to store article names and their corresponding citations
article_citations = []

# Ask the user for article names
while True:
    article_title = input("Enter an article title (or type 'q' to quit): ")
    if article_title.lower() == 'q':
        break
    citation = get_google_scholar_citations(article_title)
    article_citations.append({'Article Title': article_title, 'Google Scholar Citations': citation})

# Display the results
print("\nGoogle Scholar citations:")
for entry in article_citations:
    print(f"Article Title: {entry['Article Title']}")
    print(f"Google Scholar Citations: {entry['Google Scholar Citations']}\n")

# Save the results to a file (e.g., CSV)
with open('article_citations.csv', 'w') as f:
    for entry in article_citations:
        f.write(f"{entry['Article Title']},{entry['Google Scholar Citations']}\n")

print("Results saved to 'article_citations.csv'.")
