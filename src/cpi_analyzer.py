"""  
Core functionality for CPI data analysis.  
"""  

import pandas_datareader.data as web  
import datetime  
import pandas as pd  
from typing import Tuple, Optional  

class CPIAnalyzer:  
    """Class for analyzing CPI data and calculating inflation rates."""  
    
    def __init__(self):  
        """Initialize the CPIAnalyzer."""  
        self.data = None  
        
    def fetch_data(self,   
                   start_date: Optional[datetime.datetime] = None,  
                   end_date: Optional[datetime.datetime] = None) -> pd.DataFrame:  
        """  
        Fetch CPI data from FRED.  
        
        Args:  
            start_date: Start date for data fetch  
            end_date: End date for data fetch  
            
        Returns:  
            DataFrame containing CPI data  
        """  
        if start_date is None:  
            start_date = datetime.datetime.now() - datetime.timedelta(days=365 * 2)  
        if end_date is None:  
            end_date = datetime.datetime.now()  
            
        self.data = web.DataReader("CPIAUCSL", "fred", start_date, end_date)  
        return self.data  
    
    def calculate_quarterly_inflation(self) -> pd.DataFrame:  
        """  
        Calculate quarterly inflation rates.  
        
        Returns:  
            DataFrame containing quarterly inflation rates  
        """  
        if self.data is None:  
            raise ValueError("No data available. Please fetch data first.")  
            
        # Resample to quarterly data  
        quarterly_data = self.data.resample('Q').last()  
        
        # Calculate year-over-year inflation rate  
        quarterly_inflation = quarterly_data.pct_change(periods=4) * 100  
        quarterly_inflation.columns = ['Inflation Rate (%)']  
        
        return quarterly_inflation  
    
    def get_last_n_quarters(self, n: int = 4) -> pd.DataFrame:  
        """  
        Get the last n quarters of inflation data.  
        
        Args:  
            n: Number of quarters to return  
            
        Returns:  
            DataFrame containing the last n quarters of inflation data  
        """  
        quarterly_inflation = self.calculate_quarterly_inflation()  
        return quarterly_inflation.tail(n)  
