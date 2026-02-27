
"""
Network Operations Analytics -Streamlit Dashboard
Snowflake Native Application

This application provides network operations insights across multiple personas:
- Executive Introduction
- Network Engineer Dashboard
- Network Performance Dashboard
- Network Manager Dashboard
- Executive Summary Dashboard
"""


import streamlit as st
import pandas as pd
from datatime import datetime, timedelta
import graphviz
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import numpy as np
import json
import time

# try to import folium and pydeck for better maps
try:
    import folium
    from streamlit_folium import st_folium
    FOLIUM_AVAILABLE = True
except ImportError:
    FOLIUM_AVAILABLE = False

try:    import pydeck as pdk
    PYDECK_AVAILABLE = True 
except ImportError:
    PYDECK_AVAILABLE = False

# ===========================================================================
# SNOWFLAKE OFFICIAL STYLING AND CONFIGURATION
# ===========================================================================

# Page configuration with snowflake branding
st.set_page_config(
    page_title="Network Operations Analytics - Powered by Snowflake",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Snowflake official colors and fonts
st.markdown("""
    <style>
    /* Snowflake official colors Palette */
    :root {
     --snowflake-blue: #0072C6;
     --snowflake-dark-blue: #004A8F;
      --snowflake-light-blue: #E1F5FE;
     --snowflake-gray: #F5F5F5;
     --snowflake-dark-gray: #333333;
     --snowflake-white: #FFFFFF;
    }

    /*Main background */
    .main {
        background-color: var(--snowflake-gray);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /*Sidebar styling */
    .css-1d391kg {
        background-color: var(--snowflake-dark-blue);
        border-right: 2px solid var(--snowflake-blue);
    }

    /* Sidebar title */
    .css-1d391kg h1 {
        color: var(--snowflake-dack-blue);
        font-weight: 600;
    }

    