import koordinates

client = koordinates.Client(
    'wsp-au.koordinates.com', '1dc9b869d1894cc2a6700b54ab677380')

# for layer in client.layers.list():   print(layer.id)
layer = client.layers.get(115992)
print(layer.title)
