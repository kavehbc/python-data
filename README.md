# Python Data Exploration

In this repository, I am exploring different aspects of working with data in order to optimize the overal performance.

The following projects are available:

- **data-serialization**: This investigates different serializtion formats in `Pandas` and `PyArrow` such as `CSV`, `JSON`, `Parquet`, etc. This repository compare the `saving time`, `loading time`, `file size` and `conversion time`. This analysis can help us to make a better decision next time we need to save/load our data.

- **pandas-speedup**: Data manipulation is a time/resource expensive part in most of Data Science projects. Here I am exploring the different scenarios of maipulating pandas dataframe as fast as possible. I have covered multiple methods such as using simple loop, apply function, parallel computations, etc.

- **parallel-api**: Do you need to call an API in batch? Either it is for load testing, batch testing, batch inference, or data data collection, I have a solution here for you.

## Requirements

Each project in its own folder has its own `environment.yml` file. But if you need a conda environment with all the required libraries for all the projects in this repo, you can refer to the `environment.yml` file in the root folder.

The following command creates a conda environment using the given `environment.yml`.

    conda env create -f environment.yml
    
## Config File

There is a `config-sample.toml` which should be renamed into `config.toml` first and edited with the correct parameters.

### Plotly Chart-Studio

If you need to publish the plotly charts online, you should add the credentials in the `config.toml` file.

```toml
[plotly]
username=plotly_username
api_key=plotly_api_key
```

For more information, you can check [Plotly Chart-Studio](https://chart-studio.plotly.com/).

## Developer(s)

Kaveh Bakhtiyari - [Website](http://bakhtiyari.com) | [Medium](https://medium.com/@bakhtiyari)
  | [LinkedIn](https://www.linkedin.com/in/bakhtiyari) | [GitHub](https://github.com/kavehbc)

## Contribution

Feel free to join the open-source community and contribute to this repository.
