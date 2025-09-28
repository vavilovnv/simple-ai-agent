"""Module for tools."""

from langchain_tavily import TavilySearch

web_search_tool = TavilySearch(max_results=3)
