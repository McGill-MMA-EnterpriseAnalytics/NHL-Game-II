# NHL-Game-II
NHL-Game Part 2 (Productionisation) Analysis 🥅 🏒

**Team No.**: Group 2 \
**Team Name**: NHL Pros \
**Product Manager**: Anqi Chen (angelach99) \
**Business Analyst**: Matthew Buttler Ives (matt-buttlerives) \
**Data Engineer**: Vaibhav Vishal (vvaibhav11), Hadyan Fahreza (hifahreza), Mesaye Bahiru (mesaye3), Rebecca Mukena Yumba (beccarem) \
**Data Scientist**: Louis D'Hulst (louis-dhulst)


## Tutorial
Please notice that there could be documents of previous versions. Here are the links for documents of final versions.
- [Modelling & streaming data](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/tree/main/modeling):
  - Final modelling: [Final_Model_Merged.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/Final_Model_Merged.ipynb)
  - Drift Detection: [DriftDetection.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/DriftDetection.ipynb)
  - Hyperparameter tuning: [Hyperparameter tuning.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/Hyperparameter%20tuning.ipynb)
  - Model performance: [ModelPerformance.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/ModelPerformance.ipynb)

- [Productionization](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/tree/main/docker_kubernetes):
  - Main Files (used for docker container, kubernetes cluster deployed on GCP)
    - Dockerfile
    - Classifier.pkl
    - requirements.txt (containes relevant packages needed to run ML model and Front end application)
    - swagger_api.py (Front end application)
  - Reference files
    - Betting_Model.ipynb (sample of model script used to build pickle file)
    - flask_api.py (Basic user interface built using postman in local)
    - streamlit_api.py (Another front end application built using streamlit in local)
    - train.csv (sample of train data)
    - test.csv (sample of test data)
    - docker_kubernetes_gcp_cmds.txt (commands used to setup application using docker and kubernetes in GCP cloud shell)
    - nhl_app_arch_v1.pptx
  
  Note: In GCP swagger was used and streamlit and flask/postman user interface were tested in local.

## Overview and Business implication



## Static data 

The static data source (from part 1 of this project) is from: 
[NHL Kaggle Dataset](https://www.kaggle.com/martinellis/nhl-game-data?select=game.csv )

Here are the definitions of features used for this project:
- "won": Did the team win the game?
- "Shots": Number of shots
- "Shots_Against": Number of shots of opponent team
- "Goals": Number of goals
- "Goals_against": Number of goals of opponent team
- "Takeaways": Number of Takeaways
- "Takeaways_against": Number of Takeaways of opponent team
- "Hits": Number of hits
- "Hits_against": Number of hits of opponent team
- "Blocked shots": Number of blocks shots
- "Blocked shots against": Number of blocks shots of opponent team
- "Giveaways": Number of Giveaways
- "Giveaways_against": Number of Giveaways of opponent team
- "Missed shots": Number of missed shots
- "Missed shots_against": Number of missed shots of opponent team
- "Penalties": Number of penalties
- "Penalties_against": Number of penalties of opponent team
- "#Won faceoffs": Number of won faceoffs
- "#Lost faceoffs": Number of lost faceoffs
- "HoA_away": Is the team away?
- "HoA_home": Is the team at home?

The static dataset is [Period_1_Game_Stats_Final_ModelReady(April-10th-2022).csv](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/Period_1_Game_Stats_Final_ModelReady(April-10th-2022).csv).


## Streaming real-time data from Sportsradar





## Modelling Result & Dashboards
### Drift detection


### Model performance tracker


### Hyperparameter tuning


### Dashboards





## Docker & Kubernetes
We explored another option to productionize the machine learning model using docker and kubernetes. It was implemented in local environment and Google cloud platform (GCP) to check in live environment. Docker file was set up and relevent commands to set up environment, directory, load requirements, scripts, pickle file generated from machine learning script were added to build and run docker container. In local we did in docker desktop and on GCP docker was put on container registry. In local the application which was made with swagger was hosted and simulator and feature for uploading test file and getting prediction was tested. On GCP, kuberneters cluster was configured and docker container was deployed and our application (swagger) was exposed live on internet and was working efficiently. 

Further, on User Interface we tried Streamlit and basic Flask API using Postman along with Swagger API, however went with swagger for testing in GCP as we were able to incorporate GET and POST feature in application and was easy to integrate on Cloud.

On Autiomation, cron job for triggering pickle file and updating docker which will refresh the simulator/app was built and tested on local environment. full access to tools/softwares instead of trial or community version can help to implement on cloud and live environment. It is a part of future scope.

## Tools/Softwares/Programming Languages used,
Python, Databricks, Databricks delta lake/visualization features, Docker desktop, Google cloud platform (container registry, kubernetes, vm instance), GITHub, Streamlit, Swagger, Flask API, Postman, Anaconda




## Acknowledgements
This project was conducted as part of the final group project for INSY695-076: Enterprise DS & ML In Production II, Winter 2022, with Instructor Fatih Nayebi at Desautels Faculty of Management, McGill University. 
