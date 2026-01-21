import pandas as pd
import matplotlib.pyplot as plt

billie_df = pd.read_excel("billie_eilish_streams.xlsx")


bars = plt.bar(billie_df["Album"], billie_df["Streams"],)
bars[0].set_color("black")
bars[1].set_color("red")
bars[2].set_color("darkblue")
bars[3].set_color("yellow")
plt.title("Album")
plt.xlabel("Streams")
plt.title("Most Streamed Billie Eilish Albums (Spotify)")
plt.xlabel("Album")
plt.ylabel("Streams (Billion)")

plt.xticks(rotation=20, ha="right") #this row made by chatgpt
plt.tight_layout()  #this row made by chatgpt
plt.show()
