import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scienceplots

# 设置全局样式和字体
plt.style.use(["ieee", "science"])
plt.rcParams['font.size'] = 24  # 设置全局字体大小
plt.rcParams['font.family'] = 'serif'  # 设置全局字体族为serif
plt.rcParams['font.serif'] = ['Times New Roman']  # 指定serif字体为Times New Roman
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 读取数据
group1_df = pd.read_csv('/Users/lihonglin/Desktop/system/HEA_OER/due_neighbor/group1_summary.csv')
group2_df = pd.read_csv('/Users/lihonglin/Desktop/system/HEA_OER/due_neighbor/group2_summary.csv')
group3_df = pd.read_csv('/Users/lihonglin/Desktop/system/HEA_OER/due_neighbor/group3_summary.csv')
group4_df = pd.read_csv('/Users/lihonglin/Desktop/system/HEA_OER/due_neighbor/group4_summary.csv')

# 合并数据帧，并添加组列
group1_df['Group'] = 'Group 1'
group2_df['Group'] = 'Group 2'
group3_df['Group'] = 'Group 3'
group4_df['Group'] = 'Group 4'
combined_df = pd.concat([group1_df, group2_df, group3_df, group4_df])

# 为每个组绘制条形图
plt.figure(figsize=(20, 10))
for i, group in enumerate(combined_df['Group'].unique(), 1):
    plt.subplot(2, 2, i)
    data = combined_df[combined_df['Group'] == group]
    sns.barplot(x='Element', y='Average Neighbors', hue='Neighbor Element', data=data)
    #plt.title(f'{group} - Element vs. Average Neighbors')
    plt.tight_layout()

# 绘制箱线图比较各组
plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Average Neighbors', data=combined_df)
plt.title('Distribution of Coordination Numbers Across Groups')
plt.tight_layout()

# 为每个组绘制热图，可视化平均协调数
for group in combined_df['Group'].unique():
    plt.figure(figsize=(10, 8))
    data = combined_df[combined_df['Group'] == group]
    pivot_table = data.pivot_table(index='Element', columns='Neighbor Element', values='Average Neighbors', fill_value=0)
    sns.heatmap(pivot_table, annot=True, cmap='coolwarm')
    #plt.title(f'{group} - Heatmap of Average Neighbors')
    plt.tight_layout()

plt.show()