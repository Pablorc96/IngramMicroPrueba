import multiprocessing as mp
import subprocess

def resolve_dns(url):
    output = subprocess.check_output("geoiplookup %s" % url, shell=True).decode("utf-8")
    result_string = "\nResolving domain" + str(url) + "\n" + output + "\n////////////////////////////////////////"
    print(result_string)

if __name__ == '__main__':
    domainFile = open("domains.txt", "r")
    domain_array = domainFile.read().splitlines()
    domainFile.close()

    n_processes = mp.cpu_count()
    with mp.Pool(processes = n_processes) as pool:
        pool.map(resolve_dns, [url for url in domain_array])
