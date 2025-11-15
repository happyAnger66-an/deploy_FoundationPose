from torch.utils.data import DataLoader, Dataset

import numpy as np
import dataclasses

from learning.models.score_network import ScoreNetMultiPair
from learning.models.refine_network import RefineNet
from datareader import YcbineoatReader


class FoundationPoseCalibrationData(Dataset):
    def __init__(self, data_dir,
                 model,
                 calib_size=100):
        self.data_dir = data_dir
        self.calib_size = min(calib_size, len(self.lerobot_dataset))
        self.model = model
        self.reader = YcbineoatReader(
            video_dir=data_dir, shorter_side=None, zfar=np.inf)

        self._hooks = []
        self._inputs = []

    def __len__(self):
        return self.calib_size

    def __getitem__(self, idx):
        # Use sequential indices directly

        def hook_input(m, args, kwargs):
            #            print(f'hook module input: {type(m)} args:{args} kwargs: {kwargs}')
            self._inputs.append(kwargs)

        self._inputs.clear()
        self._hooks = hook_module_inputs(self.model,
                                         hook_input, ScoreNetMultiPair)

        action_chunk = self.policy.infer(example)["actions"]

#        print(f' hooks {len(self._hooks)}')
        for hook in self._hooks:
            hook.remove()

#        print(f' left hooks {len(self._hooks)} return inputs {self._inputs}')
        return self._inputs
