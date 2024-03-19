Vuelo ={
    'Aerolinea': 'Avianca',
    'Vuelo' : 'AV3102',
    'Origen': 'CTG',
    'Destino' : 'MDE',
    'Tipo_Maleta' : ['Cabina', 'Mano', 'Bodega']
}
print('\nDicionario: \n')

for key, value in Vuelo.items():
   
    print(key)
print('\nTipos de maleta \n')
for maleta in Vuelo['Tipo_Maleta']:
    print(maleta)