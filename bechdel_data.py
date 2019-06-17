import csv

import CreateData
from Bechdel import Bechdel

data = CreateData.CreateData()
movie_list = data.create_movie()
params = []

with open("bechdel_test_data", 'a') as csvFile:
    writer = csv.writer(csvFile)
    for movie in movie_list:
        tester = Bechdel(movie)
        tester.run_bechdel_test()
        params.append(movie.movie_name)
        params.append(tester.test1)
        params.append(tester.test2)
        params.append(tester.test3)
        params.append(tester.overall)
        writer.writerow(params)

csvFile.close()


