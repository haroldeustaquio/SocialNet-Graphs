# NodePropagate

## Overview



**Content**
- [Synthetic Data](#synthetic-data)
- [Context 1: Analysis of User Interactions in a Graph](#context-1-analysis-of-user-interactions-in-a-graph)
- [Context 2: Analysis of Bipartite Graph: Tweets and Hashtags](#context-2-analysis-of-bipartite-graph-tweets-and-hashtags)
- [Mathematical Foundation](#mathematical-foundation)

---


<div align="center">
    <img src="https://st.depositphotos.com/3367263/59407/i/450/depositphotos_594077234-stock-photo-image-connections-hexagons-black-background.jpg" alt="Description of Image" />
</div>


## Synthetic Data

The script generates and exports three synthetic tables that simulate data from a social network. Below is a description of each created table and its structure.

### Tweets Table

This table contains information about the tweets published by users. Each tweet has a unique identifier, information about the creator, the content category, associated hashtags, and the publication date.


| Field       | Description                                                                                   |
|-------------|-----------------------------------------------------------------------------------------------|
| tweet_id    | Unique identifier of the tweet (starts at 1000 and increments sequentially).                  |
| creator     | User who created the tweet, randomly selected from the list of users.                         |
| category    | Category of the tweet (e.g., Politics, Economy, Sports, Culture, Technology, Health, World).  |
| hashtags    | String of associated hashtags, separated by commas. Can contain 0, 1, or 2 random hashtags.   |
| tweet_date  | Date and time of tweet publication in `YYYY-MM-DD HH:MM:SS` format (last 60 days).            |

---

### Users Table

This table simulates the information of registered users on the social network, with details about their profile and activity.

| Field                 | Description                                                                                       |
|-----------------------|---------------------------------------------------------------------------------------------------|
| user_id               | Unique identifier of the user (e.g., `User_1`, `User_2`, ...).                                    |
| username              | Username, same as the `user_id`.                                                                  |
| account_creation_date | Account creation date, randomly generated in the last 5 years.                                    |
| age                   | Age of the user, a random number between 18 and 60.                                               |
| country               | Country of origin of the user (e.g., USA, Spain, Mexico, Argentina, Colombia, Chile, Peru).       |
| bio                   | Brief biography of the user, randomly selected from a list of descriptions.                       |
| followers_count       | Number of followers of the user, randomly generated between 50 and 10,000.                        |

### Interactions Table

This table stores the interactions that users perform on tweets, such as comments, likes, reposts, or mentions. Each interaction includes references to both the tweet and the users involved.

| Field            | Description                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| interaction_id   | Unique identifier of the interaction (starts at 2000 and increments sequentially).                              |
| tweet_id         | Identifier of the tweet related to the interaction.                                                             |
| user_from        | User who performs the interaction.                                                                              |
| user_to          | User who receives the interaction. Can be empty, depending on the type of interaction.                          |
| interaction_type | Type of interaction, which can be `comment`, `like`, `repost`, or `mention`.                                    |
| interaction_date | Date and time the interaction was performed, in `YYYY-MM-DD HH:MM:SS` format (last 30 days).                    |


---


## Context 1: Analysis of User Interactions in a Graph

In this scenario, a directed graph is created to represent the interactions between users of a social network. Each node in the graph corresponds to a user, while the edges indicate interactions between them, such as comments, likes, reposts, and mentions. The goal is to analyze the network structure, obtain important metrics, and visualize the distribution and direction of interactions.

**Graph Type:**  
- Directed Graph (DiGraph).

**Processed Data:**  
- **Nodes:** Users with attributes (username, creation date, age, country, bio, followers).  
- **Edges:** Interactions (comments, likes, reposts, mentions) between users.

**Key Results:**  

| Metric                          | Description                                                      |
|---------------------------------|------------------------------------------------------------------|
| Total users (nodes)             | Total number of users in the network.                            |
| Total interactions (edges)      | Total number of connections between users.                       |
| Top 3 In-degree                 | Users who receive the most interactions.                         |
| Top 3 Out-degree                | Users who initiate the most interactions.                        |
| Top 3 Betweenness Centrality    | Users who act as critical bridges in the network.                |

**Adjacency Matrix:** Generated to numerically visualize the connectivity between users.  

**Graph Visualization:**  

<div align="center">
    <img src="https://github.com/user-attachments/assets/fd7aa595-1e20-44c9-b5b7-331bd67d2770" alt="Graph Visualization" />
</div>


---

## Context 2: Analysis of Bipartite Graph: Tweets and Hashtags

A bipartite graph is created that connects tweets with the hashtags they use. Each node represents a tweet or a hashtag, and an edge indicates that a tweet uses a hashtag. This allows identifying which tweets use the most hashtags and which hashtags are the most popular.

**Graph Type:**  
- Undirected Graph (Graph) with a bipartite structure.

**Processed Data:**  
- **Nodes:**  
    - Tweets (type "tweet", positioned in one set).  
    - Hashtags (type "hashtag", positioned in the other set).  
- **Edges:**  
    - Connection between a tweet and the hashtags it uses, with the relation "uses".

**Key Results:**  

| Metric                                    | Description                                                            |
|-------------------------------------------|------------------------------------------------------------------------|
| Top 3 Tweets by number of hashtags used   | Tweets with the highest number of connections to hashtags.             |
| Top 3 Hashtags by popularity               | Most used hashtags (highest number of tweets using them).              |

**Bipartite Graph Visualization:**  

<div align="center">
    <img src="https://github.com/user-attachments/assets/533bac25-dd9e-415f-b6dd-258720c2b602" alt="Bipartite Graph Visualization" />
</div>

---

## Mathematical Foundation

