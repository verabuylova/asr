from torch_audiomentations import PeakNormalization
from torch import Tensor, nn


class PeakNormalize(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._aug = PeakNormalization(*args, **kwargs)

    def __call__(self, data: Tensor):
        x = data.unsqueeze(1)
        return self._aug(x).squeeze(1)