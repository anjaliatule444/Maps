from geopy.geocoders import ArcGIS
import folium
import pandas as pd

#def add_child_demo()
# x=Location.geocode('Aurangabad')
# map=folium.Map(location=[x.latitude,x.longitude])
# map.add_child(folium.Marker(location=[x.latitude,x.longitude],popup='Abad MH',icon=folium.Icon(color='green')))
# map.save('Abad.html')

def Tiger_Reserves():
    Location=ArcGIS()
    data=pd.read_excel('TigerReservesInIndia.xlsx')
    data['Address_data']=data['Name of Tiger']+" "+data['State']
    data['Geocode']=data['Address_data'].apply(Location.geocode)
    data['latitude']=list(map(lambda x :x.latitude,data['Geocode']))
    data['longitude']=list(map(lambda x :x.longitude,data['Geocode']))
    latitude_list=list(data['latitude'])
    longitude_list=list(data['longitude'])
    Address_data_list=list(data['Address_data'])
    fg=folium.FeatureGroup(name='TigerReserve')
    mapp = folium.Map(location=[latitude_list[0], longitude_list[0]])
    for i in range(len(latitude_list)):
        fg.add_child(folium.Marker(location=[latitude_list[i],longitude_list[i]],popup=Address_data_list[i],icon=folium.Icon(color='green')))
    mapp.add_child(fg)
    mapp.save('map.html')

