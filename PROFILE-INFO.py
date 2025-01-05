#!/bin/python

import facebook

Masukkan API Key dan ID Profil
api_key = "882a8490361da98702bf97a021ddc14d"
id_profil = "100087020197894"

Buat objek Facebook
graph = facebook.GraphAPI(api_key)

Ambil informasi profil
profil = graph.get_object(id=id_profil, fields='name,email,birthday,location')

print(profil)
