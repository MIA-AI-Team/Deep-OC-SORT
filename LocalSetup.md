# Requirments

## Python version

python 3.10 (Recommended 3.8)

## Virtual Env Setup

_Versions Modifications in Requirements_

```
python3.10 -m venv deepOCenv

source deepOCenv/bin/activate
```

## Requirements Installation

```
cd external/YOLOX/
pip install -r requirements.txt && python setup.py develop

cd ../deep-person-reid/
pip install -r requirements.txt && python setup.py develop

cd ../fast_reid/
pip install -r docs/requirements.txt

cd ../adaptors/
pip install -r requirements.txt
```

# Run

- Added Required weights from the repo
  - SBS for embedding
- Added the dataset to folder data **Note Differs from main README**

# Deep OC Inference

**No Training for detection included**

```
python3 main.py --exp_name $exp --post --cmc_off --aw_off --new_kf_off --grid_off --dataset mot20 --test_dataset --track_thresh 0.4 --aspect_ratio_thresh 0.8
```

```
mv results/trackers/MOT20-val results/trackers/MOT20-test
```

```
python3 external/TrackEval/scripts/run_mot_challenge.py --SPLIT_TO_EVAL test --METRICS HOTA Identity --TRACKERS_TO_EVAL ${exp}\_post --GT_FOLDER results/gt/ --TRACKERS_FOLDER results/trackers/ --BENCHMARK MOT20
```

**For another test**

```
rm -r cache/embeddings/ cache/det_yoloV11_best.pkl results/trackers/
```

Or Change exp_name
