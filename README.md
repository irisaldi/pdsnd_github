### Date created

11 November 2023

### Divvy Bikeshare Stat

Crunch some stats out of [**<ins>Divvy Bikeshare</ins>**](https://en.wikipedia.org/wiki/Divvy) data.

### Description

**Divvy Bikeshare Stat** is a statistic project based on the *Divvy bicycle sharing system* data in Chicago, New York City, and Washington. For future business development, it is necessary to be able to run analysis on data of these bikes and its users. On this regard was this project initiated.

The statistic part is made available by utilizing [**<ins>Python</ins>**](https://www.python.org) programming language and its powerful data manipulation tool [**<ins>pandas</ins>**](https://pandas.pydata.org) and [**<ins>numpy</ins>**](https://numpy.org).

>   :memo: **IMPORTANT NOTE**: At the moment, our available data spans from January to June 2017. :memo:

#### Getting Started

>   :warning: **WARNING**: This guideline hasn't been tested in MacOs/Linux. :warning:

1. **Download/Clone Repository**
   
   To run the code, you are free to download this repository into your local machine.
   
   If you're familiar with [**<ins>Git</ins>**](https://git-scm.com/download), please clone our repository:

    > ```bash
    > $ git clone https://github.com/irisaldi/pdsnd_github.git
    > ```

2. **Install Python and Create Python Environment**
   
   You're going to need Python 3 and we highly recommend to install it from the most recent package and environment management [**<ins>Miniconda3</ins>**](https://docs.conda.io/projects/miniconda/en/latest) release. After a successfully installation of Miniconda3, create a conda environment by using `environment.yml` file we provided.

    Open your command prompt and run this command:

    > ```bash
    > $ conda env create -f environment.yml
    > ```

3. **Execute `bikeshare.py`**
   
   Before you execute the `bikeshare.py` code, you need to activate the environment you created in step 2. If you haven't signed a new name for your environment, then this following command should do:

    > ```bash
    > $ conda activate nano_env
    > ```

    Now, please run this code from whatever your current directory is:

    > ```bash
    > $ python <your-path-to-pdsnd_github-directory>/bikeshare.py
    > ```

    Once it executed, follow the instruction prompted on your screen.

    ![Run `bikeshare.py`](/assets/images/bikeshare.gif)

### Files used

The code requires these three files stored in your local repository:

+ `chicago.csv`
+ `new_york_city.csv`
+ `washington.csv`

Get the files [**here**](https://www.example.com/divvy-files)

### [License](/LICENSE)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Credits

+ Many thanks for [@wiraDKP](https://github.com/wiraDKP) for most of the inspirations.
+ Thanks to [@lukas-h](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba) for providing *Markdown License Badges*.
