
# Project Description

This is a sample project designed to illustrate a machine learning process, covering data exploration, model development, and deployment.
In this scenario your team has been asked to build a classifier that can identify office buildings, given some building attributes. You are provided a labelled training dataset that contains records of buildings with various features and labels as to whether they are an office building or not. You are also given a test dataset of records with features but no labels, which you should label with your classifier (office: TRUE or FALSE).

Your task is to:

1.	Review the baseline model the company intern developed in a Jupyter notebook. Advise on what to do next and why. How must the current baseline model be improved? You are invited to begin to develop and test a new model, but at a minimum provide specific feedback on what should be done to improve the model’s performance based on your expertise and your understanding of the dataset. The use of graphs for data analysis or result analysis can help support your feedback.
2.	Expose your new model through an HTTP API endpoint that can serve model predictions through a POST request (this can be either point or batch predictions). You should provide an example request so that it can be evaluated.
3.	Imagine that an improved version of the model must be placed into production in 3-weeks. Outline an ML work plan. Consider established DevOps practices such as testing, versioning, continuous delivery and monitoring. What do you tackle in the first phase of the project? Why? What information do you need to be successful? Describe further steps in README.md with a short summary.

___
## Work Plan

### Week 1: Project Kick-off

- Understanding the desired outcomes and success criteria.
- Documentation of business needs and expectations.
- Ensuring availability and quality of training and testing data.
- Validating data consistency and completeness.
- Regular communication and collaboration with key stakeholders.
- Clear understanding of the overall timeline and milestones.
- Configuring development, testing, and production environments.
- Implementing version control for code and model artifacts.

### Week 2: Model Improvement and Testing

- Collaboration on feature engineering and model improvements.
- Allow data scientists to conduct experiments and iterate on model enhancements.
- Provide an explanation of the chosen model(s) and the training process.
- Provide an overview of the testing and validation strategies employed. 
- Develop unit tests and conduct integration tests.
- Incorporating model interpretability checks by data scientists.

### Week 3: DevOps Integration

- Set up CI pipelines for automated testing on code changes.
- Ensure CI includes testing for both code and model artifacts.
- Configure CD pipelines for automated deployment to staging environments.
- Implement blue-green deployments for seamless updates.
- Implement logging for model predictions, errors, and system behavior.
- Collaborate on defining relevant metrics for model performance monitoring.
- Establish version control for the model and datasets.
- Collaborate on versioning for feature engineering scripts.
- Document DevOps processes and practices, involving both ML engineers and data scientists.
___
# How to Run the Code

To run the FastAPI web application, install dependencies and execute the script below:
```bash
pip install -r requirements.txt
cd app
uvicorn main:app
```

To run the notebooks and reproduce their results, execute the scripts below to install required dependencies:
```bash
cd notebooks
pip install -r requirements.txt
```







