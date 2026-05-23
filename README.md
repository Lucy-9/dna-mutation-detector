# DNA Mutation Detector

This is a simple Python project that compares an original DNA sequence with a changed DNA sequence and detects possible mutations.

## What This Program Does

The program takes two DNA sequences as input:

1. Original DNA sequence
2. Changed DNA sequence

It then compares both sequences and detects whether any mutation has occurred.

## Types of Mutations Detected

This program can detect:

### 1. Substitution Mutation

A substitution happens when one base is replaced by another base.

Example:

```text
Original: ATGC
Changed:  ATCC
```

Here, `G` is changed to `C`.

The program also classifies substitution into:

#### Transition Mutation

A transition mutation occurs when:

- Purine changes to purine: `A ↔ G`
- Pyrimidine changes to pyrimidine: `C ↔ T`

#### Transversion Mutation

A transversion mutation occurs when:

- Purine changes to pyrimidine
- Pyrimidine changes to purine

Purines: `A`, `G`  
Pyrimidines: `C`, `T`

---

### 2. Deletion Mutation

A deletion happens when one or more bases are removed from the original DNA sequence.

Example:

```text
Original: ATGCA
Changed:  ATGA
```

Here, one base has been deleted.

---

### 3. Insertion Mutation

An insertion happens when one or more bases are added to the original DNA sequence.

Example:

```text
Original: ATGC
Changed:  ATGCA
```

Here, one base has been inserted.

---

## How to Run the Program

Make sure Python is installed on your computer.

Run the program using:

```bash
python dna_mutation_detector.py
```

Then enter the DNA sequences when asked:

```text
Enter the original DNA sequence: ATGC
Enter the Changed DNA sequence: ATCC
```

---

## Example Output

```text
Mutation detected at position 3
G changed to C
Type of mutation: Substitution
Type of mutation: Transversion mutation
```

---

## Features

- Accepts DNA sequences from the user
- Converts lowercase letters to uppercase automatically
- Detects substitution, insertion, and deletion mutations
- Classifies substitution as transition or transversion
- Shows the position where mutation occurs

---

## Concepts Used

This project uses basic Python concepts such as:

- Lists
- Functions
- Loops
- Conditional statements
- String input
- DNA base comparison

---

## Limitations

This program is beginner-friendly and detects simple mutations.

It works best when comparing short DNA sequences and may not accurately detect complex mutations involving multiple insertions or deletions at different positions.

---

## Author

Gayatri Ghosh