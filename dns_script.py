import multiprocessing as mp
import subprocess

def resolve_dns(url):
    output = subprocess.check_output("geoiplookup %s" % url, shell=True)
    print("\nResolving domain", url, "\n", output, "\n////////////////////////////////////////")

if __name__ == '__main__':
    domainFile = open("domains.txt", "r") #opens the file in read mode
    domain_array = domainFile.read().splitlines() #puts the file into an array
    domainFile.close()

    n_processes = mp.cpu_count()
    with mp.Pool(processes = n_processes) as pool:
        pool.map(resolve_dns, [url for url in domain_array])
