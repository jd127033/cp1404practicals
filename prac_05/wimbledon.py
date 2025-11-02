"""
CP1404/CP5632 Practical
Wimbeldon practical
estimate: 30 min
actual:  40 min
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    data = load_data()
    countries, champ_to_count = analyse_records(data)
    print_results(countries, champ_to_count)


def load_data():
    """ Open data from CSV file and begin processing"""
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove CSV header row
        for line in in_file:
            pieces = line.strip().split(",")
            data.append(pieces)
    return data


def analyse_records():
    """ Process record data """
    # Create Dictionary for champ to count
    champ_to_count = {}
    countries = set()
    for record in data:
        countries.add(record[COUNTRY_INDEX])
        # Better to ask for forgiveness than permission
        try:
            champ_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champ_to_count[record[CHAMPION_INDEX]] = 1
    return countries, champ_to_count


def print_results():
    """ load the results for the user """
    print("Wimbledon Champions: ")
    for name, count in champ_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

main()
