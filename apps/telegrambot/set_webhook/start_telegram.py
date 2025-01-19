from pyngrok import ngrok

https_tunnel = ngrok.connect(bind_tls=True)

print(https_tunnel)