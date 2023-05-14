import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


'''df = pd.read_csv("../Questions/Answers/releases_smells.csv")
df = df.drop("Unnamed: 0", axis=1)

df = df.rename(columns={
    "comment_ratio": "CR",
    "cyclomatic_complexity": "CC",
    "fanout_external": "Fan-out",
    "fanout_internal": "Fan-in",
    "halstead_bugprop": "HB",
    "halstead_difficulty": "HD",
    "halstead_effort":"HE",
    "halstead_timerequired":"HT",
    "halstead_volume": "HV"
    })

pearsoncorr = df.corr(method='pearson')
sb.set(rc={'figure.figsize': (10, 10)})
sb.heatmap(pearsoncorr,
            xticklabels=pearsoncorr.columns,
            annot=True,
            linewidth=0.5)

plt.savefig('./Correlation-charts/metrics_smells_releases.png')'''

'''df_0_releases = pd.read_csv("../Questions/Answers/without_releases_smells.csv")
df_0_releases = df_0_releases.drop("Unnamed: 0", axis=1)

df_0_releases = df_0_releases.rename(columns={
    "comment_ratio": "CR",
    "cyclomatic_complexity": "CC",
    "fanout_external": "Fan-out",
    "fanout_internal": "Fan-in",
    "halstead_bugprop": "HB",
    "halstead_difficulty": "HD",
    "halstead_effort":"HE",
    "halstead_timerequired":"HT",
    "halstead_volume": "HV"
    })

correlation_0_Releases = df_0_releases.corr(method='pearson')
sb.set(rc={'figure.figsize': (10, 10)})
sb.heatmap(correlation_0_Releases,
            xticklabels=correlation_0_Releases.columns,
            annot=True,
            linewidth=0.5)

plt.savefig('./Correlation-charts/metrics_smells_without_releases.png')'''

'''df_metric_smells = pd.read_csv("../Questions/Answers/metrics_with_smells.csv")
df_metric_smells = df_metric_smells.drop("Unnamed: 0", axis=1)

df_metric_smells = df_metric_smells.rename(columns={
    "comment_ratio": "CR",
    "cyclomatic_complexity": "CC",
    "fanout_external": "Fan-out",
    "fanout_internal": "Fan-in",
    "halstead_bugprop": "HB",
    "halstead_difficulty": "HD",
    "halstead_effort":"HE",
    "halstead_timerequired":"HT",
    "halstead_volume": "HV"
    })

correlation_metrics_smells = df_metric_smells.corr(method='pearson')
sb.set(rc={'figure.figsize': (10, 10)})
sb.heatmap(correlation_metrics_smells,
            xticklabels=correlation_metrics_smells.columns,
            annot=True,
            linewidth=0.5)

plt.savefig('./Correlation-charts/metrics_smells.png')'''


df_metric_without_smells = pd.read_csv("../Questions/Answers/metrics_without_smells.csv")
df_metric_without_smells = df_metric_without_smells.drop("Unnamed: 0", axis=1)

df_metric_without_smells = df_metric_without_smells.rename(columns={
    "comment_ratio": "CR",
    "cyclomatic_complexity": "CC",
    "fanout_external": "Fan-out",
    "fanout_internal": "Fan-in",
    "halstead_bugprop": "HB",
    "halstead_difficulty": "HD",
    "halstead_effort":"HE",
    "halstead_timerequired":"HT",
    "halstead_volume": "HV"
    })

correlation_metrics_without_smells = df_metric_without_smells.corr(method='pearson')
sb.set(rc={'figure.figsize': (10, 10)})
sb.heatmap(correlation_metrics_without_smells,
            xticklabels=correlation_metrics_without_smells.columns,
            annot=True,
            linewidth=0.5)

plt.savefig('./Correlation-charts/metrics_without_smells.png')
