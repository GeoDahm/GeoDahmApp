import folium
import pandas


data =pandas.read_csv('Volcanoes.txt')
lat =list(data["LAT"])
lon =list(data["LON"])
ele = list(data["ELEV"])

def colour_marker(elevation):
    if elevation < 1000:
        return 'red',70
    elif 1000 <= elevation < 3000:
        return 'orange',26
    else:
        return 'yellow',9


map = folium.Map(location=[38.58, -99.08], zoom_start=6, tiles='OpenStreetMap')

f = folium.FeatureGroup(name="danger zones")
for lt, ln, el in zip(lat, lon, ele):
    #this line adds a marker that enables he user to pinpoint the values.
    #f.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color=colour_marker(el))))
    color_it,rad=colour_marker(el)
    f.add_child(folium.CircleMarker(location=[lt, ln], popup=el, radius=rad, fill_color=color_it, color='grey', fill_opacity=0.5))

fg = folium.FeatureGroup(name="area under observation")

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x:{'fillColor':'yellow'
if x['properties']['POP2005'] <10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'

}))

map.add_child(f)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map3.html")