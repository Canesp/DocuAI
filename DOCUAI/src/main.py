import os 

os.environ["test"] = "test"
t = os.getenv("test")

print(t)