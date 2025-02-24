from selenium.webdriver.common.by import By
from models.row_data_model import RowDataModel
from helpers.base_helper import prepare_languages, remove_links, prepare_popularity


class Table:
    def __init__(self, driver, locator: str):
        """
        Initializes the Table object.

        :param driver: Selenium WebDriver instance.
        :param locator: The locator value.

        """
        self.driver = driver
        self.element = driver.find_element(By.CSS_SELECTOR, locator)
        self.headers = self._parse_headers()
        row_elements = self.element.find_elements(By.TAG_NAME, "tr")[1:]
        self.rows = [Row(row, self.headers) for row in row_elements if row.find_elements(By.TAG_NAME, "td")]

    def _parse_headers(self) -> dict:
        """
        Parses the header row of the table and returns a dictionary mapping header names to their column number.

        :return: Dictionary with header names as keys and their indices as values.
        """
        header_row = self.element.find_elements(By.TAG_NAME, "tr")[0]
        header_cells = header_row.find_elements(By.TAG_NAME, "th")
        headers = {}
        for index, cell in enumerate(header_cells):
            text = remove_links(cell.text).split("\n")[0]
            headers[text] = index
        return headers

    def get_rows_model(self) -> list[RowDataModel]:
        """
        Converts all rows of the table to a list of RowDataModel instances.

        :return: List of RowDataModel.
        """
        return [row.to_model() for row in self.rows]


class Row:
    def __init__(self, element, headers: dict):
        """
        Initializes the Row object.

        :param element: Selenium WebElement representing the row.
        :param headers: Dictionary mapping header names to column number.
        """
        self.element = element
        self.headers = headers
        cells = self.element.find_elements(By.TAG_NAME, "td")
        self.cells = [remove_links(cell.text) for cell in cells]

    def get_cell(self, column: str) -> str:
        """
        Retrieves the cell text by column name.

        :param column: The header column name.
        :return: Text of the cell.
        """
        if column not in self.headers:
            raise Exception(f"Column '{column}' not found in the table")
        index = self.headers[column]
        return self.cells[index]

    def to_model(self) -> RowDataModel:
        """
        Converts the row into a RowDataModel instance.

        :return: A RowDataModel object with data extracted from the row.
        """
        website = self.get_cell("Websites")
        frontend_text = self.get_cell("Front-end")
        backend_text = self.get_cell("Back-end")
        popularity_text = self.get_cell("Popularity")
        frontend = prepare_languages(frontend_text)
        backend = prepare_languages(backend_text)
        popularity = prepare_popularity(popularity_text)
        return RowDataModel(
            website=website,
            frontend=frontend,
            backend=backend,
            popularity=popularity
        )
