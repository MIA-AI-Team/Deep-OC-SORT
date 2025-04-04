"""Generic detector."""
import os
import pickle

import torch

from external.adaptors import yolox_adaptor
from external.adaptors import yolo11_adaptor

class Detector(torch.nn.Module):
    K_MODELS = {"yolox", "yoloV11"}

    def __init__(self, model_type, path, dataset, conf_thresh=0.1, iou=0.7):
        super().__init__()
        if model_type not in self.K_MODELS:
            raise RuntimeError(f"{model_type} detector not supported")

        self.model_type = model_type
        self.path = path
        self.dataset = dataset
        self.conf = conf_thresh
        self.iou = iou
        self.model = None

        os.makedirs("./cache", exist_ok=True)
        self.cache_path = os.path.join(
            "./cache", f"det_{os.path.basename(path).split('.')[0]}.pkl"
        )
        self.cache = {}
        if os.path.exists(self.cache_path):
            with open(self.cache_path, "rb") as fp:
                self.cache = pickle.load(fp)
        else:
            self.initialize_model()

    def initialize_model(self):
        """Wait until needed."""
        if self.model_type == "yolox":
            self.model = yolox_adaptor.get_model(self.path, self.dataset)
        elif self.model_type == "yoloV11":
            self.model = yolo11_adaptor.get_model(conf=self.conf, iou_thresh=self.iou, weights_path=self.path)

    def forward(self, batch, tag=None):
        if tag in self.cache:
            return self.cache[tag]
        if self.model is None:
            self.initialize_model()

        with torch.no_grad():
            batch = batch.half()
            output = self.model(batch)
        if output is not None:
            self.cache[tag] = output.cpu()

        return output

    def dump_cache(self):
        with open(self.cache_path, "wb") as fp:
            pickle.dump(self.cache, fp)
