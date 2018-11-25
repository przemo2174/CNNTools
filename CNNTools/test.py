from count_labels import LabelsCounter
import numpy as np
import matplotlib.pyplot as plt



x = LabelsCounter()
path = 'C:\Projects\music_notes'

y, z = x.count_labels(path)

labels = {k:v for (k, v) in y.items() if 'quaver' or 'key' in k}
print(labels)

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
labels_ordered['key'] = labels['key']
labels_ordered['quaver_c'] = labels['quaver_c']
labels_ordered['quaver_d'] = labels['quaver_d']
labels_ordered['quaver_ef'] = labels['quaver_ef']
# labels_ordered['crotchet_g'] = labels['crotchet_g']
# labels_ordered['crotchet_a'] = labels['crotchet_a']
# labels_ordered['crotchet_b'] = labels['crotchet_b']
# labels_ordered['crotchet_c5'] = labels['crotchet_c5']

# labels_ordered = {}
# labels_ordered = labels['key']
# labels_ordered['quaver_c'] = 512
# labels_ordered['quaver_d'] = 512
# labels_ordered['quaver_ef'] = 256


x.show_labels_diagram(labels_ordered, title='Klucz wiolinowy (key) i ósemki(ang. quavers)')
