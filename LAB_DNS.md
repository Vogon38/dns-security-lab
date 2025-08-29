# Lab DNS com BIND para Testes

Este guia ensina a criar um servidor DNS local com BIND para testar transferências de zona (`AXFR`).

## Passos rápidos

1. Instale o BIND:
```bash
sudo apt update
sudo apt install bind9
```
2. Crie a pasta de zonas:
```bash
sudo mkdir -p /etc/bind/zones
```
3. Configure a zona (edite /etc/bind/named.conf.local):

```conf

zone "test.local" {
    type master;
    file "/etc/bind/zones/test.local.db";
    allow-transfer { any; };  # Permite transferir para testes
};
```
4. Crie o arquivo /etc/bind/zones/test.local.db com:

```zone

$TTL 604800
@ IN SOA ns.test.local. admin.test.local. (1 604800 86400 2419200 604800)
@ IN NS ns.test.local.
ns IN A 127.0.0.1
@ IN A 127.0.0.1
```
5. Reinicie o BIND:
```bash
sudo systemctl restart bind9
```
6. Teste a transferência:
```bash
dig AXFR test.local @127.0.0.1
