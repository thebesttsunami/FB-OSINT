#!/bin/python

import facebook

api_key = "882a8490361da98702bf97a021ddc14d"
id_profil = "100087020197894"
graph = facebook.GraphAPI(api_key)
profil = graph.get_object(id=id_profil, fields='name,email,birthday,location')
print(profil)
