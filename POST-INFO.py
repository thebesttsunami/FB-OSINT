import facebook

Masukkan API Key dan ID Profil
api_key = "882a8490361da98702bf97a021ddc14d"
id_profil = "// ID TARGET //"

Buat objek Facebook
graph = facebook.GraphAPI(api_key)

Ambil postingan
postingan = graph.get_connections(id=id_profil, connection_name='posts')

print(postingan)
