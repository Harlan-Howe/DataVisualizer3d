import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a list of 2D polygons at different Z values
patches = []
for z in np.linspace(0, 10, 5):
    verts = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) + np.random.rand(4, 2) * 0.2
    patches.append(Polygon(verts))

# Create a PatchCollection and add it to the 3D axes
collection = PatchCollection(patches, facecolor='cyan', alpha=0.5)
ax.add_collection3d(collection, zs=np.linspace(0, 10, 5), zdir='z')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()