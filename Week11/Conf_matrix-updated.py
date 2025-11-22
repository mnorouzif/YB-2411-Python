import os
import numpy as np
import matplotlib.pyplot as plt

# === CONFIG ===
output_dir = "confusion_matrices"
selected_slides = list(range(6, 11)) + list(range(12, 15))
os.makedirs(output_dir, exist_ok=True)

# === CONFUSION MATRIX DATA (edit here per slide) ===
# Each slide uses format: [[TP, FN], [FP, TN]]
# Example values can be customized per slide
slide_confusions = {
    6:  [[271, 49], [7, 147]],
    7:  [[284, 36], [6, 148]],
    8:  [[284, 36], [8, 146]],
    9:  [[297, 23], [13, 141]],
    10: [[304, 16], [15, 139]],
    12: [[50, 19], [1, 37]],
    13: [[61, 8], [0, 38]],
    14: [[63, 6], [1, 37]],
}

# === FUNCTION TO PLOT CONFUSION MATRIX ===
def plot_confusion_matrix(matrix, row_labels, col_labels, title, filename):
    """Plots confusion matrix with raw and normalized values and saves as PNG."""
    matrix = np.array(matrix, dtype=float)
    # --- Normalize by row totals (Actual class) ---
    row_sums = matrix.sum(axis=1, keepdims=True)
    normalized = np.divide(matrix, row_sums, out=np.zeros_like(matrix), where=row_sums != 0)

    fig, ax = plt.subplots(figsize=(4, 4))
    cax = ax.matshow(normalized, cmap="Blues", vmin=0, vmax=1)
    plt.title(title, pad=15)
    plt.colorbar(cax, fraction=0.046, pad=0.04)

    # Axis setup
    ax.set_xticks(np.arange(len(col_labels)))
    ax.set_yticks(np.arange(len(row_labels)))
    ax.set_xticklabels(col_labels, rotation=45, ha="right")
    ax.set_yticklabels(row_labels)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    # Annotate each cell with count and percentage
    for (i, j), val in np.ndenumerate(matrix):
        if not np.isnan(val):
            pct = normalized[i, j] * 100
            text = f"{int(val)}\n({pct:.1f}%)"
            ax.text(j, i, text, ha="center", va="center", color="black", fontsize=9)

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"✅ Saved: {filename}")

# === GENERATE MATRICES FOR EACH SLIDE ===
for idx in selected_slides:
    try:
        if idx in slide_confusions:
            matrix = slide_confusions[idx]
            row_labels = ["Actual Positive", "Actual Negative"]
            col_labels = ["Predicted Positive", "Predicted Negative"]
            fname = os.path.join(output_dir, f"confusion_matrix_slide_{idx}.png")
            plot_confusion_matrix(matrix, row_labels, col_labels,
                                  f"Confusion Matrix (Slide {idx})", fname)
        else:
            print(f"⚠️ No matrix data found for slide {idx}, skipped.")
    except Exception as e:
        print(f"❌ Error on slide {idx}: {e}")

print("\n🎉 All 2×2 confusion matrices generated and saved as PNGs.")
