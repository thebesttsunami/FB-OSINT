#!/bin/python

import facebook

Masukkan API Key dan ID Grup
api_key = "882a8490361da98702bf97a021ddc14d"
id_grup = "TARGET ID"

Buat objek Facebook
graph = facebook.GraphAPI(api_key)

Ambil informasi grup
grup = graph.get_object(id=id_grup, fields='name,description,members')

print(grup)
