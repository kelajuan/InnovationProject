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

    InnovationProject(
        "A001",
        "AI Smart Assistant",
        "AI",
        ["Ali", "Aina"],
        [92, 94, 90, 93]
    ),

    InnovationProject(
        "A002",
        "AI Learning System",
        "AI",
        ["Alicia", "Adam"],
        [87, 88, 85, 89]
    ),

    InnovationProject(
        "A003",
        "AI Health Assistant",
        "AI",
        ["Khai", "Sara"],
        [78, 80, 76, 79]
    ),

    InnovationProject(
        "C001",
        "Cyber Defence System",
        "CyberSecurity",
        ["Rudy", "Daniel"],
        [95, 96, 94, 97]
    ),

    InnovationProject(
        "C002",
        "Secure Data Platform",
        "CyberSecurity",
        ["Maya", "John"],
        [89, 91, 88, 90]
    ),

    InnovationProject(
        "C003",
        "Network Security Tool",
        "CyberSecurity",
        ["Farah", "Amir"],
        [83, 85, 81, 84]
    ),

    InnovationProject(
        "I001",
        "Smart Home System",
        "IoT",
        ["Lina", "Hakim"],
        [91, 93, 90, 92]
    ),

    InnovationProject(
        "I002",
        "Smart Agriculture System",
        "IoT",
        ["Nadia", "Irfan"],
        [86, 88, 84, 87]
    ),

    InnovationProject(
        "I003",
        "IoT Monitoring Device",
        "IoT",
        ["Sofia", "Ray"],
        [82, 84, 81, 83, 80]
    ),

    InnovationProject(
        "W001",
        "Online Learning Website",
        "Web Development",
        ["Adam", "Hana"],
        [81, 85, 79, 83]
    ),

    InnovationProject(
        "W002",
        "E-Commerce Website",
        "Web Development",
        ["Aiman", "Lisa"],
        [87, 84, 89, 86]
    ),

    InnovationProject(
        "W003",
        "Student Portal",
        "Web Development",
        ["Izzat", "Mira"],
        [75, 78, 73, 80]
    )
]


# Functional features

# Calculate average score for all projects
scores = list(
    map(lambda p: p.average_score(), project_list)
)

# Calculate overall average score
avg_score = sum(scores) / len(scores)


# Find projects with average score >= 80
top_projects = list(
    filter(
        lambda p: p.average_score() >= 80,
        project_list
    )
)


print(f"Average Team Score: {avg_score:.2f}")

print(
    "Top-Tier Projects:",
    [p.title for p in top_projects]
)


# Pandas Tactical Table

data = {
    "Project ID": [p.project_id for p in project_list],

    "Title": [p.title for p in project_list],

    "Category": [p.category for p in project_list],

    "Team Members": [
        ", ".join(p.team_members)
        for p in project_list
    ],

    "Average Score": [
        p.average_score()
        for p in project_list
    ],

    "Commercialization Potential": [
        p.commercialization_potential()
        for p in project_list
    ]
}


df = pd.DataFrame(data)


print("\n-- Project Details --")
print(df.to_string(index=False))


# Matplotlib Bar Chart

plt.bar(
    df["Project ID"],
    df["Average Score"]
)

plt.title("Innovation Project Average Scores")

plt.xlabel("Project ID")

plt.ylabel("Average Score")

plt.ylim(0, 100)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()