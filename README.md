# encryptLayer
## CN<br>
这是一个完全在本地的基于以太坊账户系统的端对端加密系统。<br>
感谢maiyude2018大佬，完善了公钥查找。<br>
现在已经可以上polygon testnet<br>
再次感谢[maiyude2018](https://github.com/maiyude2018)大佬,感谢[script-money](https://github.com/script-money)
大佬让我接触到这么优秀的大佬<br>
还要感谢box和h神，不断地给我提示，支持我<br>
关于哈希算公钥和其他密码学的原理，我推荐一些文章<br>
[关于公钥的压缩与解压](https://medium.com/asecuritysite-when-bob-met-alice/02-03-or-04-so-what-are-compressed-and-uncompressed-public-keys-6abcb57efeb6)<br>
[公钥的反向计算Go实现](https://medium.com/asecuritysite-when-bob-met-alice/can-we-recover-the-public-key-from-an-ecdsa-signature-7af4b56a8a0f)<br>
[比特币加密算法](https://medium.com/asecuritysite-when-bob-met-alice/satoshi-selected-ecdsa-with-the-secp256k1-curve-and-sha-256-are-other-options-available-9ebc87053272)<br>
[寻找随机素数](https://medium.com/asecuritysite-when-bob-met-alice/how-long-does-it-take-to-find-a-random-prime-number-92fbd484036)<br>
[后量子时代的加密](https://medium.com/asecuritysite-when-bob-met-alice/for-security-in-a-post-quantum-world-and-in-being-a-great-teacher-we-thank-robert-j-mceliece-rip-529585c1be7f)<br>

## EN<br>
This project aims to handle point to point encryption and decryption with EVM account both online and offline.<br>
Special thanks to [maiyude2018](https://github.com/maiyude2018) who helped me alot in 'findPublicKey.py' and
[script-money](https://github.com/script-money) who let me get to know a bunch of Experts in
CS who expertised in Ethereum.

## 如何使用
## How to use<br><br>
首先，安装此工程需要的库并全部升级到最新版本<br>
First, install packages this project depends on and upgrade them to the latest<br>
**[requests](https://github.com/psf/requests)**
**[pycryptodome](https://github.com/Legrandin/pycryptodome)**
**[eth-account](https://github.com/ethereum/eth-account)**
**[eth-keys](https://github.com/ethereum/eth-keys)**
**[eciespy](https://github.com/ecies/py)**
**[web3.py](https://github.com/ethereum/web3.py)**<br><br>



然后克隆或下载这个库源码,打开 'main.py'<br>
Clone or download the source code of this project, and open 'main.py'<br><br>



```python3
msg = mailbox(ifHadAccount=True) #default: False
```
初始化`mailbox`这个类,参数`ifHadAccount`代表你是否愿意使用已有账户,输入`True`会要求
输入**十六进制私钥**，输入`False`将会创建账户<br>
When `mailbox` initiating, parameter `ifHanAcount` is able to be sent in
to represent whether the client would to use their existed account. Once `True`
was sent, the client will be request to input their **private key in Hex**,
and `False` means this programme will generate an account<br><br>



```python3
msg.encrypt(
    senderPublicKey=None,
    senderAddr=0x5568BC7EebC605A88e247769c4acA92d95BC9360, Type='RSA')
```
当使用非对称加密时，请在第三个参数`Type`传入`RSA`，并且传入**在已经支持的网络上有过交易的**
`senderAddr`作为第二个参数，或者**任意地址的公钥**作为第一个参数<br>
当使用对称加密时`Type`参数请传入`ESA`,密钥将会自动生成并保存在本地<br>
**注意**:在这个函数中，请以**字典**形式传入参数<br>
When using asymmetrical encryption, please set the third parameter `Type`
`RSA` and send in an address which **has made tx on supported network** as
parameter `senderAddr` or public key of any account as parameter `publicKey`<br>
When using `Type` as `ESA`, the password will be stored in local computer.<br>
**Attention**:In this method, please send in parameter as **dictionary**.<br><br>



```python3
msg.sign()
```
这个函数将会使用你的私钥对消息签名<br>
This method will sign the massage with your private key<br><br>



```python3
msg.decrypt(senderAddr=0x5568BC7EebC605A88e247769c4acA92d95BC9360, password=None)
```
这个函数将会对签名校验，如果是`senderAddr`发送的信息，将会使用你的私钥解密并输出(`RSA`)或使用保存
在本地的对称密钥解密(`ESA`)。你也可以传入第二个参数`password`对称密钥的**字节串**作为对称密钥<br>
This method will check the sign, if the actual sender is the same as
parameter `senderAddr`, the method will decrypt(`RSA`) or decrypt with local
password(`ESA`). You can also send in the second parameter `password` with
your password in **bytes string**<br><br>



```python3
msg.sendOnline(chainID='80001', permanent=False)
```
这个函数将会把你的签名和加密后的信息作为**字节串**上传,当第二个参数`permanent`为`True`
时,会作为交易的`data`写入区块链,`chainID`代表你选择的链。当第二个参数为`False`时,会上传到
中心化服务器并在7天内删除<br>
This method will upload your signature and encrypted data as **bytes string**.
When the second parameter is `True`, the data bytes will be sent on chain
as `data`, else, these will be uploaded to a centralized server and deleted
with 7 days.<br>