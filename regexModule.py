import re

str = "@article{kornuta2015robot,\n  title={Robot control system design exemplified by multi-camera visual servoing},\n  author={Kornuta, Tomasz and Zieli{\\'n}ski, Cezary},\n  journal={Journal of Intelligent \\& Robotic Systems},\n  volume={77},\n  number={3-4},\n  pages={499--523},\n  year={2015},\n  publisher={Springer}\n}\n"

patternTitle = r"title={(.*?)}"
result = re.findall(patternTitle, str, flags=0)
print(result)

patternAuthor = r"author={(.*?)}"
result = re.findall(patternAuthor, str, flags=0)
print(result)
