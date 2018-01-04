import cv2
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from colorthief import ColorThief

data = pd.read_csv('data.data', header = None, delimiter=' *, *', engine='python')
features = data.values[:,:3]
target = data.values[:,3]
clf = GaussianNB()
clf.fit(features, target)

#Image name hard coded.
color_thief = ColorThief('1.jpg')
palette = color_thief.get_palette(6)

ans = clf.predict(palette)

for i in range(len(ans)):
	print("%s %s"%(palette[i], ans[i]))

img=cv2.imread('1.jpg')
cv2.imshow('img',img)
cv2.waitKey(0)
