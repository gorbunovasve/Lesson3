import pandas as pd
df = pd.read_csv("student_career_success_dataset.csv")
#print(df.shape)
#print(type(df))
# print(type(df["Gender"]))
# print(df.head(5))
#print(df.info())
#print(df.describe())
#print(df["Gender"].value_counts())
#print(df[["Placement_Status", "Age"]].head(2))
#q = df["Interview_Score"]
#print(q.min(), q.max(), q.max() - q.min())
#print(q.median())
#print(df["Age"].mode().tolist())
#print(df.mode().tolist())
#print(df["Study_Hours_Per_Week"].mean())
#print(df["Study_Hours_Per_Week"].std())
#print(df["Teamwork"].corr(df["Communication_Skills"]))
#print(df["Communication_Skills"].corr(df["Projects_Completed"]))
#df.isna().sum()
#print(df.duplicated().sum())
#df[df.duplicated(keep=False)]
#df = df.drop_duplicates()
#print(df.shape)
#print(df["request_id"].is_unique)
#df["request_date"] = pd.to_datetime(df["request_date"])
#print(df["request_date"].dtype)

#print(df["Starting_Salary_USD"].min(), df["Starting_Salary_USD"].max())            #   0-111000
#print(df["Starting_Salary_USD"].mean(), df["Starting_Salary_USD"].median())        #  68988.16748 83044.5
#q1, q3 = df["Starting_Salary_USD"].quantile([0.25, 0.75]) 
#print(q1, q3)                                                                      #65229.25 96486.25
# висновок що 0 - це викід  можк бути  але це не є так  що доказують данні з інших стовбців    ЦЕ ВІДСУТНІСТЬ ПРАЦІВЛАШТУВАННЯ

#zero_count=(df["Starting_Salary_USD"] == 0). sum()
#print(f"Кількість нулів: {zero_count}")                                            # 10960
#print(df["Starting_Salary_USD"].corr(df["Age"]))                                   # 0.002  
# дуже мала кореляція між віком та ЗП  
#print(df["Starting_Salary_USD"].corr(df["Attendance_Percentage"]))                  # 0.2
# також не велика кореляція між ЗП та відвідуваністю
#print(df["Starting_Salary_USD"].corr(df["Problem_Solving"]))                         # 0.38
# тут вже більш цікаво
#print(df["Starting_Salary_USD"].corr(df["CGPA"]))                                    # 0.29


#print(df["CGPA"].dtype)                                                             # float64
#q = df["CGPA"]
#print(q.min(), q.max(), q.max() - q.min())                                           # 2.0 4.0 2.0   
#print(q.median())                                                                     # 3.11
#print(sum(q))                                                                         # 155302.14 
 


#print(df["University_Year"].str.strip().str.lower().unique().tolist())
#print(df["Starting_Salary_USD"].mean(), df["Starting_Salary_USD"].median())
#q1, q3 = df["Starting_Salary_USD"].quantile([0.25, 0.75])
#print(q1, q3)
#print(df[df["Attendance_Percentage"] == 100])
#print(df[df["Age"] == 30])
#report = pd.DataFrame({"missing": df.isna().sum(),"unique": df.nunique(),"dtype": df.dtypes.astype(str),})
#print(report)
#print(df[df.duplicated(keep=False)])                                                 #

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("student_career_success_dataset.csv")
numeric_df = df.select_dtypes(include=["number"])
if numeric_df.shape[1] < 2:
  print("В таблице недостаточно числовых столбцов для расчета корреляции.")
else:
  target_col = numeric_df.columns[-1]
  correlations = (
      numeric_df.corr()[target_col].drop(target_col).sort_values(ascending=True)
  )
  print(f"=== Корреляция каждого признака со столбцом '{target_col}' ===")
  for col, val in correlations.items():
    print(f"{col}: {val:.4f}")
  plt.figure(figsize=(11, 7))
  bars = plt.barh(
      correlations.index,
      correlations,
      height=0.55,
      color=plt.cm.Blues(correlations * 0.7 + 0.3),
      edgecolor="none",
      alpha=0.9,
  )
  plt.xlim(0, min(1.05, correlations.max() + 0.12))
  plt.axvline(x=0, color="gray", linewidth=1)
  for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.015,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}",
        va="center",
        ha="left",
        fontsize=10,
        fontweight="medium",
        color="#333333",
    )
  plt.title(
      f"Сила корреляции признаков со столбцом '{target_col}'",
      fontsize=14,
      pad=20,
      fontweight="bold",
  )
  plt.xlabel("Коэффициент корреляции", fontsize=11)
  plt.grid(axis="x", linestyle="--", alpha=0.4)
  plt.tight_layout()
  plt.show()