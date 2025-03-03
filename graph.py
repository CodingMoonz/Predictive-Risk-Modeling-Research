import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:/Users/caomi/Downloads/archive/Loan.csv')  # Path to your dataset

# Set the style for Seaborn
sns.set(style="whitegrid")

# 1. Histogram of Credit Score
plt.figure(figsize=(8, 6))
sns.histplot(df['CreditScore'], bins=30, kde=True, color='skyblue', line_kws={'color': 'red'})
plt.title('Credit Score Distribution')
plt.xlabel('Credit Score')
plt.ylabel('Frequency')
plt.show()

# 2. Box Plot of Payment History
plt.figure(figsize=(8, 6))
sns.boxplot(x='PaymentHistory', data=df, palette='muted')
plt.title('Payment History Distribution')
plt.xlabel('Payment History')
plt.ylabel('Frequency')
plt.show()

# 3. Box Plot of Debt-to-Income Ratio
plt.figure(figsize=(8, 6))
sns.boxplot(x='DebtToIncomeRatio', data=df, palette='muted')
plt.title('Debt-to-Income Ratio Distribution')
plt.xlabel('Debt-to-Income Ratio')
plt.ylabel('Frequency')
plt.show()

# 4. Histogram of Annual Income
plt.figure(figsize=(8, 6))
sns.histplot(df['AnnualIncome'], bins=30, kde=True, color='green', line_kws={'color': 'red'})
plt.title('Annual Income Distribution')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')
plt.show()

# 5. Count Plot for Employment Status
plt.figure(figsize=(8, 6))
sns.countplot(x='EmploymentStatus', data=df, palette='Blues')
plt.title('Employment Status Distribution')
plt.xlabel('Employment Status')
plt.ylabel('Count')
plt.show()

# 6. Pair Plot to visualize relationships between Credit Score, Debt-to-Income Ratio, and Annual Income
sns.pairplot(df[['CreditScore', 'DebtToIncomeRatio', 'AnnualIncome']], hue='EmploymentStatus', palette='coolwarm')
plt.show()

# 7. Correlation Heatmap for selected features
plt.figure(figsize=(8, 6))
corr_matrix = df[['CreditScore', 'PaymentHistory', 'DebtToIncomeRatio', 'AnnualIncome']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Selected Features')
plt.show()
