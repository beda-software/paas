# My little cozy PaaS  

This project is an implementation as MVP of PaaS system which [bro.agency](bro.agency) use in  production. 
It is built with ansible and docker.  
The core of the system is Service Discovery based on [etcd](https://coreos.com/etcd/) and [Registrator](http://gliderlabs.com/registrator/latest/)  
Load balancer based on [confd](http://www.confd.io/) and [nginx](http://nginx.org/), provided as [docker container](https://github.com/Brogency/balancer).  

## How check it
### Requirements
`ansible 2.0.2.0`
### Launch steps
Clone the repo `git clone https://github.com/Brogency/paas.git`  
Launch a server with Ubutnu 14.04
Configure ansible playbook 
```diff
diff --git a/inventory b/inventory
index 5e72880..a1462cb 100644
--- a/inventory
+++ b/inventory
@@ -1,4 +1,5 @@
 [bro-host]
+place you server ip addres
 ;place your server ip addres here
 
 [bro-host:vars]
diff --git a/server.yml b/server.yml
index 85a8e2c..57d6e55 100644
--- a/server.yml
+++ b/server.yml
@@ -13,5 +13,6 @@
       use_build: true,
       repository: 'https://github.com/Brogency/hello-world.git',
-      #server_name: 'place your server ip addres here',
+      server_name: 'place you server ip addres',
       tags: ['hello-world']
    }
```  
Launch the playbook `ansible-playbook -i inventory server.yml`

## More information
You could know more information in Russian about it at [RootConf2016](http://rootconf.ru/2016/abstracts/2050)
