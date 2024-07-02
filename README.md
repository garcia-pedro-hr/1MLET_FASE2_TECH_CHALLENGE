# 1MLET FASE2 TECH CHALLENGE

## Overview

This API is part of the Machine Learning Engineering FIAP Pos-Tech program. 
It scraps data from the B3 website, transforms it into parquet and uploads to an AWS S3 storage.

## Project Requirements

### Bovespa Batch Pipeline (Mandatory Delivery):
#### Scraping data from the B3 website with D-1 trading session data;
#### Raw data must be ingested into S3 in parquet format with daily partitioning;
#### The bucket must trigger a Lambda, which in turn will call the ETL job in Glue;
#### Lambda can be in any language. It should only start the Glue job;
#### The Glue job must be done in visual mode. This job must contain the following mandatory transformations:
- Numeric grouping, summarization, counting or summation.
- Rename two existing columns in addition to the grouping columns.
- Perform a calculation with date fields. Example, it can be duration, comparison, difference between dates.
#### The refined data in the Glue job must be saved in parquet format, in a folder called refined, partitioned by date and by the name or abbreviation of the trading session stock.
#### The Glue job should automatically catalog the data in the Glue Catalog and create a table in the default database of the Glue Catalog.
#### The data must be available, readable in Athena.
#### Optional build an Athena notebook to build a graphical visualization of the ingested data.

## Contributors (Group 43)
- Bruno Machado Corte Real
- Pedro Henrique Romaoli Garcia
- Rodrigo Santili Sgarioni
