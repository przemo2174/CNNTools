from count_labels import LabelsCounter
import numpy as np
import matplotlib.pyplot as plt



x = LabelsCounter()
path = 'C:\Projects\music_notes'

y, z = x.count_labels(path)

labels = {k:v for (k, v) in y.items() if 'semibreve' in k}

# labels_ordered = {}
# labels_ordered['crotchet_c'] = labels['crotchet_c']
# labels_ordered['crotchet_d'] = labels['crotchet_d']
# labels_ordered['crotchet_e'] = labels['crotchet_e']
# labels_ordered['crotchet_f'] = labels['crotchet_f']
# labels_ordered['crotchet_g'] = labels['crotchet_g']
# labels_ordered['crotchet_a'] = labels['crotchet_a']
# labels_ordered['crotchet_b'] = labels['crotchet_b']
# labels_ordered['crotchet_c5'] = labels['crotchet_c5']

labels_ordered = {}
labels_ordered['semibreve_c'] = labels['semibreve_c']
labels_ordered['semibreve_d'] = labels['semibreve_d']
labels_ordered['semibreve_e'] = labels['semibreve_e']
labels_ordered['semibreve_f'] = labels['semibreve_f']
labels_ordered['semibreve_g'] = labels['semibreve_g']
labels_ordered['semibreve_a'] = labels['semibreve_a']
labels_ordered['semibreve_b'] = labels['semibreve_b']
labels_ordered['semibreve_c5'] = labels['semibreve_c5']

x.show_labels_diagram(labels_ordered, title='Całe nuty (ang. semibreves)')
