# pipeline-ende

Open SSL based Encryptor/Decryptor for Jenkins pipeline hook

Better credential management in pipileine based automation trigger. Such as auto applying the DB script or running batch tash with some credentials. 


* Installation:

    ```./install.sh```


* Uses:
    * Encrypt:
        
        ``./ende.sh --encr <some-credentails>``
        
    * Decrypt:
        
        ``./ende.sh --decr <decrypted-key>``