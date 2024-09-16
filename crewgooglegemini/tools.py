
from dotenv import load_dotenv
load_dotenv()
import os

"""
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()
"""
from crewai_tools import WebsiteSearchTool

# Example of initiating tool that agents can use to search across any discovered websites
tool = WebsiteSearchTool()
