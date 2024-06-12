from langchain.tools import tool
from bs4 import BeautifulSoup
import requests
from langchain.tools import tool
from duckduckgo_search import DDGS

class WebSearchTools:

#################################### - DDG SEARCH ENGINE TOOL - ####################################
    @tool("internet_search", return_direct=False)
    def internet_search(query: str) -> str:
        """
            Performs an internet search using a DuckDuckGo-like service and returns the results.
            
            Parameters:
            query (str): The search query.
            
            Returns:
            str: The search results or a message indicating no results were found.
        """
            # Assuming `ddgs` is initialized and ready to use here, with a context manager support
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            return results if results else "No results found."
#################################### - DDG SEARCH ENGINE TOOL - ####################################        

####################$################ - BS4 URL SCRAPER TOOL - ############$########################
    @staticmethod
    @tool("process_search_results", return_direct=False)
    def process_search_results(url: str) -> str:
        """
            Processes the content from webpages given a URL using BeautifulSoup.
            
            Parameters:
            url (str): The URL to fetch and process.
            
            Returns:
            str: The text content of the webpage.
        """
        response = requests.get(url=url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup.get_text()
        else:
            return "Failed to fetch content."
####################$################ - BS4 URL SCRAPER TOOL - ############$########################


# ddgs.text(query,maxresults=4,timelimit="d,w,y", keywords="2024")

    @tool("forecast search", return_direct=False)
    def forecast_search(query: str) -> str:
        """
            **** Note: only pass the cryptocurrency name or symbol into the search query****
            **** Note: Use the process_search_results to scrape results *******
            Parameters:
            query (str): The search query.
            
            Returns:
            str: The search results or a message indicating no results were found. 
        """
            # Assuming `ddgs` is initialized and ready to use here, with a context manager support
            
        maxresults = 5
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(f"site:digitalcoinprice.com/forecast {query}", max_results=maxresults)]
            return results if results else "No results found."

    @tool("technical signal search", return_direct=False)
    def technicalsignals_search(query: str) -> str:
        """
           *** Note - Pass only the cryptocurrency name or symbol in this tool and query*****
            **** Note: Use the process_search_results to scrape results *******
            Parameters:
            query (str): The search query.
            
            Returns:
            str: The search results or a message indicating no results were found.
        """
        
            # Assuming `ddgs` is initialized and ready to use here, with a context manager support
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(f"site:centralcharts.com trade signals {query}", max_results=5)]
            return results if results else "No results found."
        
        
    @tool("price target search", return_direct=False)
    def pricetargets_search(query: str) -> str:
        """
           *** Note - Pass only the cryptocurrency name or symbol in this tool and query*****
            
            Parameters:
            query (str): The search query.
            
            Returns:
            str: The search results or a message indicating no results were found.
        """
            # Assuming `ddgs` is initialized and ready to use here, with a context manager support
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(f"site:coincodex.com prediction 2024 {query}", max_results=3)]
            return results if results else "No results found."

