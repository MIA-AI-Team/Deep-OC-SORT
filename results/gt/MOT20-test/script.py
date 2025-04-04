"""Process the GT data into validation data."""
# Ranges of the validation data
import pdb

files = {
    "MOT20-01/gt/gt.txt": (216, 429),
}


for f_name, val_range in files.items():
    new_data = []
    with open(f_name, "r") as fp:
        for line in fp:
            tokens = line.split(",")
            if int(tokens[0]) < val_range[0]:
                continue
            tokens[0] = str(int(tokens[0]) - val_range[0] + 1)
            new_data.append(",".join(tokens))
    with open(f_name, "w") as fp:
        fp.writelines(new_data)
