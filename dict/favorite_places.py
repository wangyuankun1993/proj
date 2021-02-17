favorite_places = {
    'wangyuankun':['jiuzhaigou','mogaoku','yueyaquan'],
    'liuchunyu':['liming','qinhuangdao','tianchi'],
    'liming':['changcheng'],
}
for name, places in favorite_places.items():
    if len(places) <=1 :
        print("\n" + name.title() + "'s favorite place is:")
    else:
        print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())