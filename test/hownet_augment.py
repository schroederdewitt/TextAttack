# from textattack.augmentation import EmbeddingAugmenter
from textattack.transformations.word_swaps.word_swap_hownet import WordSwapHowNet
from textattack.augmentation import Augmenter
transformation = WordSwapHowNet(max_candidates=1)
augmenter = Augmenter(transformation=transformation)
s = 'What I cannot create, I do not understand.'
for i in range(100):
    out = augmenter.augment(s)
    print(out)