def check_popularity(row, threshold: int):
    """
    Checks if the website's popularity meets the threshold.

    :param row: A data model representing a website row.
    :param threshold: The minimum expected popularity value.
    :return: An error message string if the website's popularity is below the threshold; otherwise, None.
    """
    if row.popularity < threshold:
        frontend_str = ", ".join(row.frontend)
        backend_str = ", ".join(row.backend)
        return (
            f"{row.website} (Frontend: {frontend_str}|Backend: {backend_str}) has {row.popularity} unique visitors per month. "
            f"(Expected more than {threshold})"
        )
    return None
