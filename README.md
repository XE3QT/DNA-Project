# DNA Profiling Program

DNA, the carrier of genetic information in living things, has been used in criminal justice for decades. But how, exactly, does DNA profiling work? Given a sequence of DNA, how can forensic investigators identify to whom it belongs?

Well, DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Every human cell has billions of nucleotides arranged in sequence. Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Some portions of this sequence (i.e., genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals. In the DNA samples below, for example, Alice has the STR AGAT repeated four times in her DNA, while Bob has the same STR repeated five times.

Sample STRs

Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst can be pretty confident they came from the same person. CODIS, the FBI’s DNA database, uses 20 different STRs as part of its DNA profiling process.

What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.

name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25

The data in the above file would suggest that Alice has the sequence AGAT repeated 28 times consecutively somewhere in her DNA, the sequence AATG repeated 42 times, and TATC repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 18, and 25 times, respectively.

So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated AGATs and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of AATG is 22 repeats long, and the longest sequence of TATC is 19 repeats long, that would provide pretty good evidence that the DNA was Bob’s. Of course, it’s also possible that once you take the counts for each of the STRs, it doesn’t match anyone in your DNA database, in which case you have no match.

In practice, since analysts know on which chromosome and at which location in the DNA an STR will be found, they can localize their search to just a narrow section of DNA. But we’ll ignore that detail for this problem.

## Running the Program

1. Make sure you have Python installed on your system.
2. Place the `dna.py` file in the same directory as the CSV file containing STR counts and the text file containing the DNA sequence.
3. Open a terminal or command prompt and navigate to the directory containing the files.
4. Run the program with the following command:
python dna.py database.csv sequence.txt
Example: python dna.py databases/large.csv sequences/14.txt
Your program should output Severus

Replace `database.csv` with the name of your CSV file and `sequence.txt` with the name of your DNA sequence file.

## Program Functionality

- The program takes two command-line arguments: the CSV file containing the STR counts and the text file containing the DNA sequence.
- It reads the contents of the CSV file into memory and identifies each individual's STR counts.
- The DNA sequence is read into memory as well.
- For each STR in the CSV file, the program computes the longest run of consecutive repeats of that STR in the DNA sequence using the `longest_match` helper function.
- If the STR counts match exactly with any individual in the CSV file, the program prints the name of the matching individual.
- If there is no exact match, the program prints "No match."

Please ensure that your CSV file follows the correct format, with the first row containing column names, and the first column being labeled "name."

Feel free to use this program to explore DNA profiles and identify potential matches based on STR counts. Happy DNA profiling!

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
