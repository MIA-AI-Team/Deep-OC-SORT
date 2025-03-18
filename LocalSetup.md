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
python3 main.py --exp_name $exp --post --cmc_off --aw_off --new_kf_off --grid_off --dataset mot20 --test_dataset --track_thresh 0.4 --aspect_ratio_thresh 0.8 --conf 0.1 --nms 0.7
```

Params aw_off, new_kf_off, grid_off, track_thresh -> For The Tracker

```
mv results/trackers/MOT20-val results/trackers/MOT20-test
```

```
python3 external/TrackEval/scripts/run_mot_challenge.py --SPLIT_TO_EVAL test --METRICS HOTA --TRACKERS_TO_EVAL ${exp}\_post --GT_FOLDER results/gt/ --TRACKERS_FOLDER results/trackers/ --BENCHMARK MOT20
```

**For another test**

```
rm -r cache/embeddings/ cache/det_yoloV11_best.pkl results/trackers/
```

Or Change exp_name

## Experiments

### YoloX Experiments

#### Params

Confidence 0.1, NMS 0.7, Class Agnostics False, CMC OFF

#### Results

YOLOX 17 Embedding 17 - 63.415 -  
YOLOX 17 Embedding 20 - 63.808 -  
YOLOX 20 Embedding 17 - 74.941 - 69.667  
YOLOX 20 Embedding 20 - 75.456 - 70.739

### YoloV11 Experiments

YOLOV11 (No Test det) Embedding 17 45.459 - 43.952  
YOLOV11 (No Test det) Embedding 20 46.608 - 46.006

Confidence 0.7

YOLOV11 (No Test det) Embedding 17 45.459 - 43.952  
YOLOV11 (No Test det) Embedding 20 49.777 - 49.295

YOLOV11 (No Test det) Embedding 20 50.259 - 50.26 (track_thresh 0.6)
