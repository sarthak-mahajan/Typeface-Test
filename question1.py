# %%
import pandas as pd

# %% [markdown]
# ## Question 1

# %%
prim_df = pd.read_csv("Payment Data  - Primary ID.csv")

# %%
sec_df = pd.read_csv("Payment Data  - Secondary ID.csv")

# %%
sec_df[prim_df['Primary ID'] == 14]

# %%
dates = list(prim_df[prim_df['Primary ID'] == 14]['Payment Date'])

# %%
date_dict = {}

for idx, i in enumerate(dates):
    if i[:4] not in date_dict:
        date_dict[i[:4]] = [idx]
    else:
        date_dict[i[:4]].append(idx)

# %%
sums = {}
for key in date_dict:
    sums[key] = prim_df[prim_df['Primary ID'] == 14].iloc[date_dict[key]].Amount.sum()

# %%
sums

# %%
sec_df[sec_df['Total Payment 2020'] == sums['2020']]

# %%
sec_df[sec_df['Total Payment 2021'] == sums['2021']]

# %%
sec_df[sec_df['Total Payment 2022'] == sums['2022']]

# %%
# ANSWER 1241

# %% [markdown]
# ## Question 2

# %%
sec_df[sec_df['Secondary ID'] == 1253]

# %%
group_by_df = prim_df[prim_df['Payment Date'].str.startswith('2020')].groupby('Primary ID').Amount.sum()

# %%
group_by_df[group_by_df == 325050]

# %%
# ANSWER 2342

# %% [markdown]
# ## Question 3

# %%
(prim_df['Primary ID'] % 100 == 5).sum()

# %%
(prim_df['Amount'] % 100 == 5).sum()

# %%
# ANSWER:

# FOR PRIMARY ID: 34
# FOR AMOUNT: 0


