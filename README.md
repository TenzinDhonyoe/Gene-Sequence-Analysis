<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gene Sequence Analysis Program</title>
</head>
<body>
    <h1>Gene Sequence Analysis Program</h1>
    <h2>Overview</h2>
    <p>This repository contains two Python programs for gene sequence analysis, focusing on different aspects of DNA sequence analysis. The first program involves pattern matching, gene finding, and promoter detection, while the second program reads sequences from a FASTA file and compares OR and NC sequences to identify mutations.</p>

    
  <h2>Files</h2>
    <ol>
        <li><code>pattern_matching.py</code>: Contains functions for gene sequence analysis, including pattern matching, finding stop codons, Shine-Dalgarno sequences, and promoters.</li>
        <li><code>fasta_sequence_analysis.py</code>: Reads sequences from a FASTA file, stores them, and compares NC and OR sequences to identify and categorize mutations.</li>
    </ol>

  <h2>Functions in <code>pattern_matching.py</code></h2>

  <h3><code>matches(target, pattern, limit)</code></h3>
    <p>This function checks if the target sequence matches the pattern with a specified number of allowed mismatches.</p>
    <h4>Parameters:</h4>
    <ul>
        <li><code>target</code> (str): The sequence to be checked.</li>
        <li><code>pattern</code> (str): The consensus sequence to match against.</li>
        <li><code>limit</code> (int): The allowed number of mismatches.</li>
    </ul>
    <h4>Returns:</h4>
    <ul>
        <li><code>bool</code>: True if the number of mismatches is within the limit, False otherwise.</li>
    </ul>

  <h3><code>findpattern(seq, pattern, start, end, incr, limit)</code></h3>
    <p>Finds the specified pattern within the given sequence range.</p>
    <h4>Parameters:</h4>
    <ul>
        <li><code>seq</code> (str): The sequence to search within.</li>
        <li><code>pattern</code> (str): The pattern to search for.</li>
        <li><code>start</code> (int): The starting index for the search.</li>
        <li><code>end</code> (int): The ending index for the search.</li>
        <li><code>incr</code> (int): The increment step for the search.</li>
        <li><code>limit</code> (int): The allowed number of mismatches.</li>
    </ul>
    <h4>Returns:</h4>
    <ul>
        <li><code>int</code>: The starting index of the pattern if found, -1 otherwise.</li>
    </ul>

  <h3><code>findstop(seq, start, end, incr, minlength)</code></h3>
    <p>Finds the stop codon within the given sequence.</p>
    <h4>Parameters:</h4>
    <ul>
        <li><code>seq</code> (str): The sequence to search within.</li>
        <li><code>start</code> (int): The starting index for the search.</li>
        <li><code>end</code> (int): The ending index for the search.</li>
        <li><code>incr</code> (int): The increment step for the search.</li>
        <li><code>minlength</code> (int): The minimum length of the sequence.</li>
    </ul>
    <h4>Returns:</h4>
    <ul>
        <li><code>int</code>: The index of the stop codon if found, -1 otherwise.</li>
    </ul>

  <h2>Functions in <code>fasta_sequence_analysis.py</code></h2>

  <h3><code>mutation(codon1, codon2)</code></h3>
    <p>Determines the type of mutation (silent, nonsense, or missense) between two codons.</p>
    <h4>Parameters:</h4>
    <ul>
        <li><code>codon1</code> (str): The first codon.</li>
        <li><code>codon2</code> (str): The second codon.</li>
    </ul>
    <h4>Returns:</h4>
    <ul>
        <li><code>str</code>: 'S' for silent, 'N' for nonsense, 'M' for missense mutation.</li>
    </ul>

  <h3><code>get_differences(seq1, seq2)</code></h3>
    <p>Finds and categorizes the differences between two sequences.</p>
    <h4>Parameters:</h4>
    <ul>
        <li><code>seq1</code> (str): The first sequence.</li>
        <li><code>seq2</code> (str): The second sequence.</li>
    </ul>
    <h4>Returns:</h4>
    <ul>
        <li><code>list</code>: A list of differences and their types.</li>
        <li><code>int</code>: The count of differences.</li>
    </ul>

  <h2>Usage</h2>
    <p>To use these programs, simply run the Python scripts with the appropriate input data. Ensure that your sequences are in the correct format and adjust the parameters as needed for your specific analysis.</p>
</body>
</html>
