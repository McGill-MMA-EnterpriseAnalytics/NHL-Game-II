# NHL-Game-II
NHL-Game Part 2 (Productionisation) Analysis 🥅 🏒

**Team No.**: Group 2 \
**Team Name**: NHL Pros \
**Product Manager**: Anqi Chen (angelach99) \
**Business Analyst**: Matthew Buttler Ives (matt-buttlerives) \
**Data Engineer**: vaibhav Visual (vvaibhav1), Hadyan Fahreza (hifahreza), Mesaye Bahiru (mesaye3), Rebecca Mukena Yumba (beccarem) \
**Data Scientist**: Louis D'Hulst (louis-dhulst)


## Tutorial
Please notice that there could be documents of previous versions. Here are the links for documents of final versions.
- [Modelling & streaming data](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/tree/main/modeling):
  - Final modelling: [Final_Model_Merged.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/Final_Model_Merged.ipynb)
  - Drift Detection: [DriftDetection.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/DriftDetection.ipynb)
  - Hyperparameter tuning: [Hyperparameter tuning.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/Hyperparameter%20tuning.ipynb)
  - Model performance: [ModelPerformance.ipynb](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/blob/main/modeling/ModelPerformance.ipynb)

- [Productionization](https://github.com/McGill-MMA-EnterpriseAnalytics/NHL-Game-II/tree/main/docker_kubernetes):


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







## Acknowledgements
This project was conducted as part of the final group project for INSY695-076: Enterprise DS & ML In Production II, Winter 2022, with Instructor Fatih Nayebi at Desautels Faculty of Management, McGill University. 
