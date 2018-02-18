import folium
import geocoder
import twitter2 as tw

def creat_map():
    """
    This function creates a map
    """
    maps= folium.Map()
    fg = folium.FeatureGroup()
    return maps,fg


def transformed_geo(info):
    g = geocoder.google(info)
    return g.latlng

def draw(data, fg):
    """

    This function marks the points where movies were shot in a particular year

    """

    for d in data:
        try:
            print(d['location'])
            info = d['name'] + " "+ d['id']
            fg.add_child(folium.Marker(location=d['location'], popup=d['name']))
        except TypeError:
            print('eror')
            pass
    return fg


def main():
    tw.make_js()
    req = tw.make_recuest()
    data = tw.make_data(req)

    for d in data:
        d['location'] = transformed_geo(d['location'])

    map, fg = creat_map()
    fg = draw(data, fg)
    map.add_child(fg)
    map.save("Map.html")
