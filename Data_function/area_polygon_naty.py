from scipy.io import loadmat
annots = loadmat('lon_lat.mat')
print(annots)
exit()


co = {"type": "Polygon", "coordinates": [
    [(-102.05, 41.0),
     (-102.05, 37.0),
     (-109.05, 37.0),
     (-109.05, 41.0)]]}
lon, lat = zip(*co['coordinates'][0])
from pyproj import Proj
pa = Proj("+proj=aea +lat_1=37.0 +lat_2=41.0 +lat_0=39.0 +lon_0=-106.55")

x, y = pa(lon, lat)
cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
from shapely.geometry import shape
shape(cop).area  # 268952044107.43506