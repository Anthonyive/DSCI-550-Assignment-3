# Building Visual Apps to Explore Fake Scientific People and Literature using Data Science: Creating Data Insights

[Quick Access to Instructions](docs/DSCI550_Spring2021_HW_WEBDATAVIZ_PHISHING.pdf) | [Quick Access to Report](#) 

## Prerequisite

1. Python virtual environment has been set up using `pipenv`. You need `pipenv` installed ([learn more about installation and usage](https://pipenv-fork.readthedocs.io/en/latest/)).
2. There are several other packages/tools you may want to use along the way. You should check out the [instruction about this assignment](docs/DSCI550_Spring2021_HW_WEBDATAVIZ_PHISHING.pdf).

## Usage

1. **[Task 1]** Take your TSV dataset and convert the data to JSON to use in D3.
  - We are using modified version of etllib for Python 3.7: https://github.com/Anthonyive/etllib.git
  - Example usage:
  ```bash
  $ tsvtojson -t additional_features.tsv -c cols.txt -o "Email" -s 1.0 -v -j assignment-2.json
  ```
2. **[Task 2]** We are using Flask to build our website. To run locally:
    1. Set Flask app in your virtual environment:
      ```bash
      $ export FLASK_APP=app.py
      ```
    2. (Optional) Set Flask environment as development:
      ```bash
      $ export FLASK_ENV=development
      ```
    3. Run Flask
      ```bash
      $ flask run
      ```
    4. Click the localhost link it provides.

## About

This is the assignment 3 from DSCI 550 Spring 2021 at USC Viterbi School of Engineering. This repo is collaborated by a group of six.

Team members: Zixi Jiang, Peizhen Li, Xiaoyu Wang, Xiuwen Zhang, Yuchen Zhang, Nat Zheng
