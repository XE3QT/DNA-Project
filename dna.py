import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py database.csv sequence.txt")

    # Read command-line arguments
    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read database file into a variable
    database = read_database(database_file)

    # Read DNA sequence file into a variable
    sequence = read_sequence(sequence_file)

    # Find longest match of each STR in DNA sequence
    matches = find_str_matches(database, sequence)

    # Check database for matching profiles
    matching_individual = find_matching_individual(database, matches)

    # Print the result
    if matching_individual:
        print(matching_individual)
    else:
        print("No match")


def read_database(filename):
    """Reads the CSV file containing the database and returns its contents as a list of dictionaries."""
    database = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)
    return database


def read_sequence(filename):
    """Reads the DNA sequence file and returns its contents as a string."""
    with open(filename, "r") as file:
        sequence = file.read().strip()
    return sequence


def find_str_matches(database, sequence):
    """Finds the longest match of each STR in the DNA sequence and returns a dictionary of counts."""
    matches = {}
    str_list = list(database[0].keys())[1:]  # Get the list of STRs from the first row of the database
    for STR in str_list:
        longest_run = longest_match(sequence, STR)
        matches[STR] = longest_run
    return matches


def longest_match(sequence, subsequence):
    """Returns the length of the longest run of subsequence in the sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    i = 0
    while i < sequence_length:
        count = 0
        while sequence[i: i + subsequence_length] == subsequence:
            count += 1
            i += subsequence_length
        longest_run = max(longest_run, count)
        i += 1
    return longest_run


def find_matching_individual(database, matches):
    """Finds the matching individual in the database based on the STR matches and returns the name."""
    for row in database:
        match_count = 0
        for STR, count in matches.items():
            if int(row[STR]) == count:
                match_count += 1
        if match_count == len(matches):
            return row['name']
    return None


if __name__ == "__main__":
    main()

