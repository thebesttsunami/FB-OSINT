import facebook
import requests
from bs4 import BeautifulSoup

Masukkan API Key dan ID Profil Target
api_key = "882a8490361da98702bf97a021ddc14d"
id_profil = "100087020197894"

Buat objek Facebook
graph = facebook.GraphAPI(api_key)

Mengumpulkan Informasi Profil
def get_profil_info():
    profil = graph.get_object(id=id_profil, fields='name,birthday,location,hometown,age_range')
    return profil

Mengumpulkan Daftar Teman
def get_teman():
    teman = graph.get_connections(id=id_profil, connection_name='friends')
    return teman

Mengumpulkan Grup yang Diikuti
def get_grup():
    grup = graph.get_connections(id=id_profil, connection_name='groups')
    return grup

Mengumpulkan Informasi Akun
def get_akun_info():
    akun = graph.get_object(id=id_profil, fields='created_time')
    return akun

Menjalankan Kode
if __name__ == "__main__":
    profil_info = get_profil_info()
    teman = get_teman()
    grup = get_grup()
    akun_info = get_akun_info()

    print("Informasi Profil:")
    print(f"Nama: {profil_info['name']}")
    print(f"Tanggal Lahir: {profil_info['birthday']}")
    print(f"Tempat Tinggal: {profil_info['location']['name']}")
    print(f"Asal: {profil_info['hometown']['name']}")
    print(f"Usia: {profil_info['age_range']}")
    print(f"Akun Dibuat: {akun_info['created_time']}")

    print("\nDaftar Teman:")
    for t in teman['data']:
        print(t['name'])

    print("\nGrup yang Diikuti:")
    for g in grup['data']:
        print(g['name'])
