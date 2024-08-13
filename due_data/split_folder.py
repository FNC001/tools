import os
import shutil
from math import ceil
from tqdm import tqdm

source_dir = "/Users/lihonglin/Desktop/system/abo3/work/7e-1w/str/with_fa"
files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
num_splits = 4

files_per_split = ceil(len(files) / num_splits)

for I in range(num_splits):
    split_dir = os.path.join(source_dir, f'split_{I+1}')
    os.makedirs(split_dir, exist_ok=True)

    start_index = I * files_per_split
    end_index = min((I + 1) * files_per_split, len(files))

    for f in tqdm(files[start_index:end_index], desc=f'Moving files to split_{I+1}'):
        shutil.move(os.path.join(source_dir, f), os.path.join(split_dir, f))

print("All files have been distributed into the specified splits.")