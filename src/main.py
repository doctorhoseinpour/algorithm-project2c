import time
import random
import csv
import os
from bfs import bfs, print_path
from generate_graph import generate_graph


def run_project_experiments():
    graphs = {
        "G1": (30, 100),
        "G2": (60, 400),
        "G3": (120, 1600),
        "G4": (240, 3200)
    }

    output_dir = os.path.join(os.path.dirname(__file__), "..", "output_files")

    os.makedirs(output_dir, exist_ok=True)

    csv_file_path = os.path.join(output_dir, "results.csv")

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Graph", "Source", "Destination", "Min-Hop Path", "Time Taken (ms)"])

        for graph_name, (v, e) in graphs.items():
            g = generate_graph(v, e)
            total_time = 0
            valid_pairs = set()

            while len(valid_pairs) < 25:
                s = random.randint(1, v)
                t = random.randint(1, v)
                if (s, t) in valid_pairs or s == t:
                    continue

                start_time = time.perf_counter()
                info = bfs(g, s, t)
                end_time = time.perf_counter()
                path = print_path(info, s, t)

                if path is not None:
                    time_taken = (end_time - start_time) * 1000
                    print(f"Source node = {s}, Destination node = {t}, min-hop path: {path}, time taken = {time_taken:.4f} ms")
                    writer.writerow([graph_name, s, t, path, f"{time_taken:.4f}"])
                    total_time += time_taken
                    valid_pairs.add((s, t))
            average_time = total_time / 25
            print(f"Average time taken for {graph_name}: {average_time:.4f} ms")

            writer.writerow([graph_name, "AVERAGE", "", "", f"{average_time:.4f}"])
            writer.writerow([])  # Empty row to visually separate graphs in the CSV


if __name__ == "__main__":
    run_project_experiments()