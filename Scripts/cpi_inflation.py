"""  
Script to calculate and save US CPI inflation rates.  
"""  

import sys  
import os  
from pathlib import Path  
import datetime  

# Add src to Python path  
project_root = Path(__file__).resolve().parents[1]  
sys.path.append(str(project_root))  

from src.cpi_analyzer import CPIAnalyzer  

def main():  
    """Main function to execute the script."""  
    # Initialize analyzer  
    analyzer = CPIAnalyzer()  
    
    try:  
        # Fetch data  
        analyzer.fetch_data()  
        
        # Get last 4 quarters  
        last_4_quarters = analyzer.get_last_n_quarters(4)  
        
        # Create processed data directory if it doesn't exist  
        output_dir = project_root / 'data' / 'processed'  
        output_dir.mkdir(parents=True, exist_ok=True)  
        
        # Save to CSV file  
        output_file = output_dir / f'quarterly_inflation_{datetime.date.today()}.csv'  
        last_4_quarters.to_csv(output_file)  
        
        # Display results  
        print("\nLast 4 quarters of US CPI inflation rates:")  
        print(last_4_quarters)  
        print(f"\nData has been saved to {output_file}")  
        
    except Exception as e:  
        print(f"Error: {str(e)}")  
        sys.exit(1)  

if __name__ == "__main__":  
    main()  
