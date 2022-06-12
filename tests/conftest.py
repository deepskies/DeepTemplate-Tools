import pytest 
# Some tests in different modules may need the same fixtures. In that case, you can use a global 
# fixture file called conftest.py that allows this behavior.

@pytest.fixture()
def example_fixture_data():
    data = {'age': [10, 20, 30], 'favorite_movie': ["Ben10-niversary", "13 Going on 30", "Blazing Saddles"]}

    yield data 

