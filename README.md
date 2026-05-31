# Custom ELT Pipeline with Docker, PostgreSQL, Python, and dbt

## Portfolio Highlights

- Built an end-to-end ELT pipeline using Docker, PostgreSQL, Python, and dbt
- Automated database migration between PostgreSQL instances
- Implemented modular dbt models and data quality tests
- Developed reproducible containerized development environment
- Applied analytics engineering best practices

## Overview

This project demonstrates an end-to-end ELT (Extract, Load, Transform) pipeline built using Docker, PostgreSQL, Python, and dbt.

The pipeline extracts data from a source PostgreSQL database, loads it into a destination PostgreSQL database, and then transforms the data using dbt models to create analytics-ready tables.

## Architecture

```text
Source PostgreSQL
        │
        ▼
   Python ELT
   (pg_dump/psql)
        │
        ▼
Destination PostgreSQL
        │
        ▼
      dbt
        │
        ▼
Analytics Models
```

## Tech Stack

* Docker & Docker Compose
* PostgreSQL
* Python
* dbt (Data Build Tool)
* DBeaver (Database Exploration)

## Project Structure

```text
pipeline/
│
├── docker-compose.yml
│
├── source_db_init/
│   └── init.sql
│
├── elt/
│   ├── Dockerfile
│   └── elt_script.py
│
└── custom_postgres/
    ├── dbt_project.yml
    ├── models/
    ├── macros/
    └── tests/
```

## ELT Process

### Extract

Data is extracted from the source PostgreSQL database using:

```bash
pg_dump
```

### Load

The extracted data is loaded into the destination PostgreSQL database using:

```bash
psql
```

### Transform

dbt models transform raw tables into analytics-ready datasets.

## dbt Models

### films

Contains movie information including:

* Film ID
* Title
* Release Date
* Price
* Rating
* User Rating

### actors

Contains actor information.

### film_actors

Maps films to actors.

### film_ratings

Enriched analytical model containing:

* Film details
* Rating categories
* Associated actors

## Data Quality Tests

dbt tests are implemented to ensure:

* Unique primary keys
* Non-null critical fields
* Consistent data quality across models

## How to Run

### Start the Pipeline

```bash
docker compose up
```

### Rebuild Containers

```bash
docker compose up --build
```

### Run dbt Models

```bash
dbt run
```

### Execute Tests

```bash
dbt test
```

## Example Output

The final model `film_ratings` provides a consolidated view of movie information, actor details, and rating classifications suitable for analytics and reporting.

## Key Learnings

This project helped strengthen practical skills in:

* Docker containerization
* PostgreSQL administration
* Python automation
* ELT pipeline design
* dbt transformations
* Data modeling and testing
* SQL development and debugging

## Future Improvements

* Incremental dbt models
* Data lineage documentation
* CI/CD integration with GitHub Actions
* Data warehouse deployment
* Automated monitoring and alerting

```

