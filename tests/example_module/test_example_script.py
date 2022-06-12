from datetime import datetime
from pandas.testing import assert_frame_equal
import pandas as pd 
import pytest 

from example_environment.example_module.example_script import (
    get_some_data, 
    guess_methuselah_age, 
    return_current_date
)

# This is an example of a pytest fixture. 
# You can use this fixture property to make it easier to use variables 
# and functions that show up in many places throughout tests. These become especially useful for 
# making mock data and mock paths.

@pytest.fixture()
def example_fixture_data():
    data = {'age': [10, 20, 30], 'favorite_movie': ["Ben10-niversary", "13 Going on 30", "Blazing Saddles"]}

    yield data 


def test_return_current_date():
    
    assert return_current_date() == datetime.now()

def test_guess_methuselah_age_success():
    
    assert ("Woah, how'd you know that very specific piece of information?" 
                == guess_methuselah_age(hypothesis=969)
                )

def test_guess_methuselah_age_fail():
    
    assert ("Not quite, but try again!" == guess_methuselah_age(hypothesis=1000))

def test_guess_methuselah_age_bad_guess():
    
    with pytest.raises(ValueError):
        guess_methuselah_age(hypothesis=1)

def test_get_some_data(example_fixture_data):

    df = pd.DataFrame(data = example_fixture_data)
    assert_frame_equal(df, get_some_data())