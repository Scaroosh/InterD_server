import streamlit as st
import yfinance as yf
from typing import Optional
from google.oauth2 import service_account
from google.cloud import aiplatform
from langchain.tools import Tool
from langchain_google_vertexai import VertexAI
from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun
from WebScape_TOOL import WebSearchTools
import secret as secret

def init_sample(
    project: Optional[str] = None,
    location: Optional[str] = None,
    experiment: Optional[str] = None,
    staging_bucket: Optional[str] = None,
    service_account_file: Optional[str] = secret.path_to_file,  # Add parameter for service account file path
    encryption_spec_key_name: Optional[str] = None,
    service_account_email: Optional[str] = secret.email,  # Optional: Use if you need to specify a service account email
):
    # Load credentials from the service account file if provided
    credentials = None
    if service_account_file:
        credentials = service_account.Credentials.from_service_account_file(service_account_file)

    aiplatform.init(
        project=project,
        location=location,
        experiment=experiment,
        staging_bucket=staging_bucket,
        credentials=credentials,
        encryption_spec_key_name=encryption_spec_key_name,
        service_account=service_account_email,  # This should be an email if you're specifying a service account
    )

init_sample(
        project=secret.project_name,
        location='us-west1',
        service_account_file=secret.path_to_file
    )
llm = VertexAI(model_name="gemini-pro", verbose=True, max_output_tokens=2048, temperature=0.0)

duckduckgo_search_tool = DuckDuckGoSearchRun()
search = WebSearchTools()
process = WebSearchTools().process_search_results

def create_crewai_crypto_setup(crypto_symbol):
    ticker_obj = yf.Ticker(crypto_symbol)
    info = ticker_obj.info

    ticker_info_tool = Tool(
        name="Ticker Information",
        func=lambda: info,
        description="Provides information about the cryptocurrency from the Yahoo Finance API."
    )

    llm = VertexAI(model_name="gemini-pro", verbose=True, max_output_tokens=2048, temperature=0.0)
    duckduckgo_search_tool = DuckDuckGoSearchRun()
    search = WebSearchTools()
    process = WebSearchTools().process_search_results

    research_agent = Agent(
        role="Crypto Analysis Expert",
        goal=f"""
        Perform market analysis on cryptocurrency, your job is search, research and generate a report based on the clients prompt. 
        NOTE - Make sure the report is clear, concise and professional with actionable advice and provide any relevant metrics / information.
        Your audience is professional traders that understand the risks.
        Ensure that you focus your search and research on the cryptocurrency symbol/name provided in the prompt along with the scope of or details the client wants.
        Here is the clients prompt - {crypto_symbol}.
        """,
        backstory="Expert in technical analysis, market sentiment, and investment strategy for cryptocurrencies.",
        verbose=True,
        allow_delegation=True,
        tools=[duckduckgo_search_tool, ticker_info_tool],
        llm=llm,
    )

    research_agent2 = Agent(
        role="Crypto Analysis Expert",
        goal=f"""Using the websearchtools perform in-depth research for the cryptocurrency - {crypto_symbol}, 
        focusing on market outlook, investment strategies, technical/trade signals, etc
        """,
        backstory="Expert in technical analysis, market sentiment, and investment strategy for cryptocurrencies.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    market_data_t0 = Task(
        description=f"""
        Research using the following clients prompt which includes a cryptocurrency symbol or coin name - {crypto_symbol}. 
        Focus on the topic/details that are relevant to the clients prompt.
        Research and search the information desired using the search tools available. Always attempt to use the process tool after every search.
        Then organize your information and metrics which will be used and referred to in order to create a market/trade report for the client
        """,
        expected_output="""{
            "coin": crypto_symbol,
            "Technical Analysis": {
                "RSI": "",
                "MACD": "",
                "MA": "",
                "Fear & Greed": ""
            },
            "Market Sentiment": {
                "Social Media": "",
                "News Sentiment": ""
            },
            "Investment Strategy": {
                "Short-Term": "",
                "Long-Term": ""
            },
            "Key Metrics": {
                "Price": "",
                "Market Cap": "",
                "24-Hour Trading Volume": "",
                "Circulating Supply": ""
            },
            "Suggestion": "Overall Investment Suggestion"
            "Final Verdict": "One if these three words: buy, hold, sell"
        }""",
        tools=[search.pricetargets_search, search.forecast_search, search.technicalsignals_search, process],
        agent=research_agent,
    )

    consolidate_info_t4 = Task(
        description=f"""
        Consolidate the information gathered from the previous tasks into a JSON format with the following structure:
        {{
            "coin": "",
            "Technical Analysis": {{
                "RSI": "",
                "MACD": "",
                "MA": "",
                "Fear & Greed": ""
            }},
            "Market Sentiment": {{
                "Social Media": "",
                "News Sentiment": ""
            }},
            "Investment Strategy": {{
                "Short-Term": "",
                "Long-Term": ""
            }},
            "Key Metrics": {{
                "Price": "",
                "Market Cap": "",
                "24-Hour Trading Volume": "",
                "Circulating Supply": ""
            }},
            "Suggestion": "Overall Investment Suggestion"
            "Final Verdict": "One if these three words: buy, hold, sell"
        }}
        """,
        expected_output="{}",
        tools=[search.pricetargets_search, search.forecast_search, search.technicalsignals_search, process],
        agent=research_agent2,
    )

    crypto_crew = Crew(
        agents=[research_agent, research_agent2],
        tasks=[market_data_t0, consolidate_info_t4],
        verbose=2,
        process=Process.sequential,
    )
    crew_result = crypto_crew.kickoff()
    return crew_result

def chatbot():
    st.caption("Gemini Pro ")
    message = st.text_input("Enter a Cryptocurrency Ticker + (optional) Techincal/trading signals, price predictions, price targets, buy/sell/hold prices.")
    if message:
        crew_result = create_crewai_crypto_setup(message)
        st.write(crew_result)
