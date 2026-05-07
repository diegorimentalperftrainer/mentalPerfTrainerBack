import matplotlib

from application.constants import graph

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def generate_chart(category_results, file_path="scores.png"):

    grouped = group_results(category_results)

    categories = list(grouped.keys())
    x = np.arange(len(categories))

    comp_scores = []
    train_scores = []

    for cat in categories:
        comp_scores.append(grouped[cat].get(True, 0))
        train_scores.append(grouped[cat].get(False, 0))

    width = 0.35

    plt.figure(figsize=(12, 6))

    plt.bar(x - width/2, train_scores, width, label=graph.GRAPH_TRAINING, color="green")
    plt.bar(x + width/2, comp_scores, width, label=graph.GRAPH_COMPETITION, color="red")

    plt.xticks(x, categories, rotation=45, ha="right")
    plt.ylabel(graph.GRAPH_Y_LABEL)
    plt.title(graph.GRAPH_TITLE)

    plt.legend()

    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()

    return file_path

def group_results(results):
    grouped = defaultdict(dict)

    for r in results:
        grouped[r.name][r.competition] = r.score

    return grouped