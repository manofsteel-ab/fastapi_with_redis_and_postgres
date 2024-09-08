## Setup podman

**1. Install brew**

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

**2. Install podman**

`brew install podman`

**3. Setup podman machine**

`podman machine init`

**4. Start podman**

`podman machine start`

**5. Check machine status**

`podman machine list`

**6. Podman version**

`podman --version`

**7. To use podman-compose**

`brew install podman-compose`



## Running the Setup with Podman

**1. Build the Containers:**
podman-compose up --build

**2. Run Tests:**
podman-compose exec fastapi-app pytest

**3. Stop and Remove Containers::**
podman-compose down


### TODO - Need to add more details