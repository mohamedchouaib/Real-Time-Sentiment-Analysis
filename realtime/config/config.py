config = {
    
    "kafka":{
        "sasl.username": "N5NULYYGI4EHRFYS",
        "sasl.password": "8f1aV0I8eIeyBXlsXXXDaXWjYVhaZHlTLKvc0P3Bpeh3GWNKv6avli3XpmCZVXga",
        "bootstrap.servers": "pkc-12576z.us-west2.gcp.confluent.cloud:9092",
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms':'PLAIN',
        'session.timeout.ms':50000
    },
    "schema_registry": {
        "url": "https://psrc-12dd33.us-west2.gcp.confluent.cloud",
        "basic.auth.user.info": "KVPBP3LNDKITGOVW:teAjuWmYwXY7ZkJMbM/OzVKaE61N90NztGlykGdW1cuJfQrd0qSV6HPjQXTN0IJe" #username:password of the schema registry 
    }
}