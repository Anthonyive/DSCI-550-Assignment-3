# Building Visual Apps to Explore Fake Scientific People and Literature using Data Science: Creating Data Insights

[Quick Access to Instructions](docs/DSCI550_Spring2021_HW_WEBDATAVIZ_PHISHING.pdf) | [Quick Access to Report](TEAM_GINGERDONKEY_DATAVIS.pdf) 

## Prerequisite

1. Python virtual environment has been set up using `pipenv`. You need `pipenv` installed ([learn more about installation and usage](https://pipenv-fork.readthedocs.io/en/latest/)).
2. There are several other packages/tools you may want to use along the way. You should check out the [instruction about this assignment](docs/DSCI550_Spring2021_HW_WEBDATAVIZ_PHISHING.pdf).

## Usage

1. **[Task 1]** Take your TSV dataset and convert the data to JSON to use in D3.

- We are using modified version of etllib for Python 3.7: [https://github.com/Anthonyive/etllib.git](https://github.com/Anthonyive/etllib.git)
- Example usage:

 ```bash
 tsvtojson -t additional_features.tsv -c cols.txt -o "Email" -s 1.0 -v -j assignment-2.json
 ```

2. **[Task 2]**

- Data preparation: Run notebooks in [notebooks directory](notebooks/) except for visualization 4. For visualization 4, there's a Python script called `vis4conversion.py` in the [src directory](src/) and run it in the root directory.
- We are using Flask to build our website. To run locally:

  1. Set Flask app in your virtual environment:

   ```bash
   export FLASK_APP=app.py
   ```

  2. (Optional) Set Flask environment as development:

   ```bash
   export FLASK_ENV=development
   ```

  3. Run Flask

   ```bash
   flask run
   ```

  4. Click the localhost link it provides.
 
 3. **[Task 6]**
 
 - We have already parsed the fradulent emails data from assignment 1 and assignment 2 in Apache Solr and created the location graph in GeoParser. The generated graphs are included in the [GeoParser Directory](GeoParser/).
 - If you would love to recreate the graphs, follow the steps in [GeoParser Repo](https://github.com/nasa-jpl-memex/GeoParser/wiki/Sample:-COVID19-publication-data-parsing), and switch the example of Covid19 to one of the folders we created [here](GeoParser/).

## About

This is the assignment 3 from DSCI 550 Spring 2021 at USC Viterbi School of Engineering. This repo is collaborated by a group of six.

Team members: Zixi Jiang, Peizhen Li, Xiaoyu Wang, Xiuwen Zhang, Yuchen Zhang, Nat Zheng
