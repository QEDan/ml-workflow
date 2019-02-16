# ml-workflow
Quckly set up new machine learning projects that make best practices easier.

Successful machine learning requires a long list of best practices from research and software engineering. This project helps to enforce an opinionated but configurable workflow that supports
* Reproducible research
  * Persistance of all trained models
  * Logging of all training details needed for reproductions
  * Docker integration for reproducing exact versions of all software dependencies
* Systematic experimentation with different modeling choices and hyperparameters
* Configurable interfaces to support the needs of different organizations and individuals
  

## Project Ambitions

* New projects are set up with a single command, a la [Cookie Cutter](https://drivendata.github.io/cookiecutter-data-science/)
* Manage training many different configurations by specifying the desired experiments in configuration files
* Automate the submission of dockerized training jobs
* Manage production deployments of trained models
* Integration with [ModelDB](https://github.com/mitdbg/modeldb) so that all experiments are recorded
* Configurable interactions with your organization's computing platform
  * Training job submissions
  * Trained model deployment
  * Database for persisting models and experiment metadata
