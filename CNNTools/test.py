from count_labels import LabelsCounter
import numpy as np
import matplotlib.pyplot as plt



x = LabelsCounter()
path = 'D:\music_notes'

y, z = x.count_labels(path)

labels = {k:v for (k, v) in y.items() if 'crotchet' in k}



x.show_labels_diagram(labels, title='Crotchets')
