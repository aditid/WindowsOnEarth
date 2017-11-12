import os
from pathlib import Path

cur_path = os.path.dirname(__file__)
paths = list(Path('..', 'tf_files', 'images').glob('**/*.jpg'))

for x in paths:
    with open(os.path.join(cur_path, '..', 'tf_files', 'multi_label_images', x.stem + x.suffix + '.txt'), 'w') as f:
        f.write(x.parent.stem)
