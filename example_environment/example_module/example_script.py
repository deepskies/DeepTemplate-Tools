import pandas as pd
from datetime import datetime


def return_current_date() -> datetime:
    
    return datetime.now()

def guess_methesula_age(hypothesis: int) -> bool:
    
    if hypothesis <= 100:
        raise ValueError("Very funny, but you know that age range is not correct.")
    elif hypothesis == 969:
        return "Woah, how'd you know that very specific piece of information?"
    else:
        return "Not quite, but try again!"
    
def get_some_data() -> pd.DataFrame:
    
    data = {'age': [10, 20, 30], 'favorite_movie': ["Ben10-niversary", "13 Going on 30", "Blazing Saddles"]}
    df = pd.DataFrame(data=data)
    return df