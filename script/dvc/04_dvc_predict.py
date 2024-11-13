# %%
from app.core.config import config

# %%
logger = config.logger
logger.info("predict")
clf = config.params.model_fit_storage.load()

iris_test = config.params.test_storage.load()

predictor_df = iris_test.drop("target", axis=1)
target_vec = iris_test["target"]

predict_df = iris_test.assign(prediction=clf.predict(predictor_df))

config.params.pred_storage.save(predict_df)

# # %%
# import matplotlib.pyplot as plt
# from sklearn.svm import SVC
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import RocCurveDisplay
# from sklearn.datasets import load_wine
# from sklearn.model_selection import train_test_split

# ax = plt.gca()
# rfc_disp = RocCurveDisplay.from_estimator(
#     clf, predictor_df, target_vec, ax=ax, alpha=0.8
# )
# # svc_disp.plot(ax=ax, alpha=0.8)
# plt.show()
# %%
