# %% use the correct working directory
# import os
# import sys
# from typing import List


# %%
import json
import math
import os
from pathlib import Path
import pickle
import sys

import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn import tree
from dvclive import Live
from app.core.config import config


# %%
logger = config.logger
logger.info("print classification report")
# live = Live("evaluation")
pred_df = config.params.pred_storage.load()

classification_report = metrics.classification_report(
    pred_df["target"], pred_df["prediction"]
)
print(classification_report)

# %%
logger.info("prepare data")
labels = pred_df["target"]
predictions = pred_df["prediction"]


# # %%
# # Use dvclive to log a few simple plots ...
# live.log_plot("roc", labels, predictions)
# # live.log("avg_prec", metrics.average_precision_score(labels, predictions))
# # live.log("roc_auc", metrics.roc_auc_score(labels, predictions))

# # ... but actually it can be done with dumping data points into a file:
# # ROC has a drop_intermediate arg that reduces the number of points.
# # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve.
# # PRC lacks this arg, so we manually reduce to 1000 points as a rough estimate.
# precision, recall, prc_thresholds = metrics.precision_recall_curve(
#     pos_label=positive_level_idx, probas_pred=valid_score, y_true=valid_y_dummies
# )
# nth_point = math.ceil(len(prc_thresholds) / 1000)
# prc_points = list(zip(precision, recall, prc_thresholds))[::nth_point]
# prc_file = os.path.join("evaluation", "plots", "precision_recall.csv")
# prc_df = pd.DataFrame(prc_points, columns=["precision", "recall", "threshold"])
# prc_df.to_csv(prc_file)


# # %%
# roc_auc = metrics.roc_auc_score(y_true=valid_y_dummies, y_score=valid_score_for_level_1)
# fpr, tpr, threshold = metrics.roc_curve(
#     y_true=valid_y_dummies, y_score=valid_score, pos_label=positive_level_idx
# )
# roc_df = pd.DataFrame({"fpr": fpr, "tpr": tpr, "threshold": threshold,}).query(
#     "threshold <= 1"
# )  # avoid border useless values

# roc_df.to_csv("evaluation/plots/roc_data.csv")

# %%
logger.info("print confusion matrix")
# confusion matrix, normalized per row (real)
cm = metrics.confusion_matrix(labels, predictions, normalize="true")
cm_df = pd.DataFrame(cm)

config.params.metric_storage.save(
    {
        "true_negative": cm[0, 0],
        "true_positive": cm[1, 1],
        "false_negative": cm[1, 0],
        "false_positive": cm[0, 1],
    }
)

# %%
with Live(save_dvc_exp=True) as live:
    live.log_metric("true_negative", cm[0, 0])
    live.log_metric("true_positive", cm[1, 1])
    live.log_metric("false_negative", cm[1, 0])
    live.log_metric("false_positive", cm[0, 1])

    # live.log_sklearn_plot("confusion_matrix", [0, 0, 1, 1], [0, 1, 0, 1])

    # live.log_artifact("data/dvc/03_train/model_fit.pkl", type="model", name="model_fit")

# # # ... confusion matrix plot
# # live.log_plot("confusion_matrix", labels.squeeze(), predictions_by_class.argmax(-1))

# # # ... and finally, we can dump an image, it's also supported:
# # fig, axes = plt.subplots(dpi=100)
# # fig.subplots_adjust(bottom=0.2, top=0.95)
# # importances = model.feature_importances_
# # forest_importances = pd.Series(importances, index=feature_names).nlargest(n=30)
# # axes.set_ylabel("Mean decrease in impurity")
# # forest_importances.plot.bar(ax=axes)
# # fig.savefig(os.path.join("evaluation", "importance.png"))

# # %%


# %%
