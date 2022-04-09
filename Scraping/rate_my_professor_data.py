"""

Open the pickled object, just read it.

"""

import pickle
from generate_rmp_data import RateMyProfScraper

if __name__ == "__main__":
    data = pickle.load(open("rmp_object.obj", "rb" ))
    print(data.SearchProfessor("Justin Wyss-Gallifent"))