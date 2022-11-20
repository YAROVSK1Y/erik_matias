def ciyt_country(city, county, population=""):
    if population:
        formatted_name = f"{city.title()} {county.title()} population-{population}"
    else:
        formatted_name = f"{city.title()} {county.title()}"

    return formatted_name


