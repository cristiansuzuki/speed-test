import speedtest

teste = speedtest.Speedtest()

print("Carregando lista de servidores...")
teste.get_servers() # Pega a lista de servidores disponíveis
print("Escolhendo o melhor servidor disponível...")
melhor_server = teste.get_best_server() # Pega o melhor servidor

print(f"Encontrado: {melhor_server['host']} localizado em {melhor_server['country']}")
 
print("Realizando teste de download...")
download = teste.download()

print("Realizando teste de upload...")
upload = teste.upload()

ping = teste.results.ping

print(f"Velocidade de download: {download / 1024 / 1024:.2f} Mb/s")
print(f"Velocidade de upload: {upload / 1024 / 1024:.2f} Mb/s")
print(f"Ping: {ping:.2f} ms")