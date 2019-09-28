import folium
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
#Adding children as a feature group
fg = folium.FeatureGroup(name="My Map")

for coodinates in [[38.2,-99.1],[39.2,-97.1]]:
    fg.add_child(folium.Marker(location=coodinates,popup="Hi i am a Marker",icon=folium.Icon(color='green')))
map.add_child(fg)

#Add objects to the map
#map.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi i am a Marker",icon=folium.Icon(color='green')))
map.save("Map1.html")