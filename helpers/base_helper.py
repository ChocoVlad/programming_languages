import re


def prepare_languages(text: str) -> list[str]:
    """
    Splits the input text.

    :param text: The input string containing languages.
    :return: A list of languages.
    """
    return [s.strip() for s in text.split(',')] if text else []


def remove_links(text: str) -> str:
    """
    Removes reference links ([2], [12]).

    :param text: The table cell text.
    :return: The cleaned text with reference links removed.
    """
    cleaned = re.sub(r'\[\d+\]', '', text)
    return cleaned.strip()


def prepare_popularity(text: str) -> int:
    """
    Extracts all digits from the input text.

    :param text: The input string representing popularity.
    :return: The integer value.
    """
    numeric_str = "".join(re.findall(r'\d', text))
    return int(numeric_str)
