# Importing Libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# Loading Data

df_users = pd.read_csv("data/users.csv")
df_tweets = pd.read_csv("data/tweets.csv")
df_interactions = pd.read_csv("data/interactions.csv")


# Graph Construction

G = nx.DiGraph()

for idx, row in df_users.iterrows():
    G.add_node(row["user_id"], 
               username=row["username"],
               account_creation_date=row["account_creation_date"],
               age=row["age"],
               country=row["country"],
               bio=row["bio"],
               followers_count=row["followers_count"])
    
def add_interaction(source, target, interaction_type):
    if G.has_edge(source, target):
        G[source][target]['weight'] += 1
        G[source][target]['types'].append(interaction_type)
    else:
        G.add_edge(source, target, weight=1, types=[interaction_type])


for idx, row in df_interactions.iterrows():
    tipo = row["interaction_type"]
    actor = row["user_from"]

    if tipo in ["comment", "like", "repost"]:
        tweet_id = row["tweet_id"]
        tweet_row = df_tweets[df_tweets["tweet_id"] == tweet_id]
        if not tweet_row.empty:
            tweet_creator = tweet_row.iloc[0]["creator"]
            add_interaction(actor, tweet_creator, tipo)
    elif tipo == "mention":
        destinatario = row["user_to"]
        add_interaction(actor, destinatario, tipo)


# General Insights

print("Total number of users (nodes):", G.number_of_nodes())
print("Total number of interactions (edges):", G.number_of_edges())


in_degrees = sorted(G.in_degree(), key=lambda x: x[1], reverse=True)
print("Top 3 users who receive the most interactions (in-degree):")
for user, deg in in_degrees[:3]:
    print(f"{user}: {deg}")


out_degrees = sorted(G.out_degree(), key=lambda x: x[1], reverse=True)
print("Top 3 users who initiate the most interactions (out-degree):")
for user, deg in out_degrees[:3]:
    print(f"{user}: {deg}")

betweenness = nx.betweenness_centrality(G)
top_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nTop 3 users by betweenness centrality:")
for user, cent in top_betweenness:
    print(f"{user}: {cent:.4f}")


# Adjacency Matrix
sorted_nodes = sorted(G.nodes())
adj_matrix = nx.to_numpy_array(G, nodelist=sorted_nodes)

df_adj = pd.DataFrame(adj_matrix, index=sorted_nodes, columns=sorted_nodes)
print("\nAdjacency Matrix:")
print(df_adj)


# Graph Visualization

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="yellow", alpha=0.6)
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=12, edge_color="blue", width=1, alpha=0.4, connectionstyle="arc3,rad=0.1", min_source_margin=15, min_target_margin=15, style="dashed")
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

plt.title("User Interaction Graph")
plt.axis("off")
plt.show()




































