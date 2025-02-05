# Importing Libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# Loading Data
df_users = pd.read_csv("data/users.csv")
df_tweets = pd.read_csv("data/tweets.csv")
df_interactions = pd.read_csv("data/interactions.csv")


# Graph Construction
B = nx.Graph()

for idx, row in df_tweets.iterrows():
    tweet_id = row["tweet_id"]
    B.add_node(tweet_id, bipartite=0, type="tweet")
    
    hashtags_str = row["hashtags"]
    if pd.notna(hashtags_str) and hashtags_str.strip() != "":
        hashtags = [ht.strip() for ht in hashtags_str.split(",") if ht.strip() != ""]
        for ht in hashtags:
            B.add_node(ht, bipartite=1, type="hashtag")
            B.add_edge(tweet_id, ht, relation="uses")


# General Insights

tweet_nodes = {n for n, d in B.nodes(data=True) if d["type"] == "tweet"}
hashtag_nodes = {n for n, d in B.nodes(data=True) if d["type"] == "hashtag"}

degree_tweets = {node: B.degree(node) for node in tweet_nodes}
degree_hashtags = {node: B.degree(node) for node in hashtag_nodes}

print("Top 3 tweets by number of hashtags used:")
for tweet, deg in sorted(degree_tweets.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"Tweet {tweet}: {deg} connections")

print("\nTop 3 hashtags by popularity (number of tweets using it):")
for ht, deg in sorted(degree_hashtags.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"Hashtag {ht}: {deg} connections")


# Graph Visualization

tweet_nodes = {n for n, d in B.nodes(data=True) if d['bipartite'] == 0}
hashtag_nodes = set(B) - tweet_nodes

pos = {}
for i, n in enumerate(tweet_nodes):
    pos[n] = (1, i)
for i, n in enumerate(hashtag_nodes):
    pos[n] = (2, i)

plt.figure(figsize=(12, 8))
nx.draw(B, pos, with_labels=True,
        node_color=[ "lightblue" if B.nodes[n]["type"]=="tweet" else "lightgreen" for n in B.nodes()],
        node_size=800, font_size=8, font_color="black", alpha=1, edge_color="gray", width=0.8, style="dashed")
edge_labels = nx.get_edge_attributes(B, "relation")
nx.draw_networkx_edge_labels(B, pos, edge_labels=edge_labels, font_color="red", font_size=8)
plt.title("Bipartite Graph: Tweets and Hashtags")
plt.axis("off")
plt.show()