# Currency Client REST API Testing Framework

This framework was set up to test Currency client https://exchangeratesapi.io/documentation/

## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Make](https://discussions.apple.com/thread/1404907)
- [Python 3.7 and up](https://www.python.org/downloads/release/python-370/)

## Setup

1. Open a terminal

2. Change to your favorite local directory (i.e. `cd /opt`)

3. Clone the repository

```bash
git clone <git_repo>
```
4. Change to the project root directory

```bash
cd /opt/basic-restapi-testfwk
```

5. Create a new file, name it `secrets.ini` and add the following contents

```bash
APP_URL=http://api.exchangeratesapi.io
ACCESS_KEY=ACCESS_KEY
BASE=BASE_CURRENCY
SYMBOLS=CURRENCY_SYMBOL
```

5. Start development environment

```bash
make dev
```

> This command will remove any existing `restapi_testfwk` containers, build a new `test/restapi_testfwk` image, start a container, mount local code under `/opt/restapi_testfwk` and provide a `/bin/bash` terminal.

6. Run the tests
```
 pytest tests/
 ```
