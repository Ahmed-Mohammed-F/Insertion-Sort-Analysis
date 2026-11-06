# Empirical Analysis of Insertion Sort

**Category:** Insertion Sort / Sorting  
**Language:** Python 3

## Idea
I implemented Insertion Sort, counted comparisons and shifts, and measured its runtime for sorted, reverse-sorted, and random arrays. I also implemented Merge Sort as a comparison.

## Run
```bash
python main.py
```
The experiment writes `results.csv`. Install Matplotlib to generate the graph:
```bash
pip install matplotlib
python main.py
```
Run tests:
```bash
python -m unittest -v
```

## Experiment
Sizes: 100, 300, 600, 1000, 2000, 5000. Fixed random seed 42 keeps input data reproducible. The time is recorded in milliseconds, so measurements may be different on other computers.

## Complexity
- Insertion Sort best case: **O(n)** on sorted input.
- Insertion Sort average/worst case: **O(n²)**.
- Merge Sort: **O(n log n)**, but needs extra memory.

`running_time.png` shows measured time alongside *scaled* O(n) and O(n²) reference curves.
