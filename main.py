import requests

BASE_URL = "https://restcountries.com/v3.1/name/"

def get_country_data(country):
    if not country:
        return None

    try:
        response = requests.get(BASE_URL + country)

        if response.status_code != 200:
            return None

        data = response.json()

        if not data:
            return None

        return data[0]

    except requests.exceptions.RequestException:
        return None


def print_country_info(country_data):
    name = country_data["name"]["common"]
    capital = country_data.get("capital", ["Unknown"])[0]
    population = country_data.get("population", "Unknown")
    region = country_data.get("region", "Unknown")

    languages = country_data.get("languages", {})
    language_list = ", ".join(languages.values()) if languages else "Unknown"

    formatted_population = f"{population:,}" if isinstance(population, int) else population

    print("\nCountry:", name)
    print("Capital:", capital)
    print("Population:", formatted_population)
    print("Region:", region)
    print("Languages:", language_list)


def main():
    while True:
        country = input("\nEnter a country (or 'exit'): ").strip()

        if country.lower() == "exit":
            break

        country_data = get_country_data(country)

        if country_data is None:
            print("Country not found or request failed.")
        else:
            print_country_info(country_data)


if __name__ == "__main__":
    main()