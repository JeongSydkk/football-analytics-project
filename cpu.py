import multiprocessing as mp

def burn():
    while True:
        pass

if __name__ == "__main__":
    for i in range(mp.cpu_count()):
        mp.Process(target=burn).start()
