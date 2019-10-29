# block-producer-swap-bot

  * [Getting started](#getting-started)
    * [Requirements](#getting-started-requirements)
      * [Ubuntu 16.04 & 18.04](#ubuntu-1604--1804)
  * [Block producers](#block-producers)
    * [Configuration file](#configuration-file)
    * [Usage](#usage)
  * [Development](#development)
  
## Getting started

<h3 id="getting-started-requirements">Requirements</h4>

#### Ubuntu 16.04 & 18.04

Download remprotocol_0.1.0-swap-bot.tar.gz

```bash
$ sudo wget https://github.com/Remmeauth/remprotocol/releases/download/0.1.0/remprotocol_0.1.0-swap-bot.tar.gz
```

Unpack to block_producer_swap_bot directory

```bash
$ mkdir block_producer_swap_bot
$ tar -C ./block_producer_swap_bot -xvf remprotocol_0.1.0-swap-bot.tar.gz
$ cd block-producer-swap-bot
```

Install dependencies for Ubuntu18.04 with the following command:

```bash
$ sudo ./scripts/ubuntu18.04_install.sh
```

Install dependencies for Ubuntu16.04 with the following command

```bash
$ sudo ./scripts/ubuntu16.04_install.sh
```

## Block producers

### Configuration file

Open configuration file.

```bash
$ nano ./config.ini
```

Paste into the config file following content:

```
[NODES]
remnode=127.0.0.1:8888
eth-provider=wss://ropsten.infura.io/ws/v3/<your infura id>
[REM]
swap-permission=<permission to authorize init swap actions>@active
swap-private-key=<private key to sign init swap actions>
```

Replace remnode, eth-provider, swap-permission, swap-private-key with your remnode host and port, a link to Ethereum node with websocket connection, your account and private key to authorize init swap actions (for example your block producer account name and private key for signing blocks).
[Tutorial for creating Infura API key](https://ethereumico.io/knowledge-base/infura-api-key-guide/)

Save config file with Ctrl+O.
Press Enter.
Close config file with Ctrl+X.

### Usage

To start approving swaps run the following command

```bash
$ sudo ./scripts/run.sh >> swap.log 2>&1 &
```

## Development

Manually init particular swap transaction
```bash
$ remcli --url http://127.0.0.1:8888 push action rem.swap init '[ "producer111a", "30a9479fc792d3219aba23440235a4a7e4ab32e7ff86a08d878778c5076d206b", "EOS7oNmmxo8yh8gmYLUGNCwNAFfLmrMxtmrzmFPG29CpGm5Bq4FGC", "20.0000 REM", "9fb8a18ff402680b47387ae0f4e38229ec64f098", "eth", "2019-07-25T17:51:47" ]' -p producer111a@active
```