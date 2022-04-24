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
  - Note: this file contains the DeepCheck report output
  - Drift Detection: [DriftDetection.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/DriftDetection.ipynb)
  - Drift Detection (DataBricks version): [DriftDetection_DataBricks](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/DriftDetection_DataBricks.ipynb)
  - Hyperparameter tuning: [Hyperparameter tuning.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/Hyperparameter%20tuning.ipynb)
  - Data Storage: [Games_Storage_Final.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/dd2771a62011ac7ab9d11984bfe1a7f59dff7191/nhl_db/Games_Storage_Final.ipynb)

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
Can we construct a LGBMmodel that can predict which National Hockey League (NHL) hockey team will win a game for the 2022 NHL season? This repository seeks to answer that question. By applying various supervised and unsupervised machine learning models and using public datasets offered through Kaggle, our team has constructed a Light Gradient Boosting classification model which predicts the outcome of a hockey game during a regular season using only statistics captured in the first period of play, provided through an API from SportsRadar, the official analytical partner of the NHL. The purpose of this project is to add our insights to the growing field of sports betting and to challenge ourselves as aspiring professionals in the field of analytics to solve a notoriously difficult prediction problem.

From professional sports teams to passionate fans, data scientists and analytics experts have tried to predict the outcome of sport games using a variety of different approaches, assumptions and statistics. Some analysts use data as far back as 1919 in order to gain further insights. Predicting the outcome of a game is used in a variety of sports such as the NHL, National Football League, (NFL) and the National Basketball Assocation (NBA). While simple in theory, developing a predictive model for classifying which team would win or lose has proven to be one of the most challenging forms of modeling in data science. Often, accuracy levels for this type of modeling range from 50-70%. Even models with accuracy higher than 70% typically only perform well for one season. Currently, one of the best models used in the NHL sports betting field is named Forecheck which offers a 62% accuracy. (If you are interested to read more, here is an article by The Globe And Mail that discusses Forecheck: https://www.theglobeandmail.com/sports/hockey/nhl-predictions-hockey-methodology/article37603494/)

The primary purpose of prediction in the field of sports analytics for those not employed by the NHL is sports betting. Retail sports analysts create predictive model’s that are used to inform their decision making when betting on hockey teams. The objective is to build a model that performs better than “gut instinct” and offers the potential to beat the Sports Bookies (more on that later).

Listed below are some of the most important types of Sports Betting:

Moneyline: Moneyline betting is the most popular form of sports betting in hockey. Simply, players bet on which team will win the game. The reason Moneyline is popular in hockey is due to the frequent low number of goals for most games and is based on the existing likelihood for each team to win. So when you bet on a team to win the game, you are betting on the Moneyline.

Over and Under: This unique form of betting focuses on the total number of goals scored in a game by both teams. Bettors can place bets on if the total amount of goals scored during the game will be above or below a certain threshold set by Sports Bookies. If the total amount is “Over” or “Under” that threshold, a bettor will profit if they managed to pick correctly.

Puck line: Puck line betting focus on the difference between the number of goals scored in a game by both teams, also known as the spread. First each team is assigned as the underdogs or the favourites. This label will give each team either +1.5 points or –1.5 points. A bettor can place a bet on either team, or both, and then that team must either win or lose the game by that certain number of goals (points) for the bettor to profit. This kind of bet is meant to balance the games between stronger and weaker teams.

For each betting method, all teams are given a set of odds that can be expressed as negative or positive indicating if a team is considered the underdog or the favourite. Sportbookies determine these odds, also known as the spreads between teams based on the number of bets taken throughout the week on both teams and will change the point spread to reflect the belief by the bettors on which team will win. They may also artificially change the point spread to maintain interest of bettors on the game.

For our team’s use case, we decided to build a model that would be useful for live/In-game Moneyline betting as this type of Sports betting often tends to be the most dynamic with more bettor participation and whose implications offer the largest contribution to the field of sports betting and predictive modeling. The proof of value (PoV) for our use case revolves around our model’s accuracy. Is the performance of our model valuable to the sports betting community? To answer this question, we must use the measure of value that begins at 52.4%. In the field of sports betting, an accuracy of 52.4% of picking which team will win is needed to breakeven; covering a bettor's losses along with fees associated with the bets. Any bettor whose accuracy is above 52.4% will see some profit. But an accuracy of 53% is where real money can be made and is the benchmark for a model to be considered as a “good model”. Therefore, our team’s objective is to make sure our model’s accuracy either reach’s or goes beyond 53%.




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
Please watch the following video for a live demo on how the SportsRadar API works and how we use data from the API as variables inserted into our model: (https://www.youtube.com/watch?v=xbRfSmEG2io)




## Modelling Result & Dashboards
### Drift detection

Drift detection should be scheduled to run every week. The DataBrticks file takes game data from the main delta lake table. In theory this means drift is being checked for new games every week.

Several drift detection methods are applied in the DriftDetection notebooks and the DBC counterpart.
Firstly, two sample K-S tests are performed that compare the last 50 games (100 rows) with the 100 games before those. The kernel distributions are plotted to compare changes. Results are saved in a delta lake table in the DBC version.
Secondly, a Random Forest learned classifier is used to attempt to detect drift between the new data and reference data. Again, the results are savede in a delta lake table.
Thirdly, summary statistics and other relevant info from the distributions of new and reference datasets are computed and saved in a delta lake table.

For concept drift, the Pearson coefficients are computed between the label and all features for both datasets. This allows us to verify that the causal relationships between features and the label have no changed in significance or side. Again, the results are saved in a delta lake table.

For prediction drift, model accuracy over the last 50 games (100 rows) is compared with two baseline decision rules:
 - predict the team at home wins
 - predict that the team with most goals at the end of the half wins. In case of a tie, predict the team at home wins.
 This is to ensure the model is performing better than a simple decision rule that anyone could create.
 
 A further development of this project would build a trigger in case model accuracy over the last 50 games drop below these baselines. The trigger would run the hyperparameter optimization script, and the best model generated by said script would then be used for subsequent predictions and by the drift detection script. This requires MLFlow integration, however, which we have not done.



### Hyperparameter tuning
Overall, three different hyperparameter tuning methods are used to obtain the optimal hyperparameters: GridSearchCV, Bayesian Optimization, ane HyperOpt with MLFlow. 

For GridSearchCV, it contains learning_rate, max_depth, and num_leaves, and their corresponding optinal values are 0.06, 10, and 31 respectively. The optimal score is 0.661. 

For Bayesian Optimization, there had been problems when implementing to lightGBM model. And since Random Forest performs similarly to lightGBM model, we used Bayesian Optimization to optimize the hyperparameters of Random Forest model. The hyperparameters we used are n_estimators, min_samples_split, and max_features. The optimal values are 0.35, 20.44, and 240 respectively. 

And lastly, we used HyperOpt with MLFlow to the lightGBM models. The optimal loss is 0.64. And the optimal values for the hyperparameters are:
- subsample_for_bin: 200000
- verbose: -1
- boosting_type: gbdt
- keep_training_booster: False
- subsample_freq: 0
- evals_result: None
- colsample_bytree: 1.0
- num_boost_round: 47

The optimal F1 score is 0.6611. 

### Dashboards
We created two dashboards in total. One is for the model prediction, and one is for the streaming data.

For the dashboard of model prediction, we utilized the dashboard function in Databricks to create dashboard directly from our code. You can find the dashboard here [Dashboard_prediction.png](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/Dashboard/Dashboard_prediction.png).

The code for the dashboard with information on daily games and the winner prediction is in the [databricks dashboard folder](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/tree/main/databricks%20dashboard).

## Docker & Kubernetes
We explored another option to productionize the machine learning model using docker and kubernetes. It was implemented in local environment and Google cloud platform (GCP) to check in live environment. Docker file was set up and relevent commands to set up environment, directory, load requirements, scripts, pickle file generated from machine learning script were added to build and run docker container. In local we did in docker desktop and on GCP docker was put on container registry. In local the application which was made with swagger was hosted and simulator and feature for uploading test file and getting prediction was tested. On GCP, kuberneters cluster was configured and docker container was deployed and our application (swagger) was exposed live on internet and was working efficiently. 

Further, on User Interface we tried Streamlit and basic Flask API using Postman along with Swagger API, however went with swagger for testing in GCP as we were able to incorporate GET and POST feature in application and was easy to integrate on Cloud.

On Automation, cron job for triggering pickle file and updating docker which will refresh the simulator/app was built and tested on local environment. full access to tools/softwares instead of trial or community version can help to implement on cloud and live environment. It is a part of future scope.

## Tools/Softwares/Programming Languages used,
Python, Databricks, Databricks delta table, visualization features, Docker desktop, Google cloud platform (container registry, kubernetes, vm instance), GITHub, Streamlit, Swagger, Flask API, Postman, Anaconda




## Acknowledgements
This project was conducted as part of the final group project for INSY695-076: Enterprise DS & ML In Production II, Winter 2022, with Instructor Fatih Nayebi at Desautels Faculty of Management, McGill University. 
