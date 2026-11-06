"""Simple experiment: Insertion Sort versus Merge Sort."""
import csv
import random
import time
from pathlib import Path

SIZES = [100, 300, 600, 1000, 2000, 5000]
ROOT = Path(__file__).resolve().parent


def insertion_sort(numbers):
    arr = numbers.copy()
    comparisons = 0
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons, shifts


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def time_call(function, data):
    start = time.perf_counter()
    result = function(data)
    elapsed_ms = (time.perf_counter() - start) * 1000
    return result, elapsed_ms


def run_experiment():
    rng = random.Random(42)
    rows = []
    for size in SIZES:
        random_values = [rng.randint(0, 100000) for _ in range(size)]
        inputs = {
            "sorted": sorted(random_values),
            "reverse": sorted(random_values, reverse=True),
            "random": random_values,
        }
        for kind, values in inputs.items():
            (answer, comparisons, shifts), elapsed = time_call(insertion_sort, values)
            assert answer == sorted(values)
            row = {
                "n": size, "input": kind, "time_ms": round(elapsed, 4),
                "comparisons": comparisons, "shifts": shifts,
            }
            rows.append(row)
            print(f"n={size:5} {kind:7} {elapsed:9.3f} ms   comparisons={comparisons:9}  shifts={shifts:9}")
    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return rows


def plot_results(rows):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Install matplotlib (pip install matplotlib) to create the chart.")
        return
    fig, ax = plt.subplots(figsize=(8, 4.8))
    for kind in ("sorted", "random", "reverse"):
        selected = [r for r in rows if r["input"] == kind]
        ax.plot([r["n"] for r in selected], [r["time_ms"] for r in selected],
                marker="o", label=f"Insertion - {kind}")
    # Scale theoretical curves for a shape comparison, not absolute timing.
    biggest = max(r["time_ms"] for r in rows)
    ax.plot(SIZES, [biggest * n / max(SIZES) for n in SIZES], "--", alpha=.55, label="O(n), scaled")
    ax.plot(SIZES, [biggest * (n / max(SIZES))**2 for n in SIZES], "--", alpha=.55, label="O(n^2), scaled")
    ax.set(xlabel="Number of elements (n)", ylabel="Time (milliseconds)", title="Insertion Sort Running Time")
    ax.legend(fontsize=8)
    ax.grid(alpha=.25)
    fig.tight_layout()
    fig.savefig(ROOT / "running_time.png", dpi=160)
    plt.close(fig)
    print("Saved results.csv and running_time.png")


def compare_merge_sort():
    values = list(range(5000, 0, -1))
    _, insertion_ms = time_call(insertion_sort, values)
    merge_answer, merge_ms = time_call(merge_sort, values)
    assert merge_answer == sorted(values)
    print(f"\nReverse sorted n=5000: insertion={insertion_ms:.2f} ms, merge={merge_ms:.2f} ms")


if __name__ == "__main__":
    data = run_experiment()
    plot_results(data)
    compare_merge_sort()
