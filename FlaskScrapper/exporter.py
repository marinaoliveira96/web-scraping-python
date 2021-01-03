import csv 

def save_to_file(jobs):
  file = open('jobs.csv', mode='w')
  writer = csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'link'])
  for job in jobs:
    # dicionários tem método pra pegar só os valores
    writer.writerow(list(job.values()))
  return