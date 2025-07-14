import matplotlib.pyplot as plt

def plot_f1_scores(f1_scores_dict):
    months = list(f1_scores_dict.keys())
    scores = list(f1_scores_dict.values())

    plt.figure(figsize=(8, 4))
    plt.plot(months, scores, marker='o')
    plt.title("F1-score mensual")
    plt.xlabel("Mes")
    plt.ylabel("F1-score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
