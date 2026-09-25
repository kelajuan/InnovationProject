import pandas as pd
import matplotlib.pyplot as plt


class InnovationProject:
    def __init__(self, project_id: str, title: str, category: str,
                 team_members: list, scores: list):
        self.project_id = project_id
        self.title = title
        self.category = category
        self.team_members = team_members
        self.scores = scores

    def average_score(self) -> float:
        return sum(self.scores) / len(self.scores)

    def clearance_level(self) -> str:
        if self.average_score() > 85:
            return "Level 1 (Override)"
        else:
            return "Level 2 (Standard)"

    def commercialization_potential(self) -> str:
        average = self.average_score()

        if average > 85:
            return "High"
        elif average >= 70:
            return "Medium"
        else:
            return "Low"


# Innovation project data
project_list = [
    InnovationProject("P001", "Smart Technology", "Tekno",
                      ["Ali"], [92]),
    InnovationProject("P002", "Neuro Assistant", "Neuro",
                      ["Alicia"], [88]),
    InnovationProject("P003", "Digital Innovation", "Tekno",
                      ["Khai"], [75]),
    InnovationProject("P004", "Invisible Security", "Inviso",
                      ["Rudy"], [85]),
    InnovationProject("P005", "Combat Technology", "Kombat",
                      ["Moon"], [68])
]


# Functional features
scores = list(map(lambda p: p.average_score(), project_list))

avg_score = sum(scores) / len(scores)

level_1_projects = list(
    filter(lambda p: p.clearance_level() == "Level 1 (Override)", project_list)
)

top_projects = list(
    filter(lambda p: p.average_score() >= 80, project_list)
)

print(f"Average Team Score: {avg_score:.2f}")
print("Level 1 Projects:", [p.title for p in level_1_projects])
print("Top-Tier Projects:", [p.title for p in top_projects])


# Pandas Tactical Table
data = {
    "Project ID": [p.project_id for p in project_list],
    "Title": [p.title for p in project_list],
    "Category": [p.category for p in project_list],
    "Team Members": [", ".join(p.team_members) for p in project_list],
    "Average Score": [p.average_score() for p in project_list],
    "Clearance Level": [p.clearance_level() for p in project_list],
    "Commercialization Potential":
        [p.commercialization_potential() for p in project_list]
}

df = pd.DataFrame(data)

print("\n-- MATA Tactical Summary Table --")
print(df.to_string(index=False))


# Matplotlib Bar Chart
plt.bar(df["Title"], df["Average Score"])

plt.title("Innovation Project Scores")
plt.xlabel("Project")
plt.ylabel("Average Score")

plt.ylim(0, 100)
plt.xticks(rotation=20)

plt.tight_layout()
plt.show()