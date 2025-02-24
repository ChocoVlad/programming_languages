import pytest
import allure
from checkers.popularity_checker import check_popularity

threshold_values = [
    10 ** 7,
    int(1.5 * 10 ** 7),
    5 * 10 ** 7,
    10 ** 8,
    5 * 10 ** 8,
    10 ** 9,
    int(1.5 * 10 ** 9)
]


@allure.feature("Popularity Check")
@allure.story("Verify website popularity")
@pytest.mark.parametrize("threshold", threshold_values)
def test_sites_popularity_threshold(table_data, threshold):
    """
    Verifies that each website's popularity meets the specified threshold.
    """
    errors = []
    with allure.step(f"Checking threshold: {threshold}"):
        for row in table_data:
            error = check_popularity(row, threshold)
            if error:
                errors.append(error)
    if errors:
        pytest.fail("\n".join(errors))
