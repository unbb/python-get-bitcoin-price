import pandas as pd
import time
from get_waves_price import get_percentage_and_price
from email_to_me import send_email_to_myself


def main():
    count=0
    while(True):
        
        price,percentage = get_percentage_and_price() # get price and percentage of specific coin
        if abs(percentage)>10 or price>2.8: # when the price or percentage is on alert
            send_email_to_myself(percentage,price) # send email to your own address
        count+=1
        print(count)
        time.sleep(1800) # get prize every 0.5 hour 
        # test  
        

# def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    

if __name__=="__main__":
    main()
   